# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 07:13:16 2018

@author: Devlin
"""

def solve_for_x(var, m, b, y):
    
    try:
        givens = [int(i) for i in [m, b, y]]
    except ValueError:
        print("You did not input M, B, or Y as numbers. Do it again")
    
    if var == "1":
        x = (givens[2] - givens[1])/givens[0]
    elif var == "2":
        x = ((givens[2] - givens[1])/givens[0]) ** .5
    else:
        print("Simple to solve Y = Mx + B when you have Y, M, and B")
        print("Complex to solve Y = Mx^2 + B when you have Y, M, and B")
        print("What you have was gibberish")
        
        
    print("x = " + str(int(x)))

if __name__ == "__main__":
    print("lets solve some Algebra")
    print("Your equation needs to be either...")
    print("1) Y = Mx + B")
    print("2) Y = Mx^2 + B")
    variant = input("The number of your equation >> ")
    slope = input("x Coefficient >> ")
    intercept = input("Constant >> ")
    equals = input("Y >> ")
    solve_for_x(variant, slope, intercept, equals)
