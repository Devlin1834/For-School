# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 06:14:20 2018

@author: Devlin
"""
def simplifier(nu, de):
    numerator = int(nu)
    denominator = int(de)
    
    nu_factors = [n for n in range(1, numerator + 1) if numerator % n == 0]
    de_factors = [n for n in range(1, denominator + 1) if denominator % n == 0]
    shared = [f for f in nu_factors if f in de_factors]
        
    hcf = max(shared)
    
    return str(int(numerator / hcf)) + "/" + str(int(denominator / hcf))

if __name__ == "__main__":
    print("Lets Simplify!")
    print("type STOP to stop")
    while True:
        a = input("Numerator >> ")
        b = input("Denominator >> ")
        if a.lower() == "stop" or b.lower() == "stop":
            break
        else:
            print(simplifier(a, b))
        
        