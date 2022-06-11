"""
N = 7, Generate Following Half Pyramid Reversed Number Pattern.
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
6 5 4 3 2 1
7 6 5 4 3 2 1
"""
N = 5
for i in range(N):
    for j in range(i,-1,-1):
        print(j+1,end=" ")
    print()
