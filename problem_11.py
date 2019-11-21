'''
project euler problem 11 
What is the greatest product of four adjacent numbers 
in the same direction (up, down, left, right, or 
diagonally) in the 20x20 grid?
'''

from numpy import *

filename = 'problem_11.txt'

with open(filename, "r") as file:
	array = []
	for line in file:
		array.append(line)
print array

newArray = []

for i in array:

    j = i.split(' ')

    k = [int(n) for n in j]

    newArray.append(k)

print newArray

problemMatrix = matrix(newArray)

print problemMatrix