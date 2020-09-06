from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
import allure

class TestAllure:
    def test_Logo(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\User\\PycharmProjects\\PythonUnitTestPOMBased\\drivers\\chromedriver.exe")
        self.driver.maximize_window()

        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status=self.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()

        if status==True:
            assert True
        else:
            assert False
        self.driver.close()
    @allure.severity(allure.severity_level.NORMAL)
    def test_SkippingTest(self):
        pytest.skip("Skipping the test")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\User\\PycharmProjects\\PythonUnitTestPOMBased\\drivers\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Veera")
        self.driver.find_element_by_id("txtPassword").send_keys("Pulapakura")
        self.driver.find_element_by_id("btnLogin").click()


        status=self.driver.title

        if status=="OrangeCRM":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="LogintestGetTitle",attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False




