# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 07:08:04 2018

@author: Devlin
"""

def factors(number):
    
    factors = [i for i in range(1, number + 1) if number % i == 0]

    if factors == [1, number]:
        return "Its Prime!"
    else:
        return factors
    
if __name__ == "__main__":
    while True:
        print("\nList of factors")
        print("Type 0 to stop")
        while True:
            number = input("Any number >> ")
            try:
                number = int(number)
                break
            except ValueError:
                print("It has to be a number, Jackass")
        if number == 0:
            break
        else:
            print(factors(number))
