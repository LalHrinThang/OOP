file = open("contents.txt","r")
file2 = open("create.txt","w")
file3 = open("append.txt","a")

if file:
    print("Success of Opening file")
    data = file.read(16) # -1 == () will read the whole contents
    print(data)
else:
    print("There is no file")


file.close()