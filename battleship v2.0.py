# check the print statement which prints the position

from random import randint

board = []
board2= []
percent=0
percent2=0 

for x in range(5):
    board.append(["O"] * 5)

for y in range(5):
    board2.append(["O"]*5)


print "Let's play Battleship!"
print "Rules:  There are two side boats and one main boat. You have to sunk the main boat"
name1= raw_input("Player1 name:")
name2= raw_input("Player2 name:")

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

ship_row_main = random_row(board)
ship_col_main = random_col(board)

ship_row_main2 = random_row(board2)
ship_col_main2 = random_col(board2)

ship_row_side = random_row(board)
ship_col_side = random_col(board)

while ship_row_side == ship_row_main and ship_col_side == ship_col_main:
    ship_row_side = random_row(board)
    ship_col_side = random_col(board)

ship_row_side2 = random_row(board)
ship_col_side2 = random_col(board)

while (ship_row_side2 == ship_row_main and ship_col_side2 == ship_col_main) or (ship_row_side2 == ship_row_side and ship_col_side2 == ship_col_side):
    ship_row_side2 = random_row(board)
    ship_col_side2 = random_col(board)

ship_row_side21 = random_row(board)
ship_col_side21 = random_col(board)

while ship_row_side21 == ship_row_main2 and ship_col_side21 == ship_col_main2:
    ship_row_side21 = random_row(board)
    ship_col_side21 = random_col(board)

ship_row_side22 = random_row(board)
ship_col_side22 = random_col(board)

while (ship_row_side22 == ship_row_main2 and ship_col_side22 == ship_col_main2) or (ship_row_side22 == ship_row_side21 and ship_col_side22 == ship_col_side21):
    ship_row_side22 = random_row(board)
    ship_col_side22 = random_col(board)


# here in loops guess_row or guess_col is of opponent players position

for turn in range(5):
    print name1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship_row_main and guess_col == ship_col_main:
        print "Congratulations! You sunk my battleship!"
        print name1+" wins"
        break
    elif (guess_row == ship_row_side and guess_col == ship_col_side) or (guess_row == ship_row_side2 and guess_col == ship_col_side2):
        percent=percent+1
        if percent==1:
            print "You have just sunked my side boat and done 33% damage."
        else:
            print "You have just sunked my side boat and done 66% damage."
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!" 
            board[guess_row][guess_col] = "X"
            print_board(board)

            
    print name2
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship_row_main2 and guess_col == ship_col_main2:
        print "Congratulations! You sunk my battleship!"
        print name2+" wins"
        break
    elif (guess_row == ship_row_side21 and guess_col == ship_col_side21) or (guess_row == ship_row_side22 and guess_col == ship_col_side22):
        percent2=percent2+1
        if percent2==1:
            print "You have just sunked my side boat and done 33% damage."
        else:
            print "You have just sunked my side boat and done 66% damage."
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board2[guess_row][guess_col] == "Y"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!" 
            board2[guess_row][guess_col] = "Y"
            print_board(board2)

    
    print "Turn", turn+1
        
    if turn==4:
        if percent2>percent:
            print name2+" wins"
        elif percent2<percent:
            print name1+" wins"
        else:
            print "Match draw"
