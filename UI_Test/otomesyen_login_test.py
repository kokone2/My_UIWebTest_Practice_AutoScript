from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

base_url = "https://www.youtube.com/"
username = "ユアネス-yourness-「籠の中に鳥」Official Music Video【アニメ「イエスタデイをうたって」主題歌】"
password = "Search All - MyAnimeList.net"
driver = webdriver.Chrome(executable_path=r"C:\Users\itzmezehel\class-qa\Driver\chromedriver.exe")

driver.maximize_window()
driver.get(base_url)

WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input#search.ytd-searchbox"))).send_keys(username)
WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.ID,"search-icon-legacy"))).click()
WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#video-title > yt-formatted-string"))).click()
