def check(lst):
    # check horizontally
    for l in lst:
        s = "".join(sorted(l))
        if s != "123456789":
            return False
    print("hori ok")

        
    # check vertically
    for x in range(9):
        col = []
        for y in range(9):
            col.append(lst[y][x])
        col.sort()
        scol = "".join(col)
        if scol != "123456789":
            return False
    print("verti ok")

        
    # check boxes
    for verti_box in range(3):
        for hori_box in range(3):
            box = ""
            for y in range(3):
                box += lst[y+verti_box*3][0+hori_box*3:3+hori_box*3]

            s = "".join(sorted(box))
            if s != "123456789":
                return False
    print("box ok")
            
    return True


"""
inputs = [
    "195743862",
    "431865927",
    "876192543",
    "387459216",
    "612387495",
    "549216738",
    "763524189",
    "928671354",
    "254938671"
    ]
"""
inputs = []
for i in range(9):
    st = input("Line: ")
    if len(st) != 9 or not st.isdigit():
        print("Invalid input")
        break
    inputs.append(st)


if check(inputs):
    print("Yes")
else:
    print("No")
