'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product 
of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from 
the product of two 3-digit numbers.
'''
def pal(n):
    if str(n) == str(n)[::-1]:
        return True
var = []
for x in range (999, 900, -1):
    for y in range (999, 900, -1):
        if pal(x * y):
            var.append(x * y)
print(max(var))            