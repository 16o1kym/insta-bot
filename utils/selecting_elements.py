
# from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from utils.driver import driver,wait


# todo : check other function available to wait other than clickable for some cases
def select_by_css(element):
    return wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, element)))

def select_by_xpath(element):
    return wait.until(EC.element_to_be_clickable((By.XPATH, element)))

def select_by_class_name(element):
    return wait.until(EC.element_to_be_clickable(By.CLASS_NAME , element))
    
def select_by_text(element):
    return wait.until(EC.element_located_to_be_selected(By.XPATH, "//*[contains(text() , {})]".format(element)))