# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:07:09 2026

@author: Fatemeh
"""

ramz= input("enter password:")
number=0
for i in ramz:
    if i.isdigit():
        number+=1
upper=0
for i in ramz:
    upper+=1
lower=0
for i in ramz:
    lower+=1
alpha=0
for i in ramz:
    alpha+=1
    if len(ramz)>8:
     print("موفقیت امیز")
else:
    print("اشتباه است")