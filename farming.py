from main.py import *
import time

def farm(driver):
    try: 
        driver.find_elements_by_id("manager_icon_farm")[0].click()
    except:
        closePopup(driver)
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