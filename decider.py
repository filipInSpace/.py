
#Author: Filip Navrkal 

import random

def decide():
    options = input("Enter your options, separated by commas: ").split(",")
    print("Your options are: ", options)
    choice = random.choice(options)
    print("I have randomly chosen for you: ", choice)

decide()
