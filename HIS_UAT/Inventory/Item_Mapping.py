import re
import time
from turtledemo.penrose import start

import pandas as pd
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Item_Mapping:
    def __init__(self):
        self.driver = None

    def read_an_excel_file(self):
        file_path = "C:\\Users\\10013887\\PycharmProjects\\Testing_Repo\\Excel_Test_Data\\Inventory_Test_Data.xlsx"
        data = pd.read_excel(file_path, sheet_name='LoginPage')
        data_one = pd.read_excel(file_path, sheet_name='Inventory')
        data_two = pd.read_excel(file_path, sheet_name='Direct_Receipt_Medicines')
        data_three = pd.read_excel(file_path, sheet_name='Item_Mapping')

        url = data['Input'].iloc[0]
        username = data['Input'].iloc[1]
        password = data['Input'].iloc[2]
        facility_option = data_one['Inputs'].iloc[0]
        main_menu_option = data_one['Inputs'].iloc[1]
        drop_down_option = data_one['Inputs'].iloc[2]
        footer_option = data_one['Inputs'].iloc[3]
        search_field_option = data_one['Inputs'].iloc[4]
        medicines = data_two['Medicines_List']
        item_code = data_three['Item_Code']

        items_code_list = []
        for option in item_code:
            items_code_list.append(option)

        return url, username, password, main_menu_option, drop_down_option, footer_option, search_field_option, medicines, facility_option, items_code_list

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

    def mapping(self, main_menu_option, drop_down_option, footer_option, search_field_option, items_code_list):
        self.main_menu_option = main_menu_option
        self.drop_down_option = drop_down_option
        self.footer_option = footer_option
        self.search_field_option = search_field_option
        self.item_code = items_code_list

        xpath_for_all_the_options_in_His = "//section//ul[@id='da-thumbs']//li"
        xpath_for_inventory_dropdown = "//div[@id='popup280']"
        xpath_for_dropdown_values_of_inventory_pop_up = "//select[@id='Department']"
        xpath_for_footer_in_inventory_pop_up = "//div[@id='popup280']//footer//a"
        xpath_for_search_field_in_inventory = "//input[@id='nav-search']"
        xpath_for_Indent_Items = f"//li//ul//li//a[text()='{self.search_field_option}']"
        xpath_for_Holding_stores = "(//select[@class='required'])[1]"
        xpath_for_Item_Code = "(//select[@class='required'])[2]"
        xpath_for_unchecked_items = "//span[@class='items-chbox']//input[@type='checkbox']"
        xpath_for_table_one = "//div[@class='table-border itgm-table']"
        xpath_for_table_body = "//div[@class='table-border itgm-table']//tbody"
        xpath_for_items_in_table_body = "//table[@id='tblIteams']//tbody//tr"
        xpath_for_item_mapping = "//table[@id='tblIteams']//tbody//tr//td"
        xpath_for_select_all_items = "(//div[@class='itgm-input2']//span//input[@type='checkbox'])[4]"
        xpath_for_select_all_wards = "(//div[@class='itgm-input2']//span//input[@type='checkbox'])[5]"
        xpath_for_select_all_consumptions = "(//div[@class='itgm-input2']//span//input[@type='checkbox'])[6]"
        xpath_for_save_button = "//div[@class='user_sp_menu']//a[@id='saveitem']//i[@class='fa fa-save']"
        xpath_for_save_successfully_message = "//div[@id='gritter-notice-wrapper]"
        xpath_for_close_save_message = "//div[@class='gritter-close']"

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

        ############### wait and select the holding items ###############################


        ############### wait and select the Item Code ###############################
        for options in items_code_list:
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_Holding_stores)))
            stores = self.driver.find_element(By.XPATH, xpath_for_Holding_stores)
            holding_store = Select(stores)
            for option in holding_store.options:
                if option.text == self.drop_down_option:
                    option.click()
            print(options)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_Item_Code)))
            items = self.driver.find_element(By.XPATH, xpath_for_Item_Code)
            items_code = Select(items)
            all_options = items_code.options
            for option in all_options:
                if option.text == options:
                    print(option.text)
                    option.click()
                    time.sleep(3)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_select_all_items)))
                    select_items = self.driver.find_element(By.XPATH, xpath_for_select_all_items)
                    select_items.click()
                    time.sleep(3)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_select_all_wards)))
                    select_wards = self.driver.find_element(By.XPATH, xpath_for_select_all_wards)
                    select_wards.click()
                    time.sleep(3)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_select_all_consumptions)))
                    select_cosumptions = self.driver.find_element(By.XPATH, xpath_for_select_all_consumptions)
                    select_cosumptions.click()
                    time.sleep(3)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_save_button)))
                    save_button = self.driver.find_element(By.XPATH, xpath_for_save_button)
                    save_button.click()
                    time.sleep(3)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_close_save_message)))
                    close_button = self.driver.find_element(By.XPATH, xpath_for_close_save_message)
                    close_button.click()
                    time.sleep(10)


        time.sleep(30)

items_map = Item_Mapping()
url, username, password, main_menu_option, drop_down_option, footer_option, search_field_option, medicines, facility_option,items_code_list = items_map.read_an_excel_file()
items_map.login_page(url, username, password, facility_option)
items_map.mapping(main_menu_option, drop_down_option, footer_option, search_field_option, items_code_list)

