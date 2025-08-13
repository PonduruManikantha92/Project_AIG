import time
from csv import excel_tab

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class HIS_Indents:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.xpath_for_facility_dropdown = "//select[@id='Facility']"
        self.xpath_for_facility_option = "//option[text()='AIG Hospitals, Gachibowli']"
        self.xpath_for_inventory_option = "//li[.//div/span[normalize-space(text())='Inventory']]"
        self.xpath_for_inventory_pop_up = "//div[@id='popup280']"
        self.xpath_for_inventory_option_dropdown = "//select[@id='Department']"
        self.xpath_for_yes_button_in_inventory_pop_up = "//a[@id='btn_yes_desh']"
        self.xpath_for_search_field_in_inventory = "//input[@id='nav-search']"
        self.xpath_for_indent_items_option = "//a[text()='Indent Items']"
        self.xpath_for_indent_facility = "//select[@id='ddlToFacility']"
        self.xpath_for_department = "//select[@id='ddlToDepartment']"
        self.xpath_for_indent_search = "//input[@id='TxtItemSearch']"
        self.tabs = {
                "Medicine" : "//li[@id='liMedicine']",
                "Consumables" : "//li[@id='liConsumables']",
                "Others" : "//li[@id='liOthers']",
                "Order_set" : "//li[@id='liOrderSet']",
                "CSSD" : "//li[@id='liCSSD']"
        }

        self.result_xpath_template = "//div[contains(text(), '{search_text}')]"  # change accordingly
        self.xpath_for_selected_items = "//table[@id='tblSelectedItem']//tbody//tr"
        self.xpath_for_save_button = "(//div//a[@title='Save']//i[@class='fa fa-save'])[1]"
        self.xpath_for_save_button_pop_up = "(//div[@id='popup280'])[1]"
        self.xpath_for_yes_in_save_pop_up = "//a[@id='btnYes']"

        ################## Indent Approval #####################
        self.xpath_for_showmenu = "//a[@id='showmenu']"
        self.xpath_for_indent_items_tab = "//span[normalize-space()='Indent Items']"
        self.xpath_for_indent_approval =  "//ul/li//a[text()='Indent Approval']"
        self.xpath_for_new_indent = "//label[text()='New Indent']"
        self.xpath_for_new_indent_pop_up =  "(//div[@id='popup900'])[1]"
        self.xpath_for_items_in_table = "(//table[@id='newitemreceipt']//tbody)[1]"
        self.xpath_for_approve_button = "//a[@id='btnApprove']"
        self.xpath_for_approve_this_indent_pop_up = "(//div[@id='popup280'])[1]"
        self.xpath_for_yes_button_in_approve_this_indent_pop_up = "//span//a[@id='btnyes']"
        self.xpath_for_3_bars = "//img[@id='showmenuIcon']"
        self.xpath_for_home_button_after_clicking_3_bars = "//a[normalize-space()='HOME']"
        self.xpath_for_home_button = "//img[@id='showmenuIcon1']"

        ################## Indent issue #####################
        self.xpath_for_indent_issue_option = "//span[normalize-space()='Indent Issue']"
        self.xpath_for_items_under_indent_issue = "//ul[@id='collapseMulti2']"
        self.xpath_for_indent_issue_option_one = "//a[@href='/HisTraining/Inventory/IndentIssue']"
        self.xpath_for_new_button = "//span[normalize-space() ='New']"
        self.xpath_for_indent_issue_pop_up = "(//section[@class='popupBody'])[2]"
        self.xpath_for_first_element_in_indent_issue_pop_up = "(//tr[@class='context-menu-IsUnlock'])[1]"
        self.xpath_for_save_button_in_indent_issue = "//a[@id='btnSave']/i[@class='fa fa-save']"
        self.xpath_for_save_pop_in_indent_issue = "(//div[@id='popup280'])[1]"
        self.xpath_for_yes_button_in_indent_issue_save_pop_up = "//a[@id='btnYes']"
        self.xpath_for_print_report_pop_up = "(//div[@id='popup280'])[1]"
        self.xpath_for_yes_button_in_print_report_pop_up = "//a[@id='btnNo']"

        ################## Indent Item Receipt #####################
        self.xpath_for_indent_item_receipt = "//a[normalize-space()='Item Receipt']"
        self.xpath_for_new_receipt = "//span//input[@id='radNewReceipt']"
        self.xpath_for_new_receipt_pop_up_in_item_receipt = "//section[@class='popupBody pt-1']"
        self.xpath_for_item_receipt_table_pop_up_item = "(//td[@onclick='HIS.ItemReceipt.bindfooterTable(97881,87815,201,7,1)'])[1]"
        self.xpath_for_save_button_in_item_receipt = "//li//div[@id='userfunction']//a//i[@class='fa fa-save']"



    ################## Indent Items #####################
    def select_facility(self):
        facility_dropdown = self.driver.find_element(By.XPATH, self.xpath_for_facility_dropdown)
        facility_option = self.driver.find_element(By.XPATH, self.xpath_for_facility_option)
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_facility_dropdown)))
        facility_dropdown.click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_facility_option)))
        facility_option.click()

    def click_inventory_option(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_inventory_option)))
        inventory = self.driver.find_element(By.XPATH, self.xpath_for_inventory_option)
        inventory.click()

    def select_options_from_inventory_dropdown(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_inventory_option_dropdown)))
        inventory_dropdown_option = self.driver.find_element(By.XPATH, self.xpath_for_inventory_option_dropdown)
        inventory_ops = Select(inventory_dropdown_option)
        for i in inventory_ops.options:
            if i.text.strip() == 'A-3-HDU 1':
                i.click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_yes_button_in_inventory_pop_up)))
        yes_Button = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_inventory_pop_up)
        yes_Button.click()

    def Indent_options_select(self, option_name):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_search_field_in_inventory)))
        search_field = self.driver.find_element(By.XPATH, self.xpath_for_search_field_in_inventory)
        search_field.send_keys(option_name)
        option_under_indent_items = self.driver.find_element(By.XPATH, self.xpath_for_indent_items_option)
        self.driver.execute_script("arguments[0].click();", option_under_indent_items)

    def select_facility_and_Department(self, facility_name, department_name):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_indent_facility)))
        indent_facility = self.driver.find_element(By.XPATH, self.xpath_for_indent_facility)
        facility_option = Select(indent_facility)
        for option in facility_option.options:
            if option.text.strip() == facility_name:
                option.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_department)))
        self.wait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "modal")))
        dept_name = self.driver.find_element(By.XPATH, self.xpath_for_department)
        indent_department_name = Select(dept_name)
        for dept_option in indent_department_name.options:
            if dept_option.text.strip() == department_name:
                dept_option.click()

    def search_and_click_indent_items(self, search_text):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_indent_search)))
        options_under_tab_xpath = f"//td[contains(normalize-space(text()), '{search_text.strip()}')]"

        for tab_name, tab_xpath in self.tabs.items():
            self.wait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "modal")))
            self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, tab_xpath)))
            tab_element = self.driver.find_element(By.XPATH, tab_xpath)
            tab_element.click()
            try:
                self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, options_under_tab_xpath)))
                option_name = self.driver.find_element(By.XPATH, options_under_tab_xpath)
                option_name.click()
                break
            except Exception as e:
                print(f"{search_text} not found in {tab_name} tab. Trying next tab.")
                continue

    def select_items_from_table2(self, input_value):
        selected_items_table = self.driver.find_elements(By.XPATH, self.xpath_for_selected_items)
        xpath_for_value = "//td[@ctype='QTY']"
        for option in selected_items_table:
            try:
                # Find the <input> inside the <td ctype="QTY">
                input_elem = option.find_element(By.XPATH, ".//td[@ctype='QTY']//input")

                # Check if it's enabled and visible
                if input_elem.is_displayed() and input_elem.is_enabled():
                    input_elem.clear()
                    input_elem.send_keys(input_value)
                else:
                    print("Input not interactable.")
            except Exception as e:
                print(f"Error interacting with QTY input: {e}")

    def save_indent_items(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_save_button)))
        save_button = self.driver.find_element(By.XPATH, self.xpath_for_save_button)
        save_button.click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_save_button_pop_up)))
        yes_button_save_pop_up = self.driver.find_element(By.XPATH, self.xpath_for_yes_in_save_pop_up)
        yes_button_save_pop_up.click()


    ################## Indent Approval #####################

    def click_show_menu_icon(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_showmenu)))
        show_menu_icon = self.driver.find_element(By.XPATH, self.xpath_for_showmenu)
        show_menu_icon.click()

    def indent_approval(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_indent_items_tab)))
        indent_items_tab = self.driver.find_element(By.XPATH, self.xpath_for_indent_items_tab)
        indent_items_tab.click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_indent_approval)))
        indent_approval = self.driver.find_element(By.XPATH, self.xpath_for_indent_approval)
        self.driver.execute_script("arguments[0].click();", indent_approval)
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_new_indent)))
        new_indent_option = self.driver.find_element(By.XPATH, self.xpath_for_new_indent)
        new_indent_option.click()
        new_indent_pop_up = self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_new_indent_pop_up)))
        new_indent_pop_up.click()
        # self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_items_in_table)))
        # table_item = self.driver.find_element(By.XPATH, self.xpath_for_items_in_table)
        # # table_item.click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_approve_button)))
        approve_button = self.driver.find_element(By.XPATH, self.xpath_for_approve_button)
        approve_button.click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_approve_this_indent_pop_up)))
        yes_button_approve = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_approve_this_indent_pop_up)
        yes_button_approve.click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_home_button)))
        home_button = self.driver.find_element(By.XPATH, self.xpath_for_home_button)
        home_button.click()

    ################## Indent Issue #####################
    def indent_issue(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_inventory_option)))
        inventory_option = self.driver.find_element(By.XPATH, self.xpath_for_inventory_option)
        inventory_option.click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_inventory_option_dropdown)))
        inventory_dropdown_option = self.driver.find_element(By.XPATH, self.xpath_for_inventory_option_dropdown)
        inventory_ops = Select(inventory_dropdown_option)
        for i in inventory_ops.options:
            if i.text.strip() == 'A-B1- PHARMACY MAIN STORE':
                i.click()
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.xpath_for_yes_button_in_inventory_pop_up)))
        yes_Button = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_inventory_pop_up)
        yes_Button.click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_indent_issue_option)))
        indent_issue = self.driver.find_element(By.XPATH, self.xpath_for_indent_issue_option)
        indent_issue.click()
        # Wait for submenu <ul> to appear
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//ul[@id='collapseMulti2']")))

        # Click "Indent Issue" link
        indent_issue_link = self.driver.find_element(By.XPATH, "//ul[@id='collapseMulti2']/li[1]/a")
        indent_issue_link.click()

        self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_new_button)))
        new_button = self.driver.find_element(By.XPATH, self.xpath_for_new_button)
        new_button.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_indent_issue_pop_up)))
        first_element = self.driver.find_element(By.XPATH, self.xpath_for_first_element_in_indent_issue_pop_up)
        first_element.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_save_button_in_indent_issue)))
        save_button_in_indent_issue = self.driver.find_element(By.XPATH, self.xpath_for_save_button_in_indent_issue)
        save_button_in_indent_issue.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_save_pop_in_indent_issue)))
        yes_button_indent_save_pop_up = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_indent_issue_save_pop_up)
        yes_button_indent_save_pop_up.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_print_report_pop_up)))
        yes_button_print_report_pop_up = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_print_report_pop_up)
        yes_button_print_report_pop_up.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_3_bars)))
        three_bars_indent_issue = self.driver.find_element(By.XPATH, self.xpath_for_3_bars)
        three_bars_indent_issue.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_home_button_after_clicking_3_bars)))
        home_button_indent_issue = self.driver.find_element(By.XPATH, self.xpath_for_home_button_after_clicking_3_bars)
        home_button_indent_issue.click()

    def indent_item_receipt(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_inventory_option)))
        inventory_option = self.driver.find_element(By.XPATH, self.xpath_for_inventory_option)
        inventory_option.click()
        self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_inventory_option_dropdown)))
        inventory_dropdown_option = self.driver.find_element(By.XPATH, self.xpath_for_inventory_option_dropdown)
        inventory_ops = Select(inventory_dropdown_option)
        for i in inventory_ops.options:
            if i.text.strip() == 'A-3-HDU 1':
                i.click()
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.xpath_for_yes_button_in_inventory_pop_up)))
        yes_Button = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_inventory_pop_up)
        yes_Button.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_indent_items_tab)))
        indent_items_tab = self.driver.find_element(By.XPATH, self.xpath_for_indent_items_tab)
        indent_items_tab.click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_indent_item_receipt)))
        item_receipt = self.driver.find_element(By.XPATH, self.xpath_for_indent_item_receipt)
        self.driver.execute_script("arguments[0].click();", item_receipt)

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_new_receipt)))
        new_receipt_in_item_receipt = self.driver.find_element(By.XPATH, self.xpath_for_new_receipt)
        new_receipt_in_item_receipt.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_new_receipt_pop_up_in_item_receipt)))
        item_in_table = self.driver.find_element(By.XPATH, self.xpath_for_item_receipt_table_pop_up_item)
        item_in_table.click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_save_button_in_item_receipt)))
        save_button_item_receipt = self.driver.find_element(By.XPATH, self.xpath_for_save_button_in_item_receipt)
        save_button_item_receipt.click()



