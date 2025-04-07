from selenium.webdriver.common.by import By

class TwitchDirectoryPage:
    # Selectors
    COOKIE_ACCEPT_BTN = (By.XPATH, "//button[@data-a-target='consent-banner-accept']")
    SEARCH_INPUT = (By.XPATH, "//input[@data-a-target='tw-input']")
    STREAM_LINKS = (By.XPATH, "//a[contains(@href, '/videos') or contains(@href, '/live')]")
    VIEW_ALL_RESULTS = (By.XPATH, "//a[.//p[@aria-label='View All Video Search Results']]")
