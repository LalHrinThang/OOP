file = open("contents.txt","r")
file2 = open("create.txt","w") # write
file3 = open("append.txt","a")
file4 = open("append.txt","r")
if file:
    print("Success of Opening file")
    print("This is with readline")
    data = file.readline()
    
    print(data)
    print("This is reading with readlines => return as a list")
    data = file4.readlines()
    print(data)

    file.close()



else:
    print("There is no file")