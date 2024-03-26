file = open("contents.txt","r")
file2 = open("create.txt","w") # write
file3 = open("append.txt","a")
file4 = open("append.txt","r")


with open("contents.txt","a") as file:

    if file:
        print("The file pointer at bytes : ",file.tell())

    # r => pointer location at 0
    # a => pointer location at 27
    # w => pointer location at 0 (Delete all)
    
    else:
        print("Something wrong")