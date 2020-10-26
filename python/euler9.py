'''
A Pythagorean triplet is a set of three 
natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet 
for which a + b + c = 1000.

Find the product abc.
'''
import math

a = range(1, 1000)
b = range(1, 1000)
c = range(1, 1000)
ab = [i**2+j**2 for i in a for j in b]
clist = [k**2 for k in c]


if ab == clist:
    print(True)
'''
for i in ab:
    for j in clist:
        if i == j:
            print(int(math.sqrt(i)),int(math.sqrt(j)), True)
'''
for i in a:
    for j in b:
        for k in c:
            if [i**2+j**2] == [k**2]:
                if i + j + k == 1000:
                    print(i*j*k)

