n = int(input())
s = 0
for i in range(0, n-1):
    s = s+(10**i)
    res = s * (i+1)
    print(res)
"""
input: 5
Output :
1
22
333
4444
"""
