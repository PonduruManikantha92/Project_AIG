import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.customLogger import LogGen
from page_Objects.Page_Objects_HIS_Login_Page import (His_Login_Page)
from page_Objects.Page_Objects_HIS_Front_Office import His_OutPatient_Registration
from page_Objects.Page_Objects_HIS_Front_Office_Billing import His_OP_Billing
from testCases.conftest import browser_setup
from testCases.test_login_page_HIS import TestHIS_Login_Page



@pytest.mark.usefixtures("browser_setup")
class TestHISFrontOffice(TestHIS_Login_Page):
    logger = LogGen.loggen()
    uhid = 'AIGG.20727250'
    Doctor_name = 'Rakesh Kalapala'
    refer = 'aig'
    Discount_on_option = 'On Bill'
    Discount_head = 'Corporate Discount'
    Discount_reason = 'Corporate Discount'
    Discount_percentage = '10'
    Authorized_By = 'CAPRI JALOTA'

    def test_his_op_billing_discount(self, browser_setup):
        self.driver = browser_setup
        self.front_office_option = His_OutPatient_Registration(self.driver)
        self.front_office_billing  = His_OP_Billing(self.driver)
        ######### Select a Facility #####################
        self.logger.info("******************Select a Facility******************")
        self.front_office_option.select_facility()
        self.driver.save_screenshot(".\\Screenshots\\facility_selected.png")

        ######### Select Front Office Option #####################
        self.logger.info("******************Select Front Office Option******************")
        self.front_office_option.Select_Front_Office_from_HIS_Homepage()
        self.driver.save_screenshot(".\\Screenshots\\selecting_front_office_option.png")

        ######### Click_yes_button_in_front_office_pop_up #####################
        self.logger.info("***************Click_yes_button_in_front_office_pop_up*********************")
        self.front_office_option.Click_yes_button_in_front_office_pop_up()
        self.driver.save_screenshot(".\\Screenshots\\Click_yes_button_in_front_office_pop_up.png")

        ######### Options_under_home_in_billing #####################
        self.logger.info("*************** Options_under_home_in_billing*********************")
        self.front_office_billing.options_under_home_in_billing()
        self.driver.save_screenshot(".\\Screenshots\\Select_billing_option.png")

        ######### Enter the UHID #####################
        self.logger.info("*************** Enter the UHID *********************")
        self.front_office_billing.enter_the_uhid(self.uhid)
        self.driver.save_screenshot(".\\Screenshots\\enter_uhid.png")

        ######### Search for Doctors Name #####################
        self.logger.info("*************** Search for Doctors name *********************")
        self.front_office_billing.search_for_doctor_name(self.Doctor_name)
        self.driver.save_screenshot(".\\Screenshots\\searching_for_doc_name.png")

        ######### Referred By#####################
        self.logger.info("*************** Referred By *********************")
        self.front_office_billing.refered_by(self.refer)
        self.driver.save_screenshot(".\\Screenshots\\Referred_By.png")

        ######### Clicking add to bill#####################
        self.logger.info("*************** Clicking add to bill *********************")
        self.front_office_billing.click_add_to_bill()
        self.driver.save_screenshot(".\\Screenshots\\click_add_to_bill.png")

        ######### Close the deposit pop up#####################
        self.logger.info("*************** Close the deposit pop up *********************")
        self.front_office_billing.close_the_deposit_pop_up()
        self.driver.save_screenshot(".\\Screenshots\\close_the_deposit_pop_up.png")

        #########Click  yes button in discount pop up#####################
        self.logger.info("*************** Click  yes button in discount pop up *********************")
        self.front_office_billing.click_yes_button_in_discount_pop()
        self.driver.save_screenshot(".\\Screenshots\\click_yes_button_in_discount_pop_up.png")

        ######### Process Discount #####################
        self.logger.info("*************** Process Discount *********************")
        self.front_office_billing.process_discount(self.Discount_on_option, self.Discount_head, self.Discount_reason, self.Discount_percentage, self.Authorized_By)
        self.driver.save_screenshot(".\\Screenshots\\click_yes_button_in_discount_pop_up.png")

        ######### Clicking the billing option #####################
        self.logger.info("*************** Clicking the billing option  *********************")
        self.front_office_billing.click_the_billing_option()
        self.driver.save_screenshot(".\\Screenshots\\Clicking_the_billing_option ")

        time.sleep(2)
        ######### Generate Bill Pop up #####################
        self.logger.info("*************** Generate Bill Pop up  *********************")
        self.front_office_billing.generate_bill_pop_up()
        self.driver.save_screenshot(".\\Screenshots\\Generate_Bill_Pop_up")

        time.sleep(2)
        #########Process Payment #####################
        self.logger.info("*************** Process Payment  *********************")
        self.front_office_billing.process_payment()
        self.driver.save_screenshot(".\\Screenshots\\Generate_Bill_Pop_up")

        time.sleep(2)
        #########Print the Bill #####################
        self.logger.info("*************** Print the Bill  *********************")
        self.front_office_billing.print_the_bill()
        self.driver.save_screenshot(".\\Screenshots\\print_the_bill")

        time.sleep(10)







