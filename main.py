file=open('bangladesh.txt','r')
print(file.read())
file.close()

file=open('bangladesh.txt','r')
print("\n Read in parts \n")
print(file.read(3))
file.close()


file=open('bangladesh.txt','a')
file.write("I am from Bangladesh and I am a student of Codingal!!")
file.close()
