from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner

import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir + '\Resources')
sys.path.insert(0, parentdir + '\Resources\PageObjects')

from PracTestData import TestData
from PracLocators import Locators
from PracPages import HomePage, AuthenticationPage, VideoPage


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=TestData.CHROME_PATH)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


class HomePageTest(BaseTest):

    def test_launch(self):
        """Test Case untuk launch URL"""

        # Membuat objek kelas HomePage
        self.homePage = HomePage(self.driver)

        # Mengambil page title dari HomePage
        title = self.homePage.get_title()

        # Verifikasi title page
        assert TestData.WEB_TITLE in title

    def test_login(self):
        """Test Case untuk login"""

        # Membuuat objek kelas HomePage
        self.homePage = HomePage(self.driver)

        # Mengeklik tombol Sign In
        self.homePage.signin()

        # Membuat objek kelas AuthenticationPage
        self.authenticationPage = AuthenticationPage(self.homePage.driver)

        # Mengisi email, password, dan mngeklik tombol Sign In
        self.authenticationPage.signin_registered()

    def test_video(self):
        # Membuuat objek kelas HomePage
        self.homePage = HomePage(self.driver)

        # Membuat objek kelas VideoPage
        self.videoPage = VideoPage(self.homePage.driver)

        # Mencari video
        self.videoPage.find_play_video()

    def test_watch_later(self):
        # Menambah ke watch later
        self.videoPage.watch_later()

        # Mengambil judul dari watch list
        element1 = self.videoPage.get_text(Locators.WATCH_LATER_VIDEO_TITLE)

        # Verifikasi video sudah terdaftar di list
        assert TestData.VIDEO_TITLE == element1


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(open_in_browser=True,
                                                           output='report'))
