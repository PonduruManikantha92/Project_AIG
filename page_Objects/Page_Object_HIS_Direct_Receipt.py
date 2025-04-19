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






