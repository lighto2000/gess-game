from termcolor import colored
from time import sleep
import random
def gess_user():
    number = random.randint(0,200)
    x = True
    if number %2==0:
        print(colored('its even number ','green'))
    else:
        print(colored("is not even number ",'green'))
    while x:

        gess_number = input("gess the number ?! ")
        gess = int(gess_number)
        if gess == number:
            print(colored("yah you got it ",'green'))
            sleep(2)
            x = False

        elif gess > number:
            print(colored("you up get lower ",'red'))
        elif gess < number:
            print(colored("you down get up ",'red'))
        
import random
def cumputer_gess(x):
    low = 1
    hei = x
    back = ''
    while back != 'c':
        if low != hei:
            gess = random.randint(low,hei)
        back = input(f"is {gess} low or heigh H or L ")
        if back == 'l':
            low = gess+1
        if back =='h':
            hei = gess -1
    print(f'the gess is {gess}')

cumputer_gess(60)
