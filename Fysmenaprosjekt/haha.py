# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 17:48:20 2018

@author: Erlendo
"""
import matplotlib.pyplot as plt
import numpy as np
import sys

f = open('encut_uten_k4ox.txt', 'r')
p = []
force = []
e = []
x = np.linspace(200, 1000, 17)

print x
for i in range(0, len(x)):
    f1 = f.readline()
    a = f1.split(" ")
    print a
    try: 
        force.append(float(a[0]))
        p.append(float(a[2]))
        e.append(float(a[4]))
        
        
    except ValueError:
        
        print "hola"

f.close()

f = open('encut_uten_k4.txt', 'r')

for i in range(0, len(x)):
    f1 = f.readline()
    a = f1.split(" ")
    print a
    try: 
        force[i] -= float(a[0])
        p[i] -= float(a[2])
        e[i] -= (float(a[4]))
        
        
    except ValueError:
        
        print "hola" 

plt.subplot(2,2,1)
plt.plot(x, force, '.-')
plt.ylabel('Force')

plt.subplot(2,2,2)
plt.plot(x, p, '.-')
plt.ylabel('Pressure')

plt.subplot(2,2,3)
plt.plot(x, e, '.-')
plt.ylabel('Total energy')

plt.subplot(2,2,4)
plt.plot(x, force, '.-')
plt.ylabel('Band gap')

plt.tight_layout
plt.show()

    
    
    
    
