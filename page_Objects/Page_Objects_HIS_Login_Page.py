from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class His_Login_Page:
    def __init__(self,  driver):     # This is the constructor method for the class
        self.driver = driver  # This line assigns the passed driver argument to an instance variable self.driver. This makes the WebDriver available to the rest of the methods in the His_Login_Page class
        self.xpath_for_his_LoginPage_UserName = "//input[@id='txtLoginName']"
        self.xpath_for_his_LoginPage_Password = "//input[@id='txtPassword']"
        self.xpath_for_his_LoginPage_SubmitButton = "//input[@value='Login']"
        self.xpath_for_pop_up = "(//div[@id='popup650'])[2]"
        self.xpath_for_yes_button_in_active_session_pop_up = "//a[@id='btnYesAlreadyLogedinPopup']"

    def Enter_His_LoginPage_UserName(self, username):
        try:
            user_name = self.driver.find_element(By.XPATH, self.xpath_for_his_LoginPage_UserName)
            user_name.send_keys(username)
            self.driver.save_screenshot(".\\Screenshots\\" + "Enter_His_LoginPage_UserName.png")
        except Exception as e:
            self.driver.save_screenshot(".\\Screenshots\\" + "Enter_His_LoginPage_UserName.png")

    def Enter_His_LoginPage_Password(self, password):
        try:
            pass_word = self.driver.find_element(By.XPATH, self.xpath_for_his_LoginPage_Password)
            pass_word.send_keys(password)
            self.driver.save_screenshot(".\\Screenshots\\" + "Enter_His_LoginPage_Password.png")
        except Exception as e:
            self.driver.save_screenshot(".\\Screenshots\\" + "Enter_His_LoginPage_Password.png")

    def Click_His_LoginPage_Submit_button(self):
        try:
            submit_button = self.driver.find_element(By.XPATH, self.xpath_for_his_LoginPage_SubmitButton)
            submit_button.click()
            self.driver.save_screenshot(".\\Screenshots\\" + "Click_His_LoginPage_Submit_button.png")
        except Exception as e:
            self.driver.save_screenshot(".\\Screenshots\\" + "Click_His_LoginPage_Submit_button.png")

    def Click_yes_button_in_Pop_up(self):
        try:
            yes_button = self.driver.find_element(By.XPATH, self.xpath_for_yes_button_in_active_session_pop_up)
            yes_button.click()
            self.driver.save_screenshot(".\\Screenshots\\" + "Click_yes_button_in_Pop_up.png")
        except Exception as e:
            self.driver.save_screenshot(".\\Screenshots\\" + "Click_yes_button_in_Pop_up.png")




