"""
Q13. Generate Following Word Patterns:
N = 5 and s = "Aayush"
Aayush  Aayush Aayush Aayush Aayush
Aayush  Aayush Aayush Aayush
Aayush  Aayush Aayush
Aayush  Aayush
Aayush
"""
word = "Aayush"
N = 5
for j in range(N, 0, -1): # Column
    for i in range(j, 0, -1): # Row   
        print(word, end=" ")
    print("\n")