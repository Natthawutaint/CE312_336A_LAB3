#EX2
array = ["A","B","C","D","E","F"]
print("Address Stack")
for i in range(len(array)):
    print("|   "f"{i}","  |",f"{array[i]}","|")
array.pop(0)
print("Address Stack")
for i in range(len(array)):
    print("|   "f"{i}","  |",f"{array[i]}","|")