def mysplit(st):
    res = []
    word = ""
    for ch in st:
        if ch.isspace():
            if word.strip() != "":
                res.append(word)
                word = ""
        else:
            word += ch

    if word.strip() != "":
        res.append(word)
        
    return res
            


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
