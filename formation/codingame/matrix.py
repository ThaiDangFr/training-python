def init_matrix(x,y):
    return [[' ' for j in range(x)] for i in range(y)]


def print_matrix(lst):
    for line in lst:
        for c in line:
            print(c,end="")
        print()

lst = init_matrix(7,4)

for y in range(4):
    lst[y][0] = "+"
    lst[y][2] = "+"
    
print_matrix(lst)
