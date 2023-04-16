s = "8 5 -5 5 3"

lst = list(map(int, s.split()))

s = 0

for i in lst:
    prime = True

    if i > 0:
        for j in range(2,i):
            if i % j == 0:
                prime = False
                break
    else:
        prime = False
        
    if prime:
        s += i

print("true" if s == lst[0] else "false")
