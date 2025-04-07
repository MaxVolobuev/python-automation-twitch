from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

from pages.twitch_directory_page import TwitchDirectoryPage as Dir
from pages.twitch_stream_page import TwitchStreamPage as Stream
from utils.base_actions import wait_clickable, wait_visible, wait_all_visible

def accept_cookie_popup(driver):
    try:
        wait_clickable(driver, Dir.COOKIE_ACCEPT_BTN).click()
        print("✅ Cookies accepted")
    except TimeoutException:
        print("ℹ️ No cookie pop-up appeared.")

def search_term(driver, term):
    search_input = wait_visible(driver, Dir.SEARCH_INPUT)
    search_input.click()
    search_input.clear()
    search_input.send_keys(term)
    time.sleep(1)
    search_input.send_keys(Keys.RETURN)
    
def click_view_all_results(driver):
    try:
        element = wait_clickable(driver, Dir.VIEW_ALL_RESULTS, timeout=5)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5)
        try:
            element.click()
            print("Clicked 'View All'")
        except ElementClickInterceptedException:
            print("Native click blocked, using JS click")
            driver.execute_script("arguments[0].click();", element)
    except TimeoutException:
        print("ℹ'View All' not found — skipping")

def scroll_page(driver, direction='down', times=2, delay=2):
    scroll_amount = 1000 if direction == 'down' else -1000
    for _ in range(times):
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(delay)

def click_first_stream(driver):
    try:
        stream_links = wait_all_visible(driver, Dir.STREAM_LINKS)
        if not stream_links:
            raise Exception("No streamers found.")

        first_link = stream_links[0]
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_link)
        time.sleep(0.5)

        try:
            first_link.click()
            print("Clicked first stream")
        except ElementClickInterceptedException:
            print("Native click blocked, using JS click")
            driver.execute_script("arguments[0].click();", first_link)

    except TimeoutException:
        print("Could not find stream links")


def dismiss_stream_popup(driver):
    try:
        wait_clickable(driver, Stream.POPUP_CLOSE_BTN).click()
    except TimeoutException:
        print("No video pop-up found.")

def take_screenshot(driver, path_prefix="screenshots/streamer_page"):
    wait_visible(driver, Stream.VIDEO)
    time.sleep(5)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    full_path = f"{path_prefix}_{timestamp}.png"
    driver.save_screenshot(full_path)
    print(f"Screenshot saved to {full_path}")
