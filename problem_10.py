'''
Project Euler problem 9
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

import time
start = time.time()

M = 2000000
primes = [2]

numbers = range(2,M)

for i in numbers:
	sqrti = round(i**0.5)+1
	
	if primes[-1] > int(sqrti):
		for j in primes:
			
			if i % j == 0:
				break	
			
			elif j > int(sqrti) or j == primes[-1]:
				primes.append(i)
				break
	
	else:
	
		for j in range(2,int(sqrti)):
			
			if i % j == 0:
				break	
			
			elif j == (sqrti)-1:
				primes.append(i)
				
				

sumprimes = sum(primes)	

print sumprimes	
			
end = time.time()
duration = end-start
print "duration=", duration
