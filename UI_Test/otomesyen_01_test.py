from selenium import webdriver

base_url = "https://myanimelist.net/"
driver = webdriver.Chrome(executable_path=r"C:\Users\itzmezehel\class-qa\Driver\chromedriver.exe")

driver.maximize_window()
driver.get(base_url)

assert "MyAnimeList.net - Anime and Manga Database and Community" in driver.title

driver.quit()

