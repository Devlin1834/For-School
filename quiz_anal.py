# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:42:19 2019

@author: Devlin
"""

import csv

data = list(csv.reader(open("quizgame.csv")))

def game_analysis(start):
    start = str(start)  
    answers = []
    while len(answers) < len(data):  
        for i in data:
            if i[0] == start:
                start = i[2]
                answers.append(start)
                
            else:
                pass
    
    return answers[9]
            
choices = list(range(1, 16))
for i in range(-15, 0):
    choices.append(i)
    
ends = [str(i) + ": " + str(game_analysis(i)) for i in choices]
    
for i in ends:
    print(i)
    