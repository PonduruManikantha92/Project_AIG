from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class His_User_Registration:
    def __init__(self, driver):
        self.driver = driver
        self.xpath_for_facility_dropdown = "//select[@id='Facility']"
        self.xpath_for_facility_option = "//option[text()='AIG Hospitals, Gachibowli']"
        self.xpath_for_masters_option_in_home_page = "//li[.//div/span[normalize-space(text())='Masters']]"
        self.xpath_for_Masters_pop_up = "//div[@id='popup280']"
        self.xpath_for_yes_button_in_Masters_Pop_up = "//a[@id='btn_yes_desh']"
        self.xpath_for_search_field_in_Masters = "//input[@placeholder='Search']"
        self.xpath_for_User_Access_under_User_Access_in_Master = "(//li[@id='lstWorkList']/a[contains(@href, '/HisTraining/Masters/UserAccess/UserAccess')])[1]"
        # UAT useraccess xpath  "(//li[@id='lstWorkList']/a[contains(@href, '/HisTraining/Masters/UserAccess/UserAccess')])[1]"
        # PROD useraccess xpath  "(//li[@id='lstWorkList']/a[contains(@href, '/Histree/Masters/UserAccess/UserAccess')])[1]"
        self.xpath_for_Name_in_user_access = "//input[@id='txtname']"
        self.xpath_for_Login_name_in_user_access = "//input[@id='txtloginname']"
        self.xpath_for_Password_in_user_access = "//input[@id='tatpassword']"
        self.xpath_for_Confirm_Password_in_user_access = "//input[@id='txtconfrmpass']"
        self.xpath_for_Interface_ID_in_user_access = "//input[@id='txtinterfaceid']"
        self.xpath_for_save_button_in_user_access = "(//i[@class='fa fa-save'])[1]"
        self.xpath_for_save_confirmation_pop_up_in_user_access = "(//div[@id='popup280'])[3]"
        # UAT useraccess xpath "(//div[@id='popup280'])[3]"
        # Prod useraccess xpath "(//div[@id='popup280'])[2]"
        self.xpath_for_yes_button_in_save_pop_in_user_access = "//a[@id='btnyesuser']"
        self.xpath_for_department_names_in_user_access = "//select[@id='ddldepartment']"
        self.xpath_for_mobile_number_in_user_access = "//input[@id='txtContactNo']"

        ############ Xpath for Password Reset in Masters #################################################
        self.xpath_for_search_id_login_name = "//input[@id='txtsearchlogin']"
        self.xpath_for_pop_up_for_login_name = "//div[@id='popup650']"
        self.xpath_for_password_locked_checkbox = "//input[@id='chklockpass']"
        self.xpath_for_update_button = "//a[@title='Update']"
        self.xpath_for_modification_pop_up = "(//div[@id='popup280'])[4]"
        self.xpath_for_yes_button_in_pop_up = "//a[@id='btnyeupdateuser']"

    def select_facility(self, driver):
        facility_dropdown = self.driver.find_element(By.XPATH, self.xpath_for_facility_dropdown)
        facility_option = self.driver.find_element(By.XPATH, self.xpath_for_facility_option)
        wait = WebDriverWait(driver, 30)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_facility_dropdown)))
        facility_dropdown.click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.xpath_for_facility_option)))
        facility_option.click()

    def click_masters(self):
        masters_option = self.driver.find_element(By.XPATH, self.xpath_for_masters_option_in_home_page)
        masters_option.click()

    def click_yes_button_in_masters_pop_up(self):
        yes_option = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_Masters_Pop_up)
        yes_option.click()

    def search_option_in_masters(self, search_option_name):
        search_field_option = self.driver.find_element(By.XPATH, self.xpath_for_search_field_in_Masters)
        search_field_option.send_keys(search_option_name)

    def click_the_user_access_option(self):
        click_user_access = self.driver.find_element(By.XPATH, self.xpath_for_User_Access_under_User_Access_in_Master)
        click_user_access.click()

    def enter_name_in_user_access(self, Name):
        enter_name = self.driver.find_element(By.XPATH, self.xpath_for_Name_in_user_access)
        enter_name.send_keys(Name)

    def enter_login_name_in_user_access(self, LoginName):
        login_name = self.driver.find_element(By.XPATH, self.xpath_for_Login_name_in_user_access)
        login_name.send_keys(LoginName)

    def enter_password_in_user_access(self, Password):
        password = self.driver.find_element(By.XPATH, self.xpath_for_Password_in_user_access)
        password.send_keys(Password)

    def enter_confirm_password_in_user_access(self, Confirm_Password):
        con_password = self.driver.find_element(By.XPATH, self.xpath_for_Confirm_Password_in_user_access)
        con_password.send_keys(Confirm_Password)

    def enter_interface_id(self, Interface_ID):
        interface_id_path = self.driver.find_element(By.XPATH, self.xpath_for_Interface_ID_in_user_access)
        interface_id_path.send_keys(Interface_ID)

    def enter_department_names(self, Department):
        department_option = self.driver.find_element(By.XPATH, self.xpath_for_department_names_in_user_access)

        # Initialize the Select class
        department_dropdown = Select(department_option)

        for option in department_dropdown.options:
            if option.text.strip().upper() == Department.upper():  # Case-insensitive match
                option.click()
                print(f"Selected: {option.text}")
                break

    def enter_mobile_number(self, Mobile_number):
        contact = self.driver.find_element(By.XPATH, self.xpath_for_mobile_number_in_user_access)
        contact.send_keys(Mobile_number)

    def click_save_button(self):
        save_button = self.driver.find_element(By.XPATH, self.xpath_for_save_button_in_user_access)
        save_button.click()

    def click_yes_button_in_save_pop_up(self):
        yes_button = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_save_pop_in_user_access)
        yes_button.click()

    ################# password reset in User Access #######################################

    def enter_login_name(self, login_id):
        enter_name = self.driver.find_element(By.XPATH, self.xpath_for_search_id_login_name)

        enter_name.send_keys(login_id)

    def click_user_login_id_in_Pop_up(self, user_id):
        xpath_for_user_login_id = f"//tr[@class='clsclick']/td[text()='{user_id}']"
        login_id = self.driver.find_element(By.XPATH, xpath_for_user_login_id)
        login_id.click()

    def click_the_check_box_to_uncheck(self):
        check_box = self.driver.find_element(By.XPATH, self.xpath_for_password_locked_checkbox)
        if check_box:
            check_box.click()
        else:
            check_box.clear()

    def click_the_update_button(self):
        update_button = self.driver.find_element(By.XPATH, self.xpath_for_update_button)
        update_button.click()

    def click_the_yes_button_in_pop_up(self):
        yes_button = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_pop_up)
        yes_button.click()
