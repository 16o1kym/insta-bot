import getpass

filename = "username.txt"
username = ""
with open(filename) as f:
    username = f.read()


password = ""

def take_input():
    global username,password
    if(username == ""):
        print("Enter username,phone number >> ")
        username = input().strip()
        with open(filename, 'w') as f:
            f.write(username)
            
    else:        
        print("Continue as "+ username + "? (Y/N)" )
        temp = input().strip()
        if( temp[0].lower() == 'n' ):
            print("Enter username,phone number >> ")
            username = input().strip()
            with open(filename, 'w') as f:
                f.write(username)
    with open(filename) as f:
        username = f.read()
    print("Enter password >> ")
    password = getpass.getpass()


def get_username():
    return username
def get_password():
    return password