import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Setup drivers
os.environ["PATH"] += r"E:\Development\Selenium Drivers"

# Warning and Window options
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized")

# Start Driver
driver = webdriver.Chrome(options=chrome_options)

# Open Website
driver.get("https://www.croxyproxy.com/")

# Open Torrent Site
url_input = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (
            By.ID,
            "url",
        )
    )
)
url_input.send_keys("https://www.1377x.to/")

submit_btn = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (
            By.ID,
            "requestSubmit",
        )
    )
)
submit_btn.click()

# Goto to TV show page
show_lib_url = r"/series-library/a/1/"
show_lib = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            f'//a[@class="library" and @__cporiginalvalueofhref="{show_lib_url}"]',
        )
    )
)
show_lib.click()


# Open Shows and Scrape Data
show_name_regex = r"^\/series\/(.+)\/"
open_show = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            f'//a[@__cporiginalvalueofhref="{show_name_regex}"]',
        )
    )
)
open_show.click()

# Open Season
open_season = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//img[@alt="Missing Season Image"]',
        )
    )
)
open_season.click()


# Write data in CSV
def write_data(name, filenames):
    pass


# time.sleep(10)

# Close the driver
driver.quit()
