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
    src.close()
    
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

            #remplir dic avec (first, last) : point
            if not (first, last) in dic:
                dic[(first, last)] = float(point)
            else:
                dic[(first, last)] += float(point)

    # print result
    sorted_key = sorted(dic, key=lambda x: x[0])
    for e in sorted_key:
        print(e[0], e[1], dic[e])
                
                
    
except (FileEmpty, BadLine) as e :
    print(e)
    exit()

except Exception as e:
    if e.errno == errno.ENOENT:
        print("file not found")
        exit(e.errno)
    else:
        print(strerror(e.errno))


    

    
