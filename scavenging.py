import math
import time
from getters import *
from datetime import datetime as dt


def fourthLvlScav(driver, choosenTroops, sums):
    sendBtns = driver.find_elements_by_xpath("//a[@class ='btn btn-default free_send_button']")
    for troop in choosenTroops:
        val = math.ceil(choosenTroops[troop]/13)
        driver.find_element_by_xpath("//input[@name='"+troop+"']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    sendBtns[3].click()
    time.sleep(1)

    for troop in choosenTroops:
        val = math.ceil(choosenTroops[troop]/13 * 1.5)
        driver.find_element_by_xpath("//input[@name='"+troop+"']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    sendBtns[2].click()
    time.sleep(1)

    for troop in choosenTroops:
        val = math.ceil(choosenTroops[troop]/13 * 1.5 * 2)
        driver.find_element_by_xpath("//input[@name='"+troop+"']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    sendBtns[1].click()
    time.sleep(1)

    for troop in choosenTroops:
        val = math.ceil(choosenTroops[troop]/13 * 1.5 * 2 * 2.5)
        if sums[troop] + val > choosenTroops[troop]:
            val = choosenTroops[troop] - sums[troop]
        driver.find_element_by_xpath("//input[@name='"+troop+"']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    sendBtns[0].click()


def thirdLvlScav(driver, choosenTroops, sums):
    sendBtns = driver.find_elements_by_xpath("//a[@class ='btn btn-default free_send_button']")
    for troop in choosenTroops:
        val = math.ceil(choosenTroops[troop]/8)
        driver.find_element_by_xpath("//input[@name='"+troop+"']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    sendBtns[2].click()
    time.sleep(1)

    for troop in choosenTroops:
        val = math.ceil(choosenTroops[troop]/8 * 2)
        driver.find_element_by_xpath("//input[@name='"+troop+"']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    sendBtns[1].click()
    time.sleep(1)
    
    for troop in choosenTroops:
        val = choosenTroops[troop] - sums[troop]
        driver.find_element_by_xpath("//input[@name='"+troop+"']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    sendBtns[0].click()


def secondLvlScav(driver, choosenTroops, sums):
    sendBtns = driver.find_elements_by_xpath("//a[@class ='btn btn-default free_send_button']")
    for troop in choosenTroops:
        val = math.ceil(choosenTroops[troop]/3.5)
        driver.find_element_by_xpath("//input[@name='"+troop+"']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    sendBtns[1].click()
    time.sleep(1)
    
    for troop in choosenTroops:
        val = math.ceil(choosenTroops[troop]/3.5 * 2.5)
        if sums[troop] + val > choosenTroops[troop]:
            val = choosenTroops[troop] - sums[troop]
        driver.find_element_by_xpath("//input[@name='"+troop+"']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    sendBtns[0].click()

def getAvaibScavLevels(driver):
    time.sleep(1)
    levels = driver.find_elements_by_xpath("//a[@class ='btn btn-default unlock-button']")
    return 4 - len(levels)


def runScav(driver,choosenTroops, sums, level):
    sendBtns = driver.find_elements_by_xpath("//a[@class ='btn btn-default free_send_button']")
    if len(sendBtns) == level:
        if level == 4:
            fourthLvlScav(driver, choosenTroops, sums)
        elif level == 3:
            thirdLvlScav(driver, choosenTroops, sums)
        elif level == 2:
            secondLvlScav(driver, choosenTroops, sums)
    else:
        returnTimes = [dt.strptime(time.text,"%H:%M:%S").strftime("%H:%M:%S") for time in driver.find_elements_by_xpath("//span[@class = 'return-countdown']")]
        print("Can't send scavenge yet. Troops will return in " + max(returnTimes))
        
    

def scavenge(driver):

    sums = {
        "spear"     : 0,
        "sword"     : 0,
        "axe"       : 0,
        "archer"    : 0,
        "light"     : 0,
        "marcher"   : 0,
        "heavy"     : 0
        }


    avaiableTroops = getTroops(driver)
    choosenTroops = {
        "sword" : 0,
        "spear" : 0,
        "axe"   : 0
    }
    #troops that user wants to go to scavenging
    #TO DO: implement getting choosenTroops from cfg file
    #setting choosenTroop as 0 will set all avaiable troops.


    for troop in list(choosenTroops):
        if troop not in avaiableTroops:
            del choosenTroops[troop]
            continue 
        if choosenTroops[troop] == 0:
            choosenTroops[troop] = avaiableTroops[troop]
        elif choosenTroops[troop] > avaiableTroops[troop]:
            choosenTroops[troop] = avaiableTroops[troop]

    driver.find_element_by_xpath("//area[contains(@href,'screen=place')]").click()       
    driver.find_elements_by_xpath("//a[contains(@href,'&screen=place&mode=scavenge')]")[0].click()
    runScav(driver, choosenTroops, sums, getAvaibScavLevels(driver))


