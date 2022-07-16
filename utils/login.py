
from utils.driver import driver
from utils.selecting_elements import select_by_css ,select_by_xpath,select_by_text



def login(user , password):
    driver.get('https://www.instagram.com/accounts/login/')
    
    usernameInput = select_by_css("input[name='username']")
    usernameInput.clear()
    usernameInput.send_keys(user)
    print("Entering username")
    passwordInput = select_by_css("input[name='password']")
    passwordInput.clear()
    passwordInput.send_keys(password)
    print("Entering password")
    select_by_css("button[type='submit']").click()
   
    try:
        element = select_by_text("Please")
    except:
        print("Login Successsful\n")
        return True

    print("login failed")
    return False
    
    
def login_again():
    #todo : implemnt later as required
    exit()