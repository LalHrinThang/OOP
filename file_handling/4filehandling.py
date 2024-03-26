import os
with open("contents.txt","a+") as file:
    if file:
        print("Current Position : ",file.tell())

        file.seek(12,os.SEEK_SET)

        print("Update Position with seek_set method: ",file.tell())

        file.seek(0,os.SEEK_END)

        print("Update Position with seek_end method: ",file.tell())

        file.seek(file.tell()-7,os.SEEK_SET)

        print("Update Position : ",file.tell())

        file.seek((os.SEEK_END)+5,os.SEEK_SET)

        print("Update Position : ",file.tell())

        file.seek((os.SEEK_END)+7,os.SEEK_SET)

        print("Update Position : ",file.tell())