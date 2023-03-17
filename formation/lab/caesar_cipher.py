def caesar(st, offset):
    res = []
    lowerst = st.lower()
    count = 0
    for s in lowerst:
        if s.isalpha():
            x = ord(s) - ord("a")
            newx = (x + offset) % 26
            ch = chr(newx+ord("a"))
            if st[count].isupper():
                ch = ch.upper()
            res.append(ch)
        else:
            res.append(st[count])
            
        count += 1
    return "".join(res)

        
st = input("You message: ")
offset = int(input("Offset: "))

if offset not in range(1,26):
    print("Incorect offset")
    exit()


print(caesar(st, offset))
