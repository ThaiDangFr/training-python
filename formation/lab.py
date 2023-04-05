import time

a = [1,2]
for i in a:
    a.insert(0,i+1)
    print(a)
    time.sleep(1)



#[1,2]    index=0 i=1
#[2,1,2]  index=1 i=1
#[2,2,1,2] index=2 i=1
