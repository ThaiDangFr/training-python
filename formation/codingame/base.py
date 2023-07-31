# convert a decimal n to base
def decimal_to_base(n, base):
    res = []
    q = n
    while q > 0:
        pq = q
        q = q // base
        r = pq - q*base
        res.insert(0,str(r))
    return int("".join(res))


# convert a n in base to decimal
def other_to_decimal(n, base):
    st = str(n)
    sum = 0
    index = len(st)-1
    for i in st:
        sum += int(i)*base**index
        index -= 1
    return sum


print(decimal_to_base(29,8))
print(other_to_decimal(35,8))


# convertir base 4 en ascii
s = "120112021203"
for i in range(0, len(s), 4):
    w = s[i:i+4]
    deci = int(w, 4)
    ascii = chr(deci)
    print(ascii, end="")

