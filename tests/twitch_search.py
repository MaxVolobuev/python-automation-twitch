import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.twitch_helpers import *
from config.config_loader import ENV_CONFIG

def test_twitch_mobile_flow():
    mobile_emulation = {"deviceName": "Pixel 2"}
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(390, 844)

    driver.get(ENV_CONFIG["BASE_URL"])

    accept_cookie_popup(driver)
    search_term(driver, "StarCraft II")
    click_view_all_results(driver)
    scroll_page(driver, times=2)
    click_first_stream(driver)
    dismiss_stream_popup(driver)
    take_screenshot(driver, "screenshots/streamer_page")

    driver.quit()
