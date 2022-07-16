from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
from utils.credentials import get_password, get_username, take_input
from utils.get_followers_following import get_followers
from utils.login import login, login_again

import warnings
warnings.filterwarnings("ignore")

print("""
      
      
      
      
         _____           _                                    ____        _   
        |_   _|         | |                                  |  _ \      | |  
          | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   | |_) | ___ | |_ 
          | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  |  _ < / _ \| __|
         _| |_| | | \__ \ || (_| | (_| | | | (_| c | | | | | | |_) | (_) | |_ 
        |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| |____/ \___/ \__|
                                   __/ |                                      
                                  |___/                                       
         ==============================================================================
         author       :KYM
         linkedin     :https://www.linkedin.com/in/16o1kym77/
         github       :https://github.com/16o1kym
         email        :16o1kym@gmail.com
         ==============================================================================





""")
  
           
def show_menu():
    print(
        '''
        1. Get all followers
        2. Get all following
        3. Get list of accounts not following back
        4. Like all photos of an account
        5. Download photos of account
        6. Exit
        
        Select 1 option >>
        '''
    )
    x = int(input())
    return x
    


take_input()
print("Logging in ...")

login_status = login(get_username() , get_password())

if not login_status:
  login_again()

while 1:
  x = show_menu()
  if(x == 6): break
  
  if(x == 1) : get_followers()
  # if(x == 2) : pass
  # if(x == 3) : pass
  # if(x == 4) : pass
  # if(x == 5) : pass
sleep(5)




