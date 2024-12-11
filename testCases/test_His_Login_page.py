import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.customLogger import LogGen
from page_Objects.Page_Objects_HIS_Login_Page import His_Login_Page
import pandas as pd


class TestHISLoginPage:
    logger = LogGen.loggen()
    results = []

    @pytest.fixture(scope="class", autouse=True)
    def test_his_login_page(self, pandas_excel, browser_setup, execute_query):

        query = """SELECT TOP 1 *
                   FROM D_WebUser_LoginHistory
                   WHERE UserId = '6550'
                   ORDER BY LoginDateTime DESC;"""

        # Read the data from the Excel sheet
        data = pandas_excel('LoginData')
        url = data['Inputs'].iloc[0]
        username = data['Inputs'].iloc[1]
        password = data['Inputs'].iloc[2]
        print(url)
        self.driver = browser_setup
        self.login_page_object = His_Login_Page(self.driver)

        # Create a list for storing credentials and expected responses


        ###################### Logging and saving URL status ###############################
        self.logger.info("*********URL is invoked in the Browser*************")
        self.driver.get(url)

        if url:
            url_status = 'URL Loaded Successfully'
        else:
            url_status = 'URL Not Found or Empty'
        self.results.append(f'Expected Response: {url_status}')

        ###################### Logging and saving username status ###############################
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.login_page_object.xpath_for_his_LoginPage_UserName)))
        self.login_page_object.Enter_His_LoginPage_UserName(username)

        if username:
            username_status = 'Username entered Successfully'
        else:
            username_status = 'Failed to enter the Username'
        self.results.append(f'Expected Response: {username_status}')

        ###################### Logging and saving password status ###############################
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.login_page_object.xpath_for_his_LoginPage_Password)))
        self.login_page_object.Enter_His_LoginPage_Password(password)

        if password:
            password_status = 'Password entered Successfully'
        else:
            password_status = 'Failed to enter the Password'
        self.results.append(f'Expected Response: {password_status}')

        ###################### Clicking submit button ###############################
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.login_page_object.xpath_for_his_LoginPage_SubmitButton)))
        self.login_page_object.Click_His_LoginPage_Submit_button()

        ###################### Clicking Yes button in Pop up###############################
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.login_page_object.xpath_for_pop_up)))
        self.login_page_object.Click_yes_button_in_Pop_up()

        ###################### Capturing database results ###############################
        result = execute_query(query)
        for row in result:
            user_id = row[1]
            ip_address = row[2]
            login_time_date = row[4]
            db_status = f"UserID: {user_id}, IP Address: {ip_address}, Login Time: {login_time_date}"
            self.results.append(f'Expected Response: {db_status}')

        ###################### Writing the Results to a New Excel Sheet ###############################

        data['Expected Response'] = self.results
        output_file_path = r'C:\Users\manikanta\PycharmProjects\PythonTesting\HIS_POM_Pytest_Hybrid_framework\TestData\Output_One.xlsx'
        data.to_excel(output_file_path, index=False, sheet_name='LoginData')

        return self.results



