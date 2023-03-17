"""

  # ### ### # # ### ### ### ### ### ###   3
  #   #   # # # #   #     # # # # # # #   2
  # ### ### ### ### ###   # ### ### # #   3
  # #     #   #   # # #   # # #   # # #   2
  # ### ###   # ### ###   # ### ### ###   3

                                          total = 13 bits
"""

digits = (
    ((1,1,1),(1,1),(1,0,1),(1,1),(1,1,1)), #0 
    ((0,0,1),(0,1),(0,0,1),(0,1),(0,0,1)), #1
    ((1,1,1),(0,1),(1,1,1),(1,0),(1,1,1)), #2
    ((1,1,1),(0,1),(1,1,1),(0,1),(1,1,1)), #3
    ((1,0,1),(1,1),(1,1,1),(0,1),(0,0,1)), #4
    ((1,1,1),(1,0),(1,1,1),(0,1),(1,1,1)), #5
    ((1,1,1),(1,0),(1,1,1),(1,1),(1,1,1)), #6
    ((1,1,1),(0,1),(0,0,1),(0,1),(0,0,1)), #7
    ((1,1,1),(1,1),(1,1,1),(1,1),(1,1,1)), #8
    ((1,1,1),(1,1),(1,1,1),(0,1),(1,1,1))  #9
    )

inp = input("Your number: ")
maxx = len(inp)*3+len(inp)-1
matrice = [[0 for i in range(maxx)] for j in range(5)]

#print(matrice)

offset = 0
for ch in inp:
    n = int(ch)
    digit = digits[n]
    for y in range(len(digit)):
        line = digit[y]
        if len(line) == 3:
            matrice[y][0+offset] = line[0]
            matrice[y][1+offset] = line[1]
            matrice[y][2+offset] = line[2]
        elif len(line) == 2:
            matrice[y][0+offset] = line[0]
            matrice[y][2+offset] = line[1]
    offset += 4
                
#print(matrice)

for line in matrice:
    for b in line:
        if b == 0:
            print(" ", end="")
        elif b == 1:
            print("#", end="")
    print()


        
    
    

            
        
