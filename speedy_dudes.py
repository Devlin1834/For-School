# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 12:20:28 2018

@author: Devlin
"""

import random as rn

###############################################################################
###############################################################################
def speedy_dudes(form, diff, aao = False):
    
    if aao == True:
        count = 50
    else:
        count = 1

# Only here in case I decide to import the function but I'm never gonna do that probably  
    try:
        diff = int(diff)
        if diff not in [1, 3, 5]:
            print("It wasn't 1, 3, or 5 so I set it to 1 for you")
            diff = 1
    except ValueError:
        print("Difficulty set to 1 due to user idiocy")
        diff = 1
        
###############################################################################
# Form one generates Multiplication, Division, and Exponent questions. The number
# and dificulty of these questions is determined by the difficuty.
###############################################################################   
    if str(form).lower() == "one":        
        challenge = {#diff: [lower range, multiplication q's, division q's, exponent q's]
                     1: [2, 2, 2, 0],
                     3: [4, 1, 3, 0],
                     5: [7, 0, 3, 1]}        
        mtable_range = list(range(challenge[diff][0],13))
        for i in range(count):
            if aao == True:
                print("\n#" + str(i + 1))
            for i in range(challenge[diff][1]):
                print(str(rn.choice(mtable_range)) + " x " + str(rn.choice(mtable_range)))       
            for i in range(challenge[diff][2]):
                quotient = rn.choice(range(challenge[diff][0],13))
                divisor = rn.choice(range(challenge[diff][0],13))
                dividend = quotient * divisor
                print(str(dividend) + " / " + str(divisor))
            for i in range(challenge[diff][3]):
                x = rn.choice(range(2, 13))
                print(str(x) + "^2")
                
###############################################################################
# Form Two generates Fraction Simlication questions at levels 1 and 3, and Percent
# decimal fraction converstion questions at level 5. 
###############################################################################
    elif str(form).lower() == "two": 
        challenge = {#diff: [fracs, greater than 1]  # This dictionary is less
                     1: [1, 0],                      # elegant than the others
                     3: [1, 1],                      # but still provides a good 
                     5: [0, 0]}                      # visual of whats happening
        for i in range(count):
                if aao == True:
                    print("\n#" + str(i + 1))
        
                if challenge[diff][0] == 1:    
                    for i in range(3):
                        hcf = rn.choice(range(2, 13))
                        numerator = rn.choice(range(1, 11))
                        if challenge[diff][1] == 0:
                            denominator = rn.choice(range(numerator + 1, 13))
                        else:
                            denominator = rn.choice(range(1, 13))
                        fraction = str(numerator * hcf) + "/" + str(denominator * hcf)
                        print(fraction)
                else:
                    percent = rn.choice(range(1, 101))  
                    decimal = rn.choice(range(1, 100)) / 100
                    denominator = rn.choices([2, 4, 5, 10, 20, 25, 50], weights = [0.017, 0.034, 0.043, 0.086, 0.172, 0.216, 0.431])[0]
                    numerator = rn.choice(range(1, denominator))
                    fraction = str(numerator) + "/" + str(denominator)
                    print(str(percent) + "%")  
                    print(decimal)
                    print(fraction)  
                    
###############################################################################
# Form three generates Algebra questions that become more challenging as difficulty                
# increases.
###############################################################################    
    elif str(form).lower() == "three":
        challenge = {#diff: [lower range, upper range]
                     1: [-12, 13],
                     3: [-5, 6],
                     5: [-12, 13]}
        for i in range(count):
            if aao == True:
                print("\n#" + str(i + 1))
            
            x = rn.choice([x for x in range(challenge[diff][0], challenge[diff][1]) if x != 0])
            m = rn.choice([x for x in range(challenge[diff][0], challenge[diff][1]) if x != 0])
            b = rn.choice([x for x in range(challenge[diff][0], challenge[diff][1]) if x != 0])
            y = (m * x) + b
            z = (m * (x ** 2)) + b
            
            if m == 1:
                m = ""
            elif m == -1:
                m = "-"
            
            if diff == 1:                                       
                if b >= 0:
                    print(str(y) + " = " + str(m) + "x + " + str(b))
                else:
                    print(str(y) + " = " + str(m) + "x - " + str(b * -1))
                    
            else:                               
                if b < 0:
                    print(str(z) + " = " + str(m) + "x^2 - " + str(b * -1))
                else:
                    print(str(z) + " = " + str(m) + "x^2 + " + str(b))          
                    
###############################################################################
# Neg generates negative number questions, to be used in terms 2 and 3 in both
# forms
###############################################################################  
    elif str(form).lower() == "neg":
        x = [i for i in range(-12, 13) if i != 0]
        signs = [" + ", " - ", " x "]
        for sign in signs:
            print(str(rn.choice(x)) + sign + str(rn.choice(x)) + " = ")
        a = rn.choice(x)
        b = a * rn.choice(x)
        print(str(b) + " / " + str(a) + " = ")
        
###############################################################################
# This is what happens when you don't properly input arguments. 
#
###############################################################################                    
    else:
        print(str(form) + " is not a valid form")
        print("Form must be specified as one, two, or three")
        print("One generates Multiplication and Divison questions")
        print("Two generates fraction simplification questions")
        print("Three generates simple Alegbra questions")
###############################################################################
###############################################################################

if __name__== "__main__":       
    kind = input("One, Two, or Three? >> ")
    while True:
        diff = input("Dificulty can be 1, 3, or 5 >> ")
        try:
            diff = int(diff)
            if diff in [1, 3, 5]:
                break
            else:
                print("1, 3, or 5 only")
        except ValueError:
            print("Difficulty needs to be a number. This really isn't confusing")
    many = input("All at once, Y or N? >> ")
    if str(many).lower() == "y":
        speedy_dudes(kind, diff, aao = True)
    elif str(many).lower() == "n":
        speedy_dudes(kind, diff)
    else:
        print("Its a Y or N question, try again next time")