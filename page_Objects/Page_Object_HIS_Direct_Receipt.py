from pyodbc import drivers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class HIS_Direct_receipt:
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
        # self.xpath_for_Indent_Items = f"//li//ul//li//a[text()='{self.search_field_option}']"
        self.xpath_for_indent_items = "//ul[@class='mainList']//li[@class='nav-item']//a//span[text()='Indent Items']"
        # self.xpath_for_indent_items_list = "//ul[@class='mainList']//li[@class='nav-item']//ul[@class='sidebar-second-level collapse']"
        # self.xpath_for_direct_receipt = "//a[text()='Direct Receipt']"
        self.xpath_for_direct_receipt_page_heading = "//h2[@class='page_heading']"
        self.xpath_for_indent_menu = "//ul[@id='collapseComponents']//li/a"
        self.xpath_for_tabs = "//div//ul[@class='nav nav-tabs']//li"
        self.xpath_for_options_under_medicine_tab = "//table[@id='TblMedicine']//tbody//tr//td[1]"
        self.xpath_for_options_under_consumables_tab = "//table[@id='TblConsumables']//tbody//tr//td[1]"
        self.xpath_for_options_under_others_tab = "//table[@id='TblOther']//tbody//tr//td[1]"
        self.xpath_for_table_2 = "//table[@id='tblgrid']"
        self.xpath_for_table_2_elements = "//table[@id='tblgrid']//tbody//tr"
        self.xpath_for_Quantity_in_table_2 = "//table[@id='tblgrid']//tbody//tr//td[6]//input[@type='text']"
        self.xpath_for_remarks = "//textarea[@id='txtnewremark']"
        self.xpath_for_calculate = "//a[@id='btncalculate']"
        self.xpath_for_total = "//input[@id='txttotal']"
        self.xpath_for_save = "//div//a[@id='btnsave']"
        self.xpath_for_hor_scroll = "//div[@class='direct-table']"
        self.xpath_for_delete_pop_up = "//div[@id='DRDeleterow']//div[@id='popup280']"
        self.xpath_for_yes_button_in_delete_pop_up = "//div[@id='DRDeleterow']//div[@id='popup280']//footer//span//a[@id='btnDeleteYes']"
        self.xpath_for_vertical_scroll = "//div[contains(@class, 'direct-table') and contains(@style, 'overflow: auto')]//table[@id='tblgrid']"
        self.xpath_for_save_pop_up = "(//div[@id='popup280'])[3]"
        self.xpath_for_yes_button_in_save_pop_up = "(//div[@id='popup280'])[3]//span//a[@id='btnSaveYes']"

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

    def click_indent_items_option(self, option_name):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_indent_items)))
        click_indent = self.driver.find_element(By.XPATH, self.xpath_for_indent_items)
        click_indent.click()

    def click_direct_receipt_from_indent_items(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_indent_menu)))
        items_list = self.driver.find_elements(By.XPATH, self.xpath_for_indent_menu)
        for option in items_list:
            if option.text.strip() == "Direct Receipt":
                option.click()

    def wait_for_the_page_header_Direct_receipt(self):
        # self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_direct_receipt_page_heading)))
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_tabs)))
        three_tabs = self.driver.find_elements(By.XPATH, self.xpath_for_tabs)






