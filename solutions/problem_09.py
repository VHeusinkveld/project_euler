import time
'''
Euler project problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
start = time.time()
found = False
for a in range(1,1001):
	
	for b in range(a,1001):
		
		formula = 2 * a * b - 1000 * (2*a + 2*b - 1000)
		
		if formula == 0: 
			c = 1000 - a - b
			print 'a=',a, 'b=',b, 'c=',c
			print 'abc =', (a*b*c)
			found = True
			break
	if found:
		break	
end = time.time()
duration = end-start
print 'duration =', duration