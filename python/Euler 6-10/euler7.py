'''
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10001st prime number? 
'''
'''
r = range(1, 10001)
prime_set = []
def prime_list(x):
    
    counter = 5
    for i in r:
   
        
#The % != 0 if statement
        if i % 6 == 0:
            j = i + 1
            k = i + 5
            
            if j % 3 and j % 5 and j % 7 != 0: 
                if k % 3 and k % 5 and k % 7 != 0:
#Return the next prime number and then input prime into % != 0 if statement            
                    counter += 2
                    prime_set.append([j, k, True])

prime_list(r)
print(prime_set)
'''
'''
r = list(range(1, 10001))
print(type(r))
counter = 1
while counter < 10001:
    if ([counter % i for i in r]):
        counter += 1
        print(counter, counto)
    
'''
'''
def counter():
    counter = 0
    count_index = []
    while counter < 101:
        counter += 1
        count_index.append(counter)
    print(count_index)

counter()
'''
'''
r = range(1, 10001)
def prime_list(x):
    d = 0
    
    for i in x:
        if i != 1 or i == 2:
            d += 1
            if d < 3:
                print(i,"is a", True,"prime,","It is the", d,"prime")
            if i % 2 or i % 3 or i % 5 or i % 7 != 0:     
                if d < 102:
                    print(i,"is a", True,"prime,","It is the", d - 1,"prime")

prime_list(r)
'''
'''
z = range(1,103)
sumz = []

for i in z:
    div = 2
    if i != 1:
        if i % div !=0:
            sumz.append(i)
            div += 1
            if i % div !=0:
                sumz.append(i)
print(sumz)

for x in range(1, 1000):
	if x % int(str(z)) != 0:
		sum.append(x)
print(sum)
'''
'''
x = range(1, 25)

y = []
def value(i % 2 for i in x):
    if i != 1:
        y.append(i)

z = 0

sequence = [x,y,z]

print(sequence)
'''
'''
test_list = [i for i in range(1, 26)]
test_list2 = [i for i in range(1, 26)]


test2 = [i % j for i, j in zip(test_list, test_list2)]
print(test2)
'''
#Create list of primes
prime_list = [2, 3]
#Function determines each new prime in list
def com_prime_list():    
    #new_val acts as primer for new primes
    new_val = 5
    #Determines how long prime_list will be
    while len(prime_list) < 10001:
        #Take the new_val and divide it by
        #every integer, creating a new list
        #with the remainder of each division
        x_prime = [new_val % i for i in prime_list]
        #If the number of remainders that equal 0,
        #is 0(no factors), it is prime
        if x_prime.count(0) == 0:
            #Add this value to prime_list
            prime_list.append(new_val)
        #Increase new_val for next evaluation
        new_val += 2
            #Similar to above except if the remainder
            #is 0, it is not prime and does not append
        #elif x_prime.count(0) != 0:
            #Increase new_val for next evaluation
            #new_val += 2
#Run the function                
com_prime_list()
#Print the required solution
print('The 10,001st prime number is:',prime_list[10000])