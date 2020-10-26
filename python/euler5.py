'''
2520 is the smallest number that can be 
divided by each of the numbers from 1 to 10 
without any remainder.

What is the smallest positive number 
that is evenly divisible by all of 
the numbers from 1 to 20?
'''
z = 232792560
x = range(1, 21)
'''

'''
#Check for every value in range x is a factor of
#the variable z, if not True return the 'unfit' values 
def mod(n):
    unfit = []
    for i in x:
        if n % i != 0:
            printl = (i)
            unfit.append(printl)
    return unfit
unfit = mod(z)
print(unfit)

#Take unfit values and check
def testr():
    z = 232792560
    for i in x:
#This is so stupid, fix it
        while z % 2 != 0 or z % 3 != 0 or z % 5 != 0 or z % 7 != 0 or z % 11 != 0 or z % 13 != 0 or z % 17 != 0 or z % 19 or z % 20 or z % 18 or z % 16 or z % 12 or z % 9 or z % 8 or z % 4:
            z = z + 1
    else:
        return(z)

lab = testr()
print(lab)
print(232792560 % 2520)