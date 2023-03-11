# Using PYTHON 3.11.1
# WARNING! This is my 1st python project on GH,
# so don't blame me for awful coding.


# Imports
from random import randint as rint
import time, os

# Roll Function
def roll_func():
    print('Rolling...')
    time.sleep(1)
    dicenum = rint(1,6)
    print(f'Your number on dice is {dicenum}')
    rollagain = input('Roll again? (Y/N) ').lower()
    if rollagain == 'y':
        return roll_func()
    elif rollagain == 'n':
        print('Have a nice day!')
        time.sleep(1.3)
        exit()
    else:
        print('Unable to recognize answer.')
        time.sleep(0.7)
        exit()

# there goes the code
roll = input('Wanna role a dice? (Y/N) ').lower()
if roll == 'y':
    roll_func()
elif roll == 'n':
    print('Have a nice day!')
    time.sleep(1.3)
    exit()
else:
    print('Unable to recognize answer.')
    time.sleep(0.7)
    exit()