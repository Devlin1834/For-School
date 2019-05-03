# -*- coding: utf-8 -*-
"""
Created on Sat Feb 46 09:08:47 2049

@author: Devlin
"""

import random as rn

questions = []

for i in range(3):
    a = rn.randint(4, 12)
    b = rn.randint(-12, -4)
    questions.append(str(a) + " + " + str(b) + " = ")
    
for i in range(2):
    a = rn.randint(-12, -4)
    b = rn.randint(-12, -4)
    questions.append(str(a) + " + " + str(b) + " = ")
    
for i in range(3):
    a = rn.randint(4, 12)
    b = rn.randint(-12, -4)
    questions.append(str(a) + " - " + str(b) + " = ")
    
for i in range(2):
    a = rn.randint(-12, -4)
    b = rn.randint(-12, -4)
    questions.append(str(a) + " - " + str(b) + " = ")
    
for i in range(2):
    a = rn.randint(4, 12)
    b = rn.randint(-12, -4)
    questions.append(str(a) + " x " + str(b) + " = ")
    
for i in range(2):
    a = rn.randint(-12, -4)
    b = rn.randint(-12, -4)
    questions.append(str(a) + " x " + str(b) + " = ")
    
for i in range(2):
    a = rn.randint(4, 12)
    b = rn.randint(-12, -4)
    x = a * b
    questions.append(str(x) + " / " + str(b) + " = ")
    
for i in range(2):
    a = rn.randint(-12, -4)
    b = rn.randint(-12, -4)
    x = a * b
    questions.append(str(x) + " / " + str(b) + " = ")
    
for i in range(1):
    a = rn.randint(-100, 100)
    b = rn.randint(-100, -4)
    questions.append(str(a) + " + " + str(b) + " = ")
    
for i in range(1):
    a = rn.randint(-100, 100)
    b = rn.randint(-100, -4)
    questions.append(str(a) + " - " + str(b) + " = ")

for i in range(20):
    q = rn.choice(questions)
    questions.remove(q)
    print(str(i+1) + ": " + q)