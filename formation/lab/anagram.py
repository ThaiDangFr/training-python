def clean(st):
    newst = st.lower()
    newst = newst.strip()
    newst = "".join(newst.split()) # remove spaces
    l = list(newst)
    l.sort()
    return "".join(l)
    
    

def anagram(t1, t2):
    newt1 = clean(t1)
    newt2 = clean(t2)
    
    return newt1 == newt2

t1 = input("text 1: ")
t2 = input("text 2: ")

if anagram(t1,t2):
    print("Anagrams")
else:
    print("Not anagrams")
