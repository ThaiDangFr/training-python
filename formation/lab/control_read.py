def read_int(prompt, min, max):
    while True:
        st = input(prompt)
        
        try:
            i = int(st)
        except ValueError:
            print("Error: wrong input")
            continue

        if i < min or i > max:
            print("Error: the value is not within permitted range (",min,"..",max,")")
        else:
            return st

v = read_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)
