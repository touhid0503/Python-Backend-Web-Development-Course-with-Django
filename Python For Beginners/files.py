a = open("text.txt", "r") #read
print(a.readable())
# print(a.readline())
# print(a.readline())
# print(a.readlines()[2])
for x in a.readlines():
    print(x)
a.close()
