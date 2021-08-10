from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def getMaterials(driver):
    wood = int(driver.find_elements_by_id("wood")[0].text)
    stone = int(driver.find_elements_by_id("stone")[0].text)
    iron = int(driver.find_elements_by_id("iron")[0].text)
    storage = int(driver.find_elements_by_id("storage")[0].text)
    return wood, stone, iron, storage
    

PATH = "E:\Programowanie\Python\selenium\chromedriver.exe"

opt = Options()
opt.add_argument("user-data-dir=E:\\Programowanie\\Python\\selenium\\Tutorial\\tmp_cache")
driver = webdriver.Chrome(executable_path = PATH, options=opt)

driver.get("https://www.plemiona.pl")
try:
    world = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='world_button_active']"))
    )
    world.click()
except:
    pass

wood, stone, iron, storage = getMaterials(driver)

driver.find_elements_by_id("manager_icon_farm")[0].click()

A_btns=driver.find_elements_by_xpath("//a[contains(@onclick,'8510')]")
for x in range(13):
    A_btns[x].click()
    time.sleep(0.5)
driver.quit()