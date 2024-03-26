file = open("contents.txt","r")
file2 = open("create.txt","w")
file3 = open("append.txt","a")

if file:
    print("Success of Opening file")
    data = file.read(16) # -1 == () will read the whole contents
    print(data)
    data2 = file2.write("Hello This is Me Lal Hrin Thang") 
    # the previous content was Hello This is Me
    

    print(f"This is with write method {data2}")

    # data3 = file3.write(" : This is appended message")
    # print(f"This is with append method {data3}")
    file.close()
else:
    print("There is no file")