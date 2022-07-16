
from utils.selecting_elements import select_by_class_name, select_by_css,select_by_xpath, select_by_text
from utils.driver import driver
from utils.credentials import get_username

def get_followers():
    try:
        driver.get("https://www.instagram.com/{}/".format(get_username()))
        pass
    except Exception as e:
        print("error "+ str(e))
    