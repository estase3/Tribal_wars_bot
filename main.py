from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from scavenging import *
import time

s = Service("chromedriver.exe")
opt = Options()
opt.add_argument(
    "user-data-dir=D:\\Programowanie\\Python\\selenium\\TribalWarsBot\\tmp_cache"
)  # Gets cache needed to login automatically
driver = webdriver.Chrome(service=s, options=opt)
driver.get("https://www.plemiona.pl/page/play/pl171")
time.sleep(2)


def close_popup(driver):
    """Closes mission and daily bonus popups"""
    popup = driver.find_elements(
        By.XPATH, "//a[@class='popup_box_close tooltip-delayed']"
    )
    if len(popup) == 1:
        popup[0].click()


close_popup(driver)
scavenge(driver)
