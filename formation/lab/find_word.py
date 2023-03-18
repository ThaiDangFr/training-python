word = (input("word: ")).lower()
hidden = (input("hidden word: ")).lower()

found = True
offset = 0
for s in word:
    index = hidden.find(s,offset)
    #print(index)
    if index == -1:
        found = False
        break
    offset = index + 1

if found:
    print("Yes")
else:
    print("No")
