s = "Happy Mother's Day To You My Mom"
mylist = s.split()
size = len(mylist)
for i in range(size, 0, -1):
    for j in range(0, i):
        print(mylist[j], end=" ")
    print("\n")  
for i in range(size, 0, -1):
    for j in range(0, i):
        print(mylist[j], end=" ")
    print("\n")  
for i in range(size):
    print("<3")

