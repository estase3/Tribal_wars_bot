def get_materials(driver):
    """Gets informations about quanity of materials"""
    materials = {
        "wood": int(driver.find_elements_by_id("wood")[0].text),
        "stone": int(driver.find_elements_by_id("stone")[0].text),
        "iron": int(driver.find_elements_by_id("iron")[0].text),
        "storage": int(driver.find_elements_by_id("storage")[0].text),
    }
    return materials


def get_troops(driver):
    """Gets informations about quanity of troops"""
    driver.find_element_by_xpath("//a[@class='nowrap tooltip-delayed']")
    troops = {}
    elem = driver.find_elements_by_class_name("all_unit")
    for troop in elem:
        troops[
            troop.find_element_by_class_name("unit_link").get_attribute("data-unit")
        ] = int(troop.text.split()[0])
    return troops
