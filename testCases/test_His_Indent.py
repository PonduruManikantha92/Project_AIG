import time

import pytest
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.customLogger import LogGen
from page_Objects.Page_Object_HIS_Indent_Items import HIS_Indents
from testCases.test_login_page_HIS import TestHIS_Login_Page


class TestIndent(TestHIS_Login_Page):

    ##### """Fixture to read and return Indent_Items data once per class""" #########
    @pytest.fixture(scope='class')
    def indent_data(self, pandas_excel):
        # Load once, reuse
        data_one = pandas_excel('Indent_Items')
        data_two = pandas_excel('Indent_Issue')
        return {'items': data_one, 'issue': data_two}

    def test_indent_indents(self, indent_data, test_his_login_page):
        driver = test_his_login_page
        option_name = indent_data['items']['option_name'].iloc[0]
        facility_name = indent_data['items']['facility_name'].iloc[0]
        department_name = indent_data['items']['Department_name'].iloc[0]

        indent_items = (HIS_Indents(driver))

        self.logger.info("*********Select the Facility*************")
        indent_items.select_facility()
        self.logger.info("*******Click Inventory Option********")
        indent_items.click_inventory_option()
        self.logger.info("*******Select_options_from_inventory_dropdown*******")
        indent_items.select_options_from_inventory_dropdown()
        self.logger.info("*******Indent_options_select*******")
        indent_items.Indent_options_select(option_name)
        self.logger.info("*******select_facility_and_Department*******")
        indent_items.select_facility_and_Department(facility_name, department_name)
        self.logger.info("********search_and_click_indent_items********")
        for index, row in indent_data['items'].iterrows():
            search_text = str(row['search_text'])
            indent_items.search_and_click_indent_items(search_text)
        self.logger.info("********select_items_from_table2********")
        for index, row in indent_data['items'].iterrows():
            value = str(row['value'])
            indent_items.select_items_from_table2(str(value))

        self.logger.info("******save_indent_items******")
        indent_items.save_indent_items()

    def test_indent_approval(self, indent_data, test_his_login_page):
        driver = test_his_login_page
        indent_approval = (HIS_Indents(driver))
        option_name_indent_approval = indent_data['items']['option_name'].iloc[1]

        self.logger.info("********click the menu icon********")
        indent_approval.click_show_menu_icon()
        self.logger.info("********click_indent_approval********")
        indent_approval.indent_approval()

    def test_indent_issue(self, indent_data, test_his_login_page):
        driver = test_his_login_page
        indent_issue = (HIS_Indents(driver))
        self.logger.info("*******indent_issue*******")
        indent_issue.indent_issue()

    def test_indent_item_receipt(self, indent_data, test_his_login_page):
        driver = test_his_login_page
        indent_item_receipt = (HIS_Indents(driver))
        self.logger.info("*******indent_item_receipt*******")
        indent_item_receipt.indent_item_receipt()
        time.sleep(20)


