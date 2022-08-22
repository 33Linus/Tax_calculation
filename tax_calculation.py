# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 12:04:05 2022

@author: Linus
"""

sal = float(input('enter your salary : '))

slab1 = 50000
slab2 = 100000
slab3 = 200000

tax1 = 0
tax2 = .05
tax3 = .08
tax4 = .10
tax_s = [0,.05,.08,.10]

salary = []

if sal <= slab1:
    salary.append(sal)
    tax_slab1 = salary[0]*tax1
    print('salary',salary)
    print(tax_slab1)
    total_tax = tax_slab1
    
elif sal-slab1 <= slab2:
    salary.append(slab1)
    salary.append(sal-slab1)
    tax_slab1 = salary[0]*tax1
    tax_slab2 = salary[1]*tax2
    print('salary',salary)
    print(tax_slab1,tax_slab2)
    total_tax = tax_slab1+tax_slab2

elif sal-slab2 <= slab3:
    salary.append(slab1)
    salary.append(slab2)
    salary.append(sal-(slab1+slab2))
    tax_slab1 = salary[0]*tax1
    tax_slab2 = salary[1]*tax2
    tax_slab3 = salary[2]*tax3
    print('salary',salary)
    print(tax_slab1,tax_slab2,tax_slab3)
    total_tax = tax_slab1+tax_slab2+tax_slab3

else :
    salary.append(slab1)
    salary.append(slab2)
    salary.append(slab3)
    salary.append(sal-(slab1+slab2+slab3))
    tax_slab1 = salary[0]*tax1
    tax_slab2 = salary[1]*tax2
    tax_slab3 = salary[2]*tax3
    tax_slab4 = salary[3]*tax4
    print('salary',salary)
    print(tax_slab1,tax_slab2,tax_slab3,tax_slab4)
    total_tax = tax_slab1+tax_slab2+tax_slab3+tax_slab4
    
print('Your total tax is',total_tax)