'''
problen staement link: https://www.hackerrank.com/challenges/find-angle/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan,degrees

abl = int(input())
bcl = int(input())

x = atan(abl/bcl)
print(str(round(degrees(x)))+'\u00B0')
