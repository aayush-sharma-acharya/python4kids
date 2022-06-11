"""
Q12.Generate Following patterns without using string and without using two prints.
N = 5, pattern:
1
22
333
4444 
"""
N = 5
total = 0
for i in range(0, N-1):
    total = total + (10**i)
    res = total * (i+1)
    print(res)
