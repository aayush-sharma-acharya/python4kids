"""
Q. Generate half pyramid number pattern
N = 5, Pattern:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
N = 5


for i in range(N):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
