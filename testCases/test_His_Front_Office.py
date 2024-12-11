import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.customLogger import LogGen
from page_Objects.Page_Objects_HIS_Login_Page import (His_Login_Page)
from page_Objects.Page_Objects_HIS_Front_Office import His_OutPatient_Registration
from testCases.test_His_Login_page import TestHISLoginPage


@pytest.mark.usefixtures("browser_setup")
class TestHISFrontOffice(TestHISLoginPage):
    logger = LogGen.loggen()

    ################# Add Patient ##############
    def test_his_front_office_patient_registration(self, pandas_excel, browser_setup, test_his_login_page):
        self.driver = browser_setup
        data = pandas_excel('Front_Office')
        results = test_his_login_page
        print(results)

        ####### data driving from the excel sheet #################
        desired_option_Add_Patient = data['Add_Patient_Options'].iloc[0]
        firstname = data['Inputs'].iloc[0]
        Gender = data['Inputs'].iloc[1]
        age = str(data['Inputs'].iloc[2])
        status_of_marriage = data['Inputs'].iloc[3]
        mobile_number = str(data['Inputs'].iloc[8])
        house_number = str(data['Inputs'].iloc[9])
        locality = data['Inputs'].iloc[10]
        source_option = data['Inputs'].iloc[11]
        yes_or_no = data['Inputs'].iloc[13]
        option_yes_or_no = data['Inputs'].iloc[14]
        output_data = []

        ######### storing the pageobject class name inside a variable ############
        self.his_home_object = His_OutPatient_Registration(self.driver)

        ######### Initializing the wait ##########################################
        wait = WebDriverWait(self.driver, 30)
        ############ Selecting the facility option in home page ##################
        self.his_home_object.select_facility(self.driver)
        ###################### Wait until Front office option is located #########################
        self.logger.info("*********Wait until Front office option is located*************")
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.his_home_object.xpath_for_front_office)))

        ###################### Clicking Front option in His HomePage ###############################
        self.logger.info("*********Click the Front office option in His HomePage*************")
        self.his_home_object.Select_Front_Office_from_HIS_Homepage()

        ###################### Wait until Front office pop up is located  ###############################
        self.logger.info("*********Wait until Front office pop up is located*************")
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.his_home_object.xpath_for_front_office_pop_up)))

        ###################### Click Yes Button in the Front Office Pop up  ###############################
        self.logger.info("*********Click Yes Button in the Front Office Pop up*************")
        self.his_home_object.Click_yes_button_in_front_office_pop_up()

        ################## Wait to identify the add patient locator and click the add paitent option ############
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.his_home_object.xpath_for_add_patient)))
        self.his_home_object.click_the_Add_patient()

        ################## Wait to identify and click any option under the add paitent option ############
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.his_home_object.xpath_for_all_options_under_Add_Patient)))
        self.his_home_object.select_an_option_from_add_patient(desired_option_Add_Patient)

        # for index, row in data.iterrows(index=False):
        ################## Wait to identify and fill the first name ##################################
        wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, self.his_home_object.xpath_for_First_name)))
        self.his_home_object.enter_first_name(firstname)

        if firstname:
            first_name_update = "firstname entered successfully"
        else:
            first_name_update = "failed to enter firstname"

        output_data.append(f'Expected Response:{first_name_update}')
        # results.append(f'{firstname} is captured')

        ################## Wait to identify and select the gender name ##################################
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.his_home_object.xpath_for_Gender)))
        self.his_home_object.select_a_gender(Gender)

        if Gender:
            Gender_update = "Gender entered successfully"
        else:
            Gender_update = "failed to enter Gender"

        output_data.append(f'Expected Response:{Gender_update}')

        ################## Wait to identify and click the DOB ##################################
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.his_home_object.xpath_for_age)))
        self.his_home_object.click_age(age)

        if age:
            output_data.append(f'Expected Response:{age}')
        else:
            output_data.append(f'Expected Response:{age}')

        ################## Wait to identify and click the marital status ##################################
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.his_home_object.xpath_for_marital_status)))
        self.his_home_object.select_marital_status(status_of_marriage)
        if status_of_marriage:
            marriage_status = "Marriage status selected"
        else:
            marriage_status = "Unable to record the marital status"
        output_data.append(f'Expected Response:{marriage_status}')

        # output_data.append(results)
        for option in results:
            output_data.append(option)

        ################## Wait to identify and enter the mobile number ##################################
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.his_home_object.xpath_for_mobile_number)))
        self.his_home_object.enter_mobile_number(mobile_number)
        if mobile_number:
            output_data.append(f'Expected Response:{mobile_number}')
        else:
            output_data.append(f'Expected Response:{mobile_number}')

        ################## Wait to identify and enter the House address ##################################
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.his_home_object.xpath_for_House_address)))
        self.his_home_object.enter_house_number(house_number)
        if house_number:
            output_data.append(f'Expected Response:{house_number}')
        else:
            output_data.append(f'Expected Response:{house_number}')

        ################## Wait to identify and enter the Locality ##################################
        wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, self.his_home_object.xpath_for_Locality)))
        self.his_home_object.enter_locality(locality)
        if locality:
            output_data.append(f'Expected Response:{locality}')
        else:
            output_data.append(f'Failed to enter {locality}')

        ################## Wait to identify and enter the source ##################################
        wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, self.his_home_object.xpath_for_source)))
        self.his_home_object.enter_source(source_option)
        if source_option:
            output_data.append(f'Expected Response:{source_option}')
        else:
            output_data.append(f'Failed to enter {source_option}')

        ################## Wait to identify and click the register button ##################################
        wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, self.his_home_object.xpath_for_source)))
        self.his_home_object.click_register_button()

        ################## Wait to identify and click the confirmation ##################################
        wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, self.his_home_object.xpath_for_confirm_patient_details)))
        patient_details = self.driver.find_element(By.XPATH,
                                                   self.his_home_object.xpath_for_patient_details_in_confirm_patient_details)

        output_data.append(patient_details.text)

        self.his_home_object.confirmation_pop_up(yes_or_no)
        if yes_or_no:
            output_data.append(f'Expected Response:{yes_or_no}')
        else:
            output_data.append(f'No option to click')

        ################## Wait to identify and click the confirmation ##################################
        wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, self.his_home_object.xpath_for_Registered_successfully)))
        successful_message = self.driver.find_element(By.XPATH,
                                                      self.his_home_object.xpath_for_successful_message)

        self.his_home_object.Registered_Successfully_pop_up(option_yes_or_no)
        if yes_or_no:
            output_data.append(f'Expected Response:{option_yes_or_no}')
        else:
            output_data.append(f'No option to click')

        output_data.append(successful_message.text)

        time.sleep(10)

        ###################### Writing the Results to a New Excel Sheet ###############################

        data['Expected results'] = output_data
        output_file_path = r'C:\Users\manikanta\PycharmProjects\PythonTesting\HIS_POM_Pytest_Hybrid_framework\TestData\Patient_Registration.xlsx'
        data.to_excel(output_file_path, index=False, sheet_name='Front_Office')

    # @pytest.mark.skip(reason='its an email automator')
    ##### Automatic mail sender ###########
    def test_email_sending(self, email_manager):
        recipients = ["cheryshma.nadimpalli@aighospitals.com",
                      "rajat.atri@aighospitals.com",
                      "manikantha.ponduru@aighospitals.com", ]  # "gaurav.mojasia@aighospitals.com", "kinjal.saxena@aighospitals.com"
        subject = "Automation Test Email of HIS-UAT"
        body = "The Test Automation Team has executed the UAT HIS Test Automation, and this report details the outcomes."
        attachment_path = r'C:\Users\manikanta\PycharmProjects\PythonTesting\HIS_POM_Pytest_Hybrid_framework\TestData\Patient_Registration.xlsx'
        # Test with attachment
        email_manager(recipients, subject, body, attachment_path=attachment_path)
