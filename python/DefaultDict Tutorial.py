'''
Problem staement: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
'''T
from collections import defaultdict

sets = list(map(int,input().split(' ')))
seta = sets[0]
setb = sets[1]
d = defaultdict(list)
for i in range(0,seta):
    x = input()
    d[x].append(str(i+1))

for i in range(0,setb):
    y = input()
    if y not in d.keys():
        print(-1)
    else:
        print(' '.join(d[y]))
