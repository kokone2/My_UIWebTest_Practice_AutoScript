from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest

base_url = "http://automationpractice.com/index.php"
username = "extract1234@yopmail.com"
password = "12345"

class LoginTest(unittest.TestCase) :

    def test_login(self):

        self.driver = webdriver.Chrome(executable_path=r"C:\Users\itzmezehel\class-qa\Driver\chromedriver.exe")

        self.driver.maximize_window()
        self.driver.get(base_url)

        WebDriverWait(self.driver,300).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a.login"))).click()

        WebDriverWait(self.driver,300).until(EC.element_to_be_clickable((By.ID,"email"))).send_keys(username)
        WebDriverWait(self.driver,300).until(EC.element_to_be_clickable((By.ID,"passwd"))).send_keys(password)
        WebDriverWait(self.driver,300).until(EC.element_to_be_clickable((By.ID,"SubmitLogin"))).click()

        element = WebDriverWait(self.driver,300).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"h1.page-heading")))
        assert "MY ACCOUNT" == element.text

        self.driver.quit()

if __name__=='__main__' :
    unittest.main()