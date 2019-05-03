# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 04:45:36 2018

@author: Devlin
"""

import matplotlib.pyplot as plt

x = [i for i in range(1, 50001)]
y = []
for num in x:
    steps = 0
    c = num
    while c != 1:
        if c % 2 == 0:
            c = c // 2
            steps += 1
        elif c % 2 == 1:
            c = (3 * c) + 1
            steps += 1
    
    y.append(steps)

plt.figure(figsize = (10,6))
plt.hist(y)
plt.xlabel("# Of Collatz Steps")
plt.ylabel("Count")
plt.title("Distribution Of Collatz Steps")
plt.show()

plt.figure(figsize = (10,10))
plt.scatter(x, y)
plt.xlabel("Start Number")
plt.ylabel("# Of Collatz Steps")
plt.title("Collatz Steps")
plt.show()

plt.figure(figsize = (3,6))
plt.boxplot(y)
plt.xlabel("Collatz Steps")
plt.ylabel("#")
plt.title("Distribution Of Collatz Steps")
plt.show()

"""
plt.figure(figsize = (20,6))
plt.plot(x, y)
plt.xlabel("Start Number")
plt.ylabel("# Of Collatz Steps")
plt.title("Collatz Steps")
plt.show()
"""

plt.figure(figsize = (3,6))
plt.violinplot(y)
plt.xlabel("Collatz Steps")
plt.ylabel("#")
plt.title("Distribution Of Collatz Steps")
plt.show()




