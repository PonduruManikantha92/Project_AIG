import re
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Adjustments:
    def __init__(self):
        self.driver = None

    def read_an_excel_file(self):
        file_path = "C:\\Users\\10013887\\PycharmProjects\\Testing_Repo\\Excel_Test_Data\\Inventory_Test_Data.xlsx"
        data = pd.read_excel(file_path, sheet_name='LoginPage')
        data_one = pd.read_excel(file_path, sheet_name='Inventory')
        data_two = pd.read_excel(file_path, sheet_name='Adjustments')
        url = data['Input'].iloc[0]
        username = data['Input'].iloc[1]
        password = data['Input'].iloc[2]
        facility_option = data_one['Inputs'].iloc[0]
        main_menu_option = data_one['Inputs'].iloc[1]
        drop_down_option = data_one['Inputs'].iloc[2]
        footer_option = data_one['Inputs'].iloc[3]
        search_field_option = data_one['Inputs'].iloc[4]
        adjustment_type = data_two['Inputs'].iloc[0]
        search_options = data_two['Search_Options']
        batch_Adjustments = data_two['Batch']

        search_option_list = []
        for options in search_options:
            search_option_list.append(options)

        batch_number_list = []
        for options in batch_Adjustments:
            batch_number_list.append(options)

        return url, username, password, main_menu_option, drop_down_option, footer_option, search_field_option, facility_option, adjustment_type, search_option_list, batch_number_list

    def login_page(self, url, username, password, facility_option):
        self.driver = webdriver.Chrome()

        ############### Credentials ###############################
        self.url = url
        self.username = username
        self.password = password
        self.facility = facility_option
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        ############### login page xpaths ###############################
        xpath_for_his_LoginPage_UserName = "//input[@id='txtLoginName']"
        xpath_for_his_LoginPage_Password = "//input[@id='txtPassword']"
        xpath_for_his_LoginPage_SubmitButton = "//input[@value='Login']"
        xpath_for_pop_up = "(//div[@id='popup650'])[3]"
        xpath_for_yes_button_in_active_session_pop_up = "//a[@id='btnYesAlreadyLogedinPopup']"
        xpath_for_facility_option = "//select[@id='Facility']"


        ############### Initializing wait ###############################
        wait = WebDriverWait(self.driver, 30)
        ############### Waiting and entering the username ###############################
        user_name = self.driver.find_element(By.XPATH, xpath_for_his_LoginPage_UserName)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_his_LoginPage_UserName)))
        user_name.send_keys(self.username)

        ############### Waiting and entering the password ###############################
        pass_word = self.driver.find_element(By.XPATH, xpath_for_his_LoginPage_Password)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_his_LoginPage_Password)))
        pass_word.send_keys(self.password)

        ############### Waiting and clicking the submit button ###############################
        submit_button = self.driver.find_element(By.XPATH, xpath_for_his_LoginPage_SubmitButton)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_his_LoginPage_SubmitButton)))
        submit_button.click()

        ############### Waiting and clicking the Yes button in Pop up ###############################
        yes_button = self.driver.find_element(By.XPATH, xpath_for_yes_button_in_active_session_pop_up)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_pop_up)))
        yes_button.click()

        ############### Waiting and clicking the facility dropdown ###############################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_facility_option)))
        f_option = self.driver.find_element(By.XPATH, xpath_for_facility_option)
        facility = Select(f_option)
        for option in facility.options:
            if option.text.strip() == self.facility:
                option.click()

        time.sleep(5)

    def adjustments_func(self, main_menu_option, drop_down_option, footer_option, search_field_option, adjustment_type, search_option_list, batch_number_list):
        self.main_menu_option = main_menu_option
        self.drop_down_option = drop_down_option
        self.footer_option = footer_option
        self.search_field_option = search_field_option
        self.adjustment_type = adjustment_type
        self.search_options = search_option_list
        self.batch_number = batch_number_list

        adjustment_options = []
        for options_in_adjustments in self.search_options:
            adjustment_options.append(options_in_adjustments)

        batch_numbers = []
        for options_in_batch_number in self.batch_number:
            batch_numbers.append(options_in_batch_number)

        ############### Adjustment page page xpaths ###############################
        xpath_for_all_the_options_in_His = "//section//ul[@id='da-thumbs']//li"
        xpath_for_inventory_dropdown = "//div[@id='popup280']"
        xpath_for_dropdown_values_of_inventory_pop_up = "//select[@id='Department']"
        xpath_for_footer_in_inventory_pop_up = "//div[@id='popup280']//footer//a"
        xpath_for_search_field_in_inventory = "//input[@id='nav-search']"
        xpath_for_Indent_Items = f"//li//ul//li//a[text()='{self.search_field_option}']"
        xpath_for_adjustment_type = "//select[@id='ddlAdjust']"
        xpath_for_tick_mark = "//i[@id='fafatick']"
        xpath_for_search_option_in_adjustment = "//input[@id='search']"
        xpath_for_options_under_the_adjustment_items = "//table[@id='Adjustmnttabl']//tbody//tr"

        ############### Initializing wait ###############################
        wait = WebDriverWait(self.driver, 30)

        ############### Wait and select option from the Main page ###############################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_all_the_options_in_His)))
        all_options = self.driver.find_elements(By.XPATH, xpath_for_all_the_options_in_His)
        for option in all_options:
            if option.text.strip() == self.main_menu_option:
                option.click()
                break

        ############### Wait and select option from the inventory dropdown ###############################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_inventory_dropdown)))
        inventory_dropdown_values = self.driver.find_element(By.XPATH,
                                                             xpath_for_dropdown_values_of_inventory_pop_up)
        dropdown_values = Select(inventory_dropdown_values)
        for options in dropdown_values.options:
            if options.text.strip() == self.drop_down_option:
                options.click()
                break

        ############### wait and select "Yes" or "No" from the Inventory Pop up ###############################
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_footer_in_inventory_pop_up)))
        footer_locator_in_inventory_pop_up = self.driver.find_elements(By.XPATH,
                                                                       xpath_for_footer_in_inventory_pop_up)
        for button in footer_locator_in_inventory_pop_up:
            if button.text.strip() == self.footer_option:
                button.click()
                break
            elif button.text.strip() == self.footer_option:
                button.click()
                break
            else:
                print("No options found in footer")
                break

        ############### wait and enter option into the search field ###############################
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_search_field_in_inventory)))
        search_field = self.driver.find_element(By.XPATH, xpath_for_search_field_in_inventory)
        search_field.send_keys(self.search_field_option)

        ############### wait and click the Indent Item ###############################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_Indent_Items)))
        Indent_item = self.driver.find_element(By.XPATH, xpath_for_Indent_Items)
        Indent_item.click()

        ############### wait and click the Adjustment type ###############################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_adjustment_type)))
        adjustment = self.driver.find_element(By.XPATH, xpath_for_adjustment_type)
        adjustment_type = Select(adjustment)
        for option in adjustment_type.options:
            if option.text.strip() == self.adjustment_type:
                option.click()

        ############### wait and click the Tick mark ###############################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_tick_mark)))
        Tick_mark = self.driver.find_element(By.XPATH, xpath_for_tick_mark)
        Tick_mark.click()

        ############### wait and record the values inside the variable ###############################
        list_of_items = []

        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, xpath_for_options_under_the_adjustment_items)))
        items = self.driver.find_elements(By.XPATH, xpath_for_options_under_the_adjustment_items)
        for item in items:
            list_of_items.append(item.text)

        for elements in adjustment_options:
            if elements in list_of_items:
                for item in items:
                    if item.text == elements:
                        item.click()

        
        # xpath_for_druglist = "//table[@id='tbldrugdtaillist']//tbody//tr//td[text()='1302059']"
        # click_on_the_medicine = self.driver.find_element(By.XPATH, xpath_for_druglist)
        # click_on_the_medicine.click()

        time.sleep(15)









adjustments_inventory = Adjustments()
url, username, password, main_menu_option, drop_down_option, footer_option, search_field_option, facility_option, adjustment_type, search_option_list, batch_number_list  = adjustments_inventory.read_an_excel_file()
adjustments_inventory.login_page(url, username, password, facility_option)
adjustments_inventory.adjustments_func(main_menu_option, drop_down_option, footer_option, search_field_option, adjustment_type,search_option_list, batch_number_list)