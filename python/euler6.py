'''
The sum of the squares of the first ten natural numbers is, 385
The square of the sum of the first ten natural numbers is, 3025
Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
'''
def sum_sqr(x):
    return sum(i**2 for i in x)

def sqr_sum(y):
    return sum(y)**2

print(sqr_sum(range(101))-sum_sqr(range(101)))
