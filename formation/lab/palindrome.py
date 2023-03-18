def palindrome(st):
    clean_st = st.strip()

    if clean_st == "":
        return False
    
    clean_st = clean_st.lower()
    clean_st = clean_st.split()
    ccs = "".join(clean_st)
    rev_ccs = "".join(list(reversed(ccs)))
    
    return ccs == rev_ccs




st = input("message: ")
if palindrome(st):
    print("It's a palindrome")
else:
    print("It's not a palindrome")
    
    
    

    
