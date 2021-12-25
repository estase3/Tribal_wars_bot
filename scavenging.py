import math
import time
from getters import *
from datetime import datetime as dt


def fourth_lvl_scav(driver, choosen_troops, sums):
    send_buttons = driver.find_elements_by_xpath(
        "//a[@class ='btn btn-default free_send_button']"
    )
    for troop in choosen_troops:
        val = math.ceil(choosen_troops[troop] / 13)
        driver.find_element_by_xpath("//input[@name='" + troop + "']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    send_buttons[3].click()
    time.sleep(1)

    for troop in choosen_troops:
        val = math.ceil(choosen_troops[troop] / 13 * 1.5)
        driver.find_element_by_xpath("//input[@name='" + troop + "']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    send_buttons[2].click()
    time.sleep(1)

    for troop in choosen_troops:
        val = math.ceil(choosen_troops[troop] / 13 * 1.5 * 2)
        driver.find_element_by_xpath("//input[@name='" + troop + "']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    send_buttons[1].click()
    time.sleep(1)

    for troop in choosen_troops:
        val = math.ceil(choosen_troops[troop] / 13 * 1.5 * 2 * 2.5)
        if sums[troop] + val > choosen_troops[troop]:
            val = choosen_troops[troop] - sums[troop]
        driver.find_element_by_xpath("//input[@name='" + troop + "']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    send_buttons[0].click()


def third_lvl_scav(driver, choosen_troops, sums):
    send_buttons = driver.find_elements_by_xpath(
        "//a[@class ='btn btn-default free_send_button']"
    )
    for troop in choosen_troops:
        val = math.ceil(choosen_troops[troop] / 8)
        driver.find_element_by_xpath("//input[@name='" + troop + "']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    send_buttons[2].click()
    time.sleep(1)

    for troop in choosen_troops:
        val = math.ceil(choosen_troops[troop] / 8 * 2)
        driver.find_element_by_xpath("//input[@name='" + troop + "']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    send_buttons[1].click()
    time.sleep(1)

    for troop in choosen_troops:
        val = choosen_troops[troop] - sums[troop]
        driver.find_element_by_xpath("//input[@name='" + troop + "']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    send_buttons[0].click()


def second_lvl_scav(driver, choosen_troops, sums):
    send_buttons = driver.find_elements_by_xpath(
        "//a[@class ='btn btn-default free_send_button']"
    )
    for troop in choosen_troops:
        val = math.ceil(choosen_troops[troop] / 3.5)
        driver.find_element_by_xpath("//input[@name='" + troop + "']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    send_buttons[1].click()
    time.sleep(1)

    for troop in choosen_troops:
        val = math.ceil(choosen_troops[troop] / 3.5 * 2.5)
        if sums[troop] + val > choosen_troops[troop]:
            val = choosen_troops[troop] - sums[troop]
        driver.find_element_by_xpath("//input[@name='" + troop + "']").send_keys(val)
        sums[troop] += val
        time.sleep(0.2)
    send_buttons[0].click()


def get_scavenge_levels(driver):
    """Gets how many scavange levels are unlocked"""
    time.sleep(1)
    levels = driver.find_elements_by_xpath(
        "//a[@class ='btn btn-default unlock-button']"
    )
    return 4 - len(levels)


def start_scavenging(driver, choosen_troops, sums, level):
    send_buttons = driver.find_elements_by_xpath(
        "//a[@class ='btn btn-default free_send_button']"
    )
    if len(send_buttons) == level:
        if level == 4:
            fourth_lvl_scav(driver, choosen_troops, sums)
        elif level == 3:
            third_lvl_scav(driver, choosen_troops, sums)
        elif level == 2:
            second_lvl_scav(driver, choosen_troops, sums)
    else:
        return_times = [
            dt.strptime(time.text, "%H:%M:%S").strftime("%H:%M:%S")
            for time in driver.find_elements_by_xpath(
                "//span[@class = 'return-countdown']"
            )
        ]
        print("Can't send scavenge yet. Troops will return in " + max(return_times))


def scavenge(driver):
    sums = {
        "spear": 0,
        "sword": 0,
        "axe": 0,
        "archer": 0,
        "light": 0,
        "marcher": 0,
        "heavy": 0,
    }
    avaiable_troops = get_troops(driver)
    staying_troops = {"sword": 50, "spear": 50}
    # Troops that will stay in village

    choosen_troops = {"sword": 0, "spear": 0, "axe": 0}
    # Troops that user wants to go to scavenging, setting choosen_troops as 0 will set all avaiable troops.

    for troop in list(choosen_troops):
        if troop not in avaiable_troops:
            del choosen_troops[troop]
            continue
        if choosen_troops[troop] == 0:
            choosen_troops[troop] = avaiable_troops[troop]
        elif choosen_troops[troop] > avaiable_troops[troop]:
            choosen_troops[troop] = avaiable_troops[troop]

    for troop in staying_troops:
        if troop not in choosen_troops:
            continue
        else:
            choosen_troops[troop] -= staying_troops[troop]
            if choosen_troops[troop] < 0:
                choosen_troops[troop] = 0
    driver.find_element_by_xpath("//a[@class = 'nowrap tooltip-delayed']").click()
    driver.find_element_by_xpath("//area[contains(@href,'screen=place')]").click()
    driver.find_elements_by_xpath("//a[contains(@href,'&screen=place&mode=scavenge')]")[
        0
    ].click()
    start_scavenging(driver, choosen_troops, sums, get_scavenge_levels(driver))
    driver.quit()
