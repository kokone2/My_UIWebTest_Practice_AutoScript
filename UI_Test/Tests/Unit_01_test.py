from selenium import webdriver
import unittest

class launchtest(unittest.TestCase) :

    def test_launch(self):

        base_url = "http://automationpractice.com/index.php"
        driver = webdriver.Chrome(executable_path=r"C:\Users\itzmezehel\class-qa\Driver\chromedriver.exe")

        driver.maximize_window()
        driver.get(base_url)

        assert "My Store" in driver.title

        driver.quit()

if __name__ == '__main__' :
    unittest.main()