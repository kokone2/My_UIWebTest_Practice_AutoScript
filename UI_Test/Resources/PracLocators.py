from selenium.webdriver.common.by import By

class Locators():
    # --- Home Page Locators ---
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "ytd-button-renderer.style-scope.ytd-masthead.style-suggestive.size-small")

    # --- Authentication Page Locators ---
    REGISTERED_EMAIL_INPUT = (By.ID, "identifierId")
    EMAIL_NEXT_BUTTON = (By.ID,"identifierNext")
    REGISTERED_PASSWORD_INPUT = (By.ID, "password")
    PASS_NEXT_BUTTON = (By.ID, "passwordNext")
    PROFILE_BUTTON = (By.ID, "avatar-btn")

    # --- Setting Dark Mode Locators ---
    SETTING_BUTTON = (By.CSS_SELECTOR,"#buttons > ytd-topbar-menu-button-renderer:nth-child(3)")
    DARK_MODE_MENU = (By.CSS_SELECTOR,"ytd-toggle-theme-compact-link-renderer.style-scope.yt-multi-page-menu-section-renderer")
    DARK_MODE_TOGGLE = (By.CSS_SELECTOR,"paper-toggle-button.style-scope.ytd-toggle-item-renderer")

    # --- Search Video Locators ---
    SEARCH_TEXT_INPUT = (By.CSS_SELECTOR,"input#search.ytd-searchbox")
    SEARCH_BUTTON = (By.ID,"search-icon-legacy")
    SELECT_SONG = (By.CSS_SELECTOR,"#video-title > yt-formatted-string")
    THEATER_MODE = (By.CSS_SELECTOR,"button.ytp-size-button.ytp-button")

    # --- Watch Later Locators ---
    WATCH_LATER_ADD = (By.CSS_SELECTOR,"yt-icon-button#button.style-scope.ytd-button.renderer.style-default.size-default")
    WATCH_LATER_CHECKBOX = (By.ID,"checkboxContainer")
    WATCH_LATER_CHECKBOX_CLOSE = (By.ID,"close-button")
    GUIDE_BUTTON = (By.ID,"guide-button")
    WATCH_LATER_LIST = (By.CSS_SELECTOR,"a#endpoint.yt-simple-endpoint.style-scope.ytd-guide-entry-renderer")
    WATCH_LATER_VIDEO_TITLE = (By.ID,"video-title")

    # --- My Account Page Locators ---
    MY_ACCOUNT_PAGE_HEADER = (By.ID, "account-name")