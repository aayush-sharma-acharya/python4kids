n = int(input())
s = 0
for i in range(0, n-1):
    s = s+(10**i)
    res = s * (i+1)
    print(res)

    