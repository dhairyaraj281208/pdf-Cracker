import random
import pyautogui
import string
import pikepdf
from termcolor import colored

chars = "01234"

# chars = string.printable

chars_list = list(chars)

guess_password = ""

while(guess_password != 0):
    guess_password = random.choices(chars_list, k= 2)
    guess = []
    guess.append(guess_password)
    for password in guess:
        if password == "13":
            print(colored("Password Found: {}".format(password), 'green'))
            break
            with pikepdf.open("Getting started.pdf", password) as pdf:
                print(colored("Password Found: {}".format(password), 'green'))
                break
        else:
            print(colored("Trying Password: {}". format(password), 'red'))
            continue








