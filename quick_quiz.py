# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 03:40:28 2019

@author: Devlin
"""

import time as t
import random as rn

print("You will have 60 seconds to answer as many quesions as you can")
print("Good Luck!")

start = t.time()
end = start + 60

signs = [' + ', ' - ', ' x ', ' / ']
choices = [x for x in range (-12, 13) if x != 0]
qs = []
correct = 0
attempts = 0

input("Start >> ")

while True:
    s = rn.choice(signs)
    a = rn.choice(choices)
    b = rn.choice(choices)
    if s == ' + ':
        c = a + b
    elif s == ' - ':
        c = a - b
    else:
        c = a * b
        
    if s == ' / ':
        q = str(c) + s + str(a) + " = "
        x = b
    else:
        q = str(a) + s + str(b) + " = "
        x = c
        
    try:
        guess = int(input("\n" + q))
    except ValueError:
        guess = "Not a Number"
    
    if guess == x:
        qs.append(q + str(x) + " "*(20-len(q + str(x))) + "CORRECT  ")
        correct += 1
        attempts += 1
    else:
        qs.append(q + str(x) + " "*(20-len(q + str(x))) + "!  You Said: " + str(guess))
        attempts += 1
        
    if t.time() >= end:
        break

print("\n" + "-"*15 + "SUMMARY" + "-"*15)
print("{} problems".format(attempts))
print("{} correct".format(correct))
print("SCORE: {}%\n".format((correct/attempts)*100))

for i in qs:
    print(i)
    
print("\n" + "-"*37)
    
    
    
    
    
    
    
    