import os
import sys

def sum(num1, num2):
    try:
        print(num1+num2)
    except:
        print("error found")

def interactive():        
    number1 = input("enter a number: ")
    sum(number1, 12)


with open("sample.txt", mode="w+") as myfile:
    myfile.write("It involves drastically reducing carbohydrate intake and replacing it with fat. This reduction in carbs puts your body into a metabolic state called ketosis.\n\nWhen this happens, your body becomes incredibly efficient at burning fat for energy.")

print("method 1:")
myfile = open("sample.txt")
print(myfile.read())
print("--")
myfile.seek(0)
print(myfile.readlines())
myfile.close()

print("method 2:")
with open("sample.txt", mode="w+") as myfile:
    print(myfile.read())


for a,b,c in os.walk("/tmp"):
    print(a)
    print(b)
    print(c)
    print("--------")

print(os.path.splitext("/tmp/toto.zip"))    

for i in sys.argv[1:]:
    print(i)
