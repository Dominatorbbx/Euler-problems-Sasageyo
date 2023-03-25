# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 00:13:50 2023

@author: ydaks
"""

n1=2
n2=3
arr1=[2,3]
factors=[]
primeFlag = 1
userInput = 600851475143

for i in range(2,userInput):
    if(userInput%i==0):
        factors.append(i)
        print(factors)
arrr = [];

for j in range(0, len(factors) - 1): 
    for i in range(2,factors[j] - 1):
        if(factors[j] % i == 0):
            print("not a prime number")
            primeFlag = 0
            break
        primeFlag = 1
    if(primeFlag == 1):
        print("it is a prime number", factors[j])
    