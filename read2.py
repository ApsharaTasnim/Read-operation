file=open('bangladesh.txt','r')
print("Reading first line...")
print(file.readline())
file.close()


file=open('bangladesh.txt','r')
print("Reading lines multiple times...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file=open('bangladesh.txt','r')
print("Looping through the lines...")
for line in file:
    print(line)
file.close()
