import string

k = 2
s = "jgnnq"

alphabet = string.ascii_lowercase
# alphabet = [chr(ord('a')+i) for i in range(26)]

o = ""
for l in s:
    i = alphabet.index(l)
    i -= k
    o += alphabet[i%26]

print(o)
