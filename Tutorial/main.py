from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

def takeScreenshot(driver):
    """Takes ss of site and saves to specified folder named as number."""
    ss_num = 0
    ssPATH = "E:\Programowanie\Python\selenium\Tutorial\ss\\" + str(ss_num) + ".png"
    while os.path.isfile(ssPATH):
        ss_num += 1
        ssPATH = "E:\Programowanie\Python\selenium\Tutorial\ss\\" + str(ss_num) + ".png"
    driver.save_screenshot(ssPATH)


def getMaterials(driver):
    """Gets informations about quanity of materials"""
    materials = {
    "wood" : int(driver.find_elements_by_id("wood")[0].text),
    "stone" : int(driver.find_elements_by_id("stone")[0].text),
    "iron" : int(driver.find_elements_by_id("iron")[0].text),
    "storage" : int(driver.find_elements_by_id("storage")[0].text)
    }
    return materials

def closePopup(driver):
    """Closes mission and daily bonus popups"""
    driver.find_element_by_xpath("//a[@class='popup_box_close tooltip-delayed']").click()


PATH = "E:\Programowanie\Python\selenium\chromedriver.exe"
opt = Options()
opt.add_argument("user-data-dir=E:\\Programowanie\\Python\\selenium\\Tutorial\\tmp_cache")
driver = webdriver.Chrome(executable_path = PATH, options=opt)
driver.get("https://www.plemiona.pl/page/play/pl167")

try: 
    driver.find_elements_by_id("manager_icon_farm")[0].click()
except:
    takeScreenshot(driver)
    closePopup(driver)
    takeScreenshot(driver)
    try:
        driver.find_elements_by_id("manager_icon_farm")[0].click()
    except:
        takeScreenshot(driver)
        driver.quit()


try:
    A_btns=driver.find_elements_by_xpath("//a[contains(@onclick,'8510')]")
except:
    driver.quit()


for x in range(13):
    A_btns[x].click()
    time.sleep(0.5)
driver.quit()
