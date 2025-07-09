import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.customLogger import LogGen
from page_Objects.Page_Objects_HIS_Login_Page import (His_Login_Page)
from page_Objects.Page_Objects_HIS_Front_Office import His_OutPatient_Registration
from testCases.test_login_page_HIS import TestHIS_Login_Page



@pytest.mark.usefixtures("browser_setup")
class TestHISFrontOffice(TestHIS_Login_Page):
    logger = LogGen.loggen()

    ################# Add Patient ##############
    def test_his_front_office_patient_registration(self, pandas_excel, browser_setup, test_his_login_page):
        self.driver = browser_setup
        data = pandas_excel('Front_Office')
        results = test_his_login_page

        ####### data driving from the excel sheet #################
        desired_option_Add_Patient = data['Add_Patient_Options'].iloc[0]
        title = "Mr."
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

        self.logger.info("*********Select Facility*************")
        self.his_home_object.select_facility()

        self.logger.info("*********Click the Front office option in His HomePage*************")
        self.his_home_object.Select_Front_Office_from_HIS_Homepage()

        self.logger.info("*********Click Yes Button in the Front Office Pop up*************")
        self.his_home_object.Click_yes_button_in_front_office_pop_up()

        self.logger.info("********* Click the add patient option *************")
        self.his_home_object.click_the_Add_patient()

        self.logger.info("********* Click any option under the add paitent option *************")
        self.his_home_object.select_an_option_from_add_patient(desired_option_Add_Patient)

        self.logger.info("********* Select a Title *************")
        self.his_home_object.enter_title(title)
        if title:
            title_entered = "title entered successfully"
        else:
            title_entered = "failed to enter title"
        output_data.append(f'Title:{title_entered}')

        self.logger.info("********* Fill the firstname *************")
        self.his_home_object.enter_first_name(firstname)
        if firstname:
            first_name_entered = "firstname entered successfully"
        else:
            first_name_entered = "failed to enter firstname"
        output_data.append(f'First_name:{first_name_entered}')

        self.logger.info("********* Select a Gender *************")
        self.his_home_object.select_a_gender(Gender)
        if Gender:
            gender_update = "Gender entered successfully"
        else:
            gender_update = "failed to enter Gender"
        output_data.append(f'Gender:{gender_update}')

        self.logger.info("********* Click the age *************")
        self.his_home_object.click_age(age)
        if age:
            age_entered = "Age entered Successfully"
        else:
            age_entered = "Failed to enter age"
        output_data.append(f'age:{age_entered}')

        self.logger.info("********* Select status of Marriage *************")
        self.his_home_object.select_marital_status(status_of_marriage)
        if status_of_marriage:
            marriage_status = "Marriage status selected"
        else:
            marriage_status = "Unable to record the marital status"
        output_data.append(f'marriage_Status:{marriage_status}')

        self.logger.info("********* Enter the mobile number *************")
        self.his_home_object.enter_mobile_number(mobile_number)
        if mobile_number:
            mobile_number_entered = "Mobile entered Successfully"
        else:
            mobile_number_entered = "Failed to enter mobile number"
        output_data.append(f'mobile_number:{mobile_number_entered}')

        self.logger.info("********* Enter Address *************")
        self.his_home_object.enter_house_number(house_number)
        if house_number:
            house_number_entered = "Entered house successfully"
        else:
            house_number_entered = "Failed to enter house address"
        output_data.append(f'house_number: {house_number_entered}')

        self.logger.info("********* Enter Locality *************")
        self.his_home_object.enter_locality(locality)
        if locality:
            locality_entered = "Entered locality success"
        else:
            locality_entered = "Entered locality success"
        output_data.append(f'locality: {locality_entered}')

        self.logger.info("********* Enter source option *************")
        self.his_home_object.enter_source(source_option)
        if source_option:
            source_option_entered = "Source Option Entered Successfully"
        else:
            source_option_entered = "Failed to enter Source Option"
        output_data.append(f'source_option: {source_option_entered}')

        self.logger.info("********* Click register button *************")
        self.his_home_object.click_register_button()


        self.logger.info("********* Patient Details *************")
        patient_details = self.driver.find_element(By.XPATH,
                                                   self.his_home_object.xpath_for_patient_details_in_confirm_patient_details)
        output_data.append(patient_details.text)
        print(patient_details.text)

        self.logger.info("********* Save Patient Details *************")
        self.his_home_object.confirmation_pop_up(yes_or_no)
        if yes_or_no:
            yes_or_no_option = "Clicked yes or no button"
        else:
            yes_or_no_option = "Failed to click yes or no button"
        output_data.append(f'yes_or_no_option:{yes_or_no_option}')

        self.logger.info("********* Successful message *************")
        successful_message = self.driver.find_element(By.XPATH,
                                                      self.his_home_object.xpath_for_successful_message)
        output_data.append(successful_message.text)

        self.logger.info("********* Registration Successful Pop up *************")
        self.his_home_object.Registered_Successfully_pop_up(option_yes_or_no)
        if option_yes_or_no:
            yes_or_no_option = "Clicked either yes or no"
        else:
            yes_or_no_option = "failed to click either yes or no"


        time.sleep(10)


