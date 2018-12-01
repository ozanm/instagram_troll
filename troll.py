# FORMAT CREATING USER:
# - email: FAKE_EMAIL
# - password: RANDOM_CHARACTERS
# - username: RANDOM_CHARACTERS
# - first_name: RANDOM NAME FROM JSON FILE

import os
import random
import json
import requests
import string
import sys
import termios
import tty
import time

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

chars = string.ascii_letters + string.digits + "!@#$%^&*()"
counting_numbers = "0123456789"
random.seed = (os.urandom(1024))

url_accounts = "https://www.instagram.com/accounts/web_create_ajax/"

names = json.loads(open("names_list.json").read())["names"]
email_extentions = json.loads(open("email_extentions_list.json").read())["emails"]

authentication = raw_input(bcolors.OKBLUE + "This program creates a fake instagram user, then sends that to the link for instagram's user database[y/n]: " + bcolors.ENDC)

print bcolors.WARNING + "When you want to stop the program, press '^C'\n" + bcolors.ENDC

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    email = name.lower() + name_extra + email_extentions[random.randint(0, len(email_extentions) - 1)]
    password = ''.join(random.choice(chars) for i in range(8))
    username = name.lower() + name_extra + str(counting_numbers[0:random.randint(0, len(counting_numbers)):1])
    first_name = name.upper()

    try:
        print bcolors.WARNING + "Injecting... email: %s password: %s username: %s first_name: %s" % (email, password, username, first_name) + bcolors.ENDC
        requests.post(url_accounts, allow_redirects=False, data={
            email: str(email),
            password: str(password),
            username: str(username),
            first_name: str(first_name),
        })
        
        if name == names[-1]:
            print bcolors.OKGREEN + "Program Finished... :)" + bcolors.ENDC
            exit(0)

    except KeyboardInterrupt:
        print bcolors.OKGREEN + "\nProgram Finished... :)" + bcolors.ENDC
        exit(0)
    except Exception as error:
        print bcolors.FAIL + str(type(error).__name__) + " Error: " + error.message + bcolors.ENDC
        break
