import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.customLogger import LogGen
from page_Objects.Page_Object_HIS_Direct_Receipt import HIS_Direct_receipt
import pandas as pd
from testCases.test_login_page_HIS import TestHIS_Login_Page


class TestDirectReceipt(TestHIS_Login_Page):
    def test_direct_receipt(self):
        option_name = 'Direct Receipt'

        self.direct_receipt = HIS_Direct_receipt(self.driver)
        wait = WebDriverWait(self.driver, 30)

        ###################### Select the Facility ###############################
        self.logger.info("*********Select the Facility*************")
        self.direct_receipt.select_facility()

        ###################### Click the  inventory option###############################
        self.logger.info("********* Click the  inventory option *************")
        self.direct_receipt.click_inventory_option()

        ###################### Click the  dropdown option ###############################
        self.logger.info("********* Click the  dropdown option in inventory pop up and click yes button*************")
        self.direct_receipt.select_options_from_inventory_dropdown()

        ###################### Click the  search field and enter the option name ###############################
        self.logger.info("********* Click the  search field and enter the option name *************")
        self.direct_receipt.click_indent_items_option(option_name)

        self.direct_receipt.click_direct_receipt_from_indent_items()

        self.direct_receipt.wait_for_the_page_header_Direct_receipt()
        time.sleep(20)


