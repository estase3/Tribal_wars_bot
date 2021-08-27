from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from scavenging import *
import time
import os

PATH = "E:\Programowanie\Python\selenium\chromedriver.exe"
opt = Options()
opt.add_argument("user-data-dir=E:\\Programowanie\\Python\\selenium\\PlemionaBot\\tmp_cache")      #Gets cache needed to login automatically
driver = webdriver.Chrome(executable_path = PATH, options=opt)
driver.get("https://www.plemiona.pl/page/play/pl167")
#driver.get("https://www.plemiona.pl/page/play/plp7")


def takeScreenshot(driver):
    """Takes ss of site and saves to specified folder named as number."""
    ss_num = 0
    ssPATH = "E:\\Programowanie\\Python\\selenium\\PlemionaBot\\ss\\" + str(ss_num) + ".png"
    while os.path.isfile(ssPATH):
        ss_num += 1
        ssPATH = "E:\\Programowanie\\Python\\selenium\\PlemionaBot\\ss\\" + str(ss_num) + ".png"
    driver.save_screenshot(ssPATH)


def closePopup(driver):
    """Closes mission and daily bonus popups"""
    driver.find_element_by_xpath("//a[@class='popup_box_close tooltip-delayed']").click()

closePopup(driver)
scavenge(driver)