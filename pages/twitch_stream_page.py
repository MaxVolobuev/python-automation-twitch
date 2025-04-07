from selenium.webdriver.common.by import By

class TwitchStreamPage:
    VIDEO = (By.XPATH, "//video")
    POPUP_CLOSE_BTN = (By.XPATH, "//button[contains(text(), 'Not now') or contains(text(), 'Close')]")
