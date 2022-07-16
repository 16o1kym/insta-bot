from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService



def set_driver():
    print("Would You Like To See The Automation : (Y/N)")
    x = input()   
    if(x.lower() == 'y'):
        return False
    return True


options = Options()
options.headless = set_driver()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


# driver = webdriver.Chrome(ChromeDriverManager().install() , chrome_options=options)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


wait = WebDriverWait(driver, 10)