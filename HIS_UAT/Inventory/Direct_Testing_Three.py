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


class Receipt_Direct:
    def __init__(self):
        self.driver = None

    def read_an_excel_file(self):
        file_path = "C:\\Users\\10013887\\PycharmProjects\\Testing_Repo\\Excel_Test_Data\\Inventory_Test_Data.xlsx"
        data = pd.read_excel(file_path, sheet_name='LoginPage')
        data_one = pd.read_excel(file_path, sheet_name='Inventory')
        data_two = pd.read_excel(file_path, sheet_name='Direct_Receipt_Medicines')
        url = data['Input'].iloc[0]
        username = data['Input'].iloc[1]
        password = data['Input'].iloc[2]
        facility_option = data_one['Inputs'].iloc[0]
        main_menu_option = data_one['Inputs'].iloc[1]
        drop_down_option = data_one['Inputs'].iloc[2]
        footer_option = data_one['Inputs'].iloc[3]
        search_field_option = data_one['Inputs'].iloc[4]
        medicines = data_two['Medicines_List']
        item_quantity = data_two['Quantity']
        batch_list = data_two['Batch_numbers']
        expiry_date = data_two['Expiry_Date']

        table2_quantity = []
        for items in item_quantity:
            table2_quantity.append(items)

        batch_numbers = []
        for batches in batch_list:
            batch_numbers.append(batches)

        expiry_date_list = []
        for expiry_dates in expiry_date:
            expiry_date_list.append(expiry_dates)

        return url, username, password, main_menu_option, drop_down_option, footer_option, search_field_option, medicines, table2_quantity, batch_numbers, expiry_date_list, facility_option

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
        xpath_for_pop_up = "(//div[@id='popup650'])[2]"
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

    def direct_update(self, main_menu_option, drop_down_option, footer_option, search_field_option, medicines,
                      table2_quantity, batch_numbers, expiry_date_list):

        self.main_menu_option = main_menu_option
        self.drop_down_option = drop_down_option
        self.footer_option = footer_option
        self.search_field_option = search_field_option
        self.medicines = medicines
        self.table2_quantity = table2_quantity
        self.batch_numbers = batch_numbers
        self.expiry_date_list = expiry_date_list

        # Sanitizing/Normalizing data appropriately before processing
        medicines_list = [medicine.strip() for medicine in self.medicines]  # Apply strip to each medicine

        quantity = []
        for quantity_in_table2 in self.table2_quantity:
            quantity.append(quantity_in_table2)

        batch_number = []
        for batch in self.batch_numbers:
            batch_number.append(batch)

        date = []
        for expiry_date in self.expiry_date_list:
            date.append(expiry_date)

        xpath_for_all_the_options_in_His = "//section//ul[@id='da-thumbs']//li"
        xpath_for_inventory_dropdown = "//div[@id='popup280']"
        xpath_for_dropdown_values_of_inventory_pop_up = "//select[@id='Department']"
        xpath_for_footer_in_inventory_pop_up = "//div[@id='popup280']//footer//a"
        xpath_for_search_field_in_inventory = "//input[@id='nav-search']"
        xpath_for_Indent_Items = f"//a[text()='{self.search_field_option}']"
        xpath_for_tabs = "//div//ul[@class='nav nav-tabs']//li"
        xpath_for_options_under_medicine_tab = "//table[@id='TblMedicine']//tbody//tr//td[@style='text-align: left;']"
        xpath_for_options_under_consumables_tab = "//table[@id='TblConsumables']//tbody//tr//td[1]"
        xpath_for_options_under_others_tab = "//table[@id='TblOther']//tbody//tr//td[1]"
        xpath_for_table_2 = "//table[@id='tblgrid']"
        xpath_for_table_2_elements = "//table[@id='tblgrid']//tbody//tr"
        xpath_for_Quantity_in_table_2 = "//table[@id='tblgrid']//tbody//tr//td[6]//input[@type='text']"
        xpath_for_remarks = "//textarea[@id='txtnewremark']"
        xpath_for_calculate = "//a[@id='btncalculate']"
        xpath_for_total = "//input[@id='txttotal']"
        xpath_for_save = "//div//a[@id='btnsave']"
        xpath_for_hor_scroll = "//div[@class='direct-table']"
        xpath_for_delete_pop_up = "//div[@id='DRDeleterow']//div[@id='popup280']"
        xpath_for_yes_button_in_delete_pop_up = "//div[@id='DRDeleterow']//div[@id='popup280']//footer//span//a[@id='btnDeleteYes']"
        xpath_for_vertical_scroll = "//div[contains(@class, 'direct-table') and contains(@style, 'overflow: auto')]//table[@id='tblgrid']"
        xpath_for_save_pop_up = "(//div[@id='popup280'])[3]"
        xpath_for_yes_button_in_save_pop_up = "(//div[@id='popup280'])[3]//span//a[@id='btnSaveYes']"

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
        print(Indent_item.text)
        self.driver.execute_script("arguments[0].click();", Indent_item)

        ############### wait and locate the 3tabs ###############################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_tabs)))
        three_tabs = self.driver.find_elements(By.XPATH, xpath_for_tabs)

        for tab in three_tabs:
            if tab.text.strip() == 'Medicine':
                tab.click()
                medicine_options = self.driver.find_elements(By.XPATH, xpath_for_options_under_medicine_tab)

                # Get text of all available options
                medicine_text_set = {option.text.strip() for option in medicine_options}

                # Iterate only over the medicines you want to match
                for medicine in medicines_list:
                    if medicine in medicine_text_set:
                        print(f"'{medicine}' found in the list!")
                        # You can also click the element here if needed:
                        for option in medicine_options:
                            if option.text.strip() == medicine:
                                self.driver.execute_script("arguments[0].click();", option)
                                break
                        time.sleep(20)
                    else:
                        print(f"'{medicine}' not found.")

        ############### Start an empty list ###############################
        # selected_option_in_table_2 = []



        ###############Retriving each and every medicine/items name from the medicines list###############################
        # for unique_medicine in medicines_list:
            # Flag to break outer tab loop once the medicine is found
            # medicine_found = False
            # # Iterating through the 3 tabs
            # for tab in three_tabs:
            #     tab_text = tab.text.strip()  # Removing the blank spaces using the strip and storing the text of the tabs (Medicine, Consumables and Others into a variable called tab_text
            #     if medicine_found:
            #         break  # Exit the tab loop once the medicine is found
            #
            #     if tab_text == "Medicine":  # if text in the tab_text matches with Medicine then click the Medicine tab
            #         tab.click()
            #         wait.until(expected_conditions.visibility_of_element_located(
            #             (By.XPATH, xpath_for_options_under_medicine_tab)))  # wait for the options under medicine tab
            #         items = self.driver.find_elements(By.XPATH,
            #                                           xpath_for_options_under_medicine_tab)  # locate and store all the medicines inside a variable called items
            #         print(f"Iterating through '{tab_text}'")
            #     elif tab_text == "Consumables":  # if text in the tab_text matches with Consumables then click the Consumables tab
            #         tab.click()
            #         wait.until(expected_conditions.visibility_of_element_located(
            #             (By.XPATH,
            #              xpath_for_options_under_consumables_tab)))  # wait for the options under consumables tab
            #         items = self.driver.find_elements(By.XPATH,
            #                                           xpath_for_options_under_consumables_tab)  # locate and store all the consumables inside a variable called items
            #         print(f"Iterating through '{tab_text}'")
            #     elif tab_text == "Others":  # if text in the tab_text matches with Others then click the Consumables tab
            #         tab.click()
            #         wait.until(expected_conditions.visibility_of_element_located(
            #             (By.XPATH, xpath_for_options_under_others_tab)))  # wait for the options under Others tab
            #         items = self.driver.find_elements(By.XPATH,
            #                                           xpath_for_options_under_others_tab)  # locate and store all the other items inside a variable called items
            #         print(f"Iterating through '{tab_text}'")
            #     else:
            #         continue
            #     ###############Iterate through the all the items stored in the item variable using for loop###############################
            #     for option in items:
            #         options = option.text.strip()  # remove the blanks before and after the text of every option and store the text inside a variable called options
            #         print(options)
            #         break

batch_modifier = Receipt_Direct()
url, username, password, main_menu_option, drop_down_option, footer_option, search_field_option, medicines, table2_quantity, batch_numbers, expiry_date_list, facility_option = batch_modifier.read_an_excel_file()
batch_modifier.login_page(url, username, password, facility_option)
batch_modifier.direct_update(main_menu_option, drop_down_option, footer_option, search_field_option, medicines,
                             table2_quantity, batch_numbers, expiry_date_list)