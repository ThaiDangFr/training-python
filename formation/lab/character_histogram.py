from os import strerror

srcname = input("filename: ")
try:
    src = open(srcname, "rt")
    
    counter = { chr(x):0 for x in range(ord('a'), ord('z')+1) }

    block_size = 1024
    while True:
        block = src.read(block_size)
        if not block: # block is empty
            break
        for e in block:
            if e.isalpha():
                counter[e.lower()] += 1

    sorted_keys = sorted(counter, key=lambda x: counter[x], reverse=True)

    dstname = srcname[:srcname.rfind(".")] + ".hist"
    dst = open(dstname, "wt")

    for k in sorted_keys:
        if counter[k]>0:
            dst.write(str(k) + " -> " + str(counter[k]) + "\n")

    src.close()
    dst.close()


except IOError as e:
    print("Cannot open file:", strerror(e.errno))
    exit(e.errno)
