# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 20:47:31 2026

@author: Fatemeh
"""


a=input("salam aya mikhahid kharid konid?")
a=a.lower()
a=a.strip()
if a=="yes":
    print("yadasht mikonam")
    product=input("mahsol vard konid:")
    product.append(product)
    print(product)
elif a=="no":
    print("mamnon")
else:
    print("faqat bayad ba yes va no javab bedid")