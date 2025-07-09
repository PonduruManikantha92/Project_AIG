import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.customLogger import LogGen
from page_Objects.Page_Object_HIS_Indent_Items import HIS_Indents
import pandas as pd
from testCases.test_login_page_HIS import TestHIS_Login_Page


class TestIndent(TestHIS_Login_Page):
    def test_indent_indents(self, pandas_excel):
        data_one  = pandas_excel('Indent_Items')
        option_name = data_one['option_name'].iloc[0]
        facility_name = data_one['facility_name'].iloc[0]
        department_name = data_one['Department_name'].iloc[0]

        ########## Indent Approval ######################
        data_one = pandas_excel('Indent_Items')
        option_name_indent_approval = data_one['option_name'].iloc[1]

        self.indent_items = (HIS_Indents(self.driver))

        self.logger.info("*********Select the Facility*************")
        self.indent_items.select_facility()
        self.logger.info("*******Click Inventory Option********")
        self.indent_items.click_inventory_option()
        self.logger.info("*******Select_options_from_inventory_dropdown*******")
        self.indent_items.select_options_from_inventory_dropdown()
        self.logger.info("*******Indent_options_select*******")
        self.indent_items.Indent_options_select(option_name)
        self.logger.info("*******select_facility_and_Department*******")
        self.indent_items.select_facility_and_Department(facility_name, department_name)
        self.logger.info("********search_and_click_indent_items********")
        for index, row in data_one.iterrows():
            search_text = str(row['search_text'])
            self.indent_items.search_and_click_indent_items(search_text)
        self.logger.info("********select_items_from_table2********")
        for index, row in data_one.iterrows():
            value = str(row['value'])
            self.indent_items.select_items_from_table2(str(value))

        self.logger.info("******save_indent_items******")
        self.indent_items.save_indent_items()
        time.sleep(10)

        ########## Indent Approval ######################

        self.indent_approval = (HIS_Indents(self.driver))
        self.indent_approval.click_show_menu_icon()
        self.indent_approval.indent_approval(option_name_indent_approval)
        time.sleep(15)




