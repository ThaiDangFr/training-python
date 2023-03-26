from os import strerror
import errno

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return "Bad line: " + self.msg


class FileEmpty(StudentsDataException):
    def __str__(self):
        return "File is empty"


def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
        

    
try:
    srcname = input("filename: ")
    src = open(srcname, "rt")
    lines = src.readlines()

    dic = {}
    
    if len(lines) == 0:
        raise FileEmpty

    for line in lines:
        ls = line.split()

        # control the line
        if len(ls) != 3:
            raise BadLine(line)
        else:
            first,last,point = ls
            if not first.isalpha() or not last.isalpha() or not isfloat(point):
                raise BadLine(line)

            #TODO
            #remplir dic avec (first, last) : point


except (FileEmpty, BadLine) as e :
    print(e)
    exit()

except Exception as e:
    if e.errno == errno.ENOENT:
        print("file not found")
        exit(e.errno)
    else:
        print(strerror(e.errno))


    

    
