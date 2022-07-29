# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# author: Valquiria Scarelli Storer

n = int(input('Digite n: '))
a = (n // 3) + 1
pitag = False
while a >= 1 and pitag == False:
    b = (n - a) // 2
    while b > a and b >= 2 and pitag == False:
        c = n - a - b
        pitag = False
        if n == (a + b + c) and (a**2 + b**2) == c**2:
          pitag = True  
        else:
            b -= 1
    if pitag == False:
        a -= 1
if pitag == True:
    print(f'{n} é pitagoreano ({a},{b},{c})')    

if pitag == False:
        print(f'{n} não é pitagoreano')