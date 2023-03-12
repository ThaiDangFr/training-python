from random import randrange

"""
the computer (i.e., your program) should play the game using 'X's;
the user (e.g., you) should play the game using 'O's;
the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
all the squares are numbered row by row starting with 1
don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.

+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+

the board should be stored as a three-element list, while each element is another three-element list (the inner lists represent rows) so that all of the squares may be accessed using the following syntax:
board[row][column]

each of the inner list's elements can contain 'O', 'X', or a digit representing the square's number (such a square is considered free)
the board's appearance should be exactly the same as the one presented in the example.
implement the functions defined for you in the editor.

Drawing a random integer number can be done by utilizing a Python function called randrange()

"""

def convert_n_to_xy(n):
    x,y = 0,0
    if n in (1,2,3):
        y=0
    elif n in (4,5,6):
        y=1
    elif n in (7,8,9):
        y=2

    if n in (1,4,7):
        x=0
    elif n in (2,5,8):
        x=1
    elif n in (3,6,9):
        x=2

    return (x,y)
        

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for col in range(3):
            print("|   ", board[row][col], "   ", sep="", end="")
        print("|")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    user_moved = False

    while not user_moved:
        n = int(input("Enter your move: "))
        x,y = convert_n_to_xy(n)

        if board[y][x] not in ('O','X'):
            board[y][x] = "O"
            user_moved = True
        else:
            print("Wrong move")
    


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ('X','O'):
                free.append((row,col))
    return free


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return True

    for col in range(3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            return True

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True

    if board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        return True    
    
    return False


def tie(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ('X','O'):
                return False
            
    return True



def draw_move(board):
    free = make_list_of_free_fields(board)
    rand = randrange(len(free))
    row,col = free[rand]
    board[row][col] = 'X'



endgame = False
board = ([i for i in range(1,4)], [i for i in range(4,7)], [i for i in range(7,10)])
board[1][1] = 'X'
display_board(board)    

while not endgame:
    enter_move(board)
    draw_move(board)
    display_board(board)
    
    if victory_for(board, 'O'):
        print("You won!")
        endgame = True
    elif victory_for(board, 'X'):
        print("I won!")
        endgame = True
    elif len(make_list_of_free_fields(board)) == 0:
        print("Tie")
        endgame = True
