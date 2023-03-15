""" module.py - exemple de module """

__counter = 0

def sum1(mylist):
    global __counter
    __counter += 1
    mysum = 0
    for elem in mylist:
        mysum += elem
    return mysum

def prod1(mylist):
    global __counter
    __counter += 1
    myprod = 1
    for elem in mylist:
        myprod *= elem
    return myprod



if __name__ == "__main__":
    print("module.py executed directly")
    print("launching unit test..")
    mylist = [i+1 for i in range(5)]
    print(sum1(mylist) == 15)
    print(prod1(mylist) == 120)
else:
    print("module.py executed as a module")
