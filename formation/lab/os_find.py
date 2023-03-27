import os

def find(path, dir):
    os.chdir(path)
    dirs = os.listdir()
    for d in dirs:
        if os.path.isdir(path+"/"+d) and os.access(path+"/"+d, os.R_OK):
            if dir == d:
                print(path + "/" + d)
            find(path + "/" + d, dir)

find("/tmp", "UserData")
        

