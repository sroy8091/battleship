# check the print statement which prints the position

from random import randint

board = []
board2= []
percent=0
percent2=0 
count=0
count2=0
overall=0
overall2=0
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
    return randint(1, len(board) - 2)

def random_col(board):
    return randint(1, len(board) - 2)

ship_row_main = random_row(board)
ship_col_main = random_col(board)

ship_row_main2 = random_row(board2)
ship_col_main2 = random_col(board2)

ship_row_side = random_row(board)
ship_col_side = random_col(board)

while (ship_row_side in range((ship_row_main-1),(ship_row_main+1))) and (ship_col_side in range((ship_col_main-1), (ship_col_main+1))):
    ship_row_side = random_row(board)
    ship_col_side = random_col(board)

ship_row_side2 = random_row(board)
ship_col_side2 = random_col(board)

while (ship_row_side2 in range((ship_row_main-1),(ship_row_main+1))) and (ship_col_side2 in range((ship_col_main-1), (ship_col_main+1))) or (ship_row_side2 == ship_row_side and ship_col_side == ship_col_side+1):
    ship_row_side2 = random_row(board)
    ship_col_side2 = random_col(board)

ship_row_side21 = random_row(board)
ship_col_side21 = random_col(board)

while (ship_row_side21 in range((ship_row_main2-1), (ship_row_main2+1))) and (ship_col_side21 in range((ship_col_main2-1), (ship_col_main2+1))):
    ship_row_side21 = random_row(board)
    ship_col_side21 = random_col(board)

ship_row_side22 = random_row(board)
ship_col_side22 = random_col(board)

while (ship_row_side22 in range((ship_row_main2-1), (ship_row_main2+1))) and (ship_col_side22 in range((ship_col_main2-1), (ship_col_main2+1))) or (ship_row_side22 == ship_row_side21 and ship_col_side21 == ship_col_side22):
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
    if (guess_row == ship_row_main+1 and guess_col == ship_col_main+1) or (guess_row == ship_row_main-1 and guess_col == ship_col_main-1):
        count+=1
        if count==1 and percent==0:
            print "33.33% damage to main ship"
            overall=15
            print "15% overall damage"
        elif count==2 and percent==0:
            print "66.66% damage to main ship"
            overall=30
            print "30% overall damage"
        elif count==1 and percent==1:
            print "33.33% damage to main ship"
            print "40% overall damage"
            overall=40
        elif count==2 and percent==1:
            print "66.66% damage to main ship"
            print "55% overall damage"
            overall=55
        elif count==1 and percent==2:
            print "33.33% damage to main ship"
            print "65% overall damage"
            overall=65
        elif count==1 and percent==2:
            print "33.33% damage to main ship"
            print "65% overall damage"
            overall=65
        elif count==2 and percent==2:
            print "66.66% damage to main ship"
            print "80% overall damage"
            overall=80
    
    elif (guess_row == ship_row_side and guess_col == ship_col_side) or (guess_row == ship_row_side2 and guess_col == ship_col_side2):
        percent=percent+1
        if percent==1 and count==0:
            print "You have just sunked my side boat and done 25% overall damage."
            overall=25
        elif percent==2 and count==0:
            print "You have just sunked my side boat and done 50% overall damage."
            overall=50
        elif percent==1 and count==1:
            print "You have just sunked my side boat and done 40% overall damage."
            overall=40
        elif percent==2 and count==1:
            print "You have just sunked my side boat and done 65% overall damage."
            overall=65
        elif percent==1 and count==2:
            print "You have just sunked my side boat and done 55% overall damage."
            overall=55
        elif percent==2 and count==2:
            print "You have just sunked my side boat and done 80% overall damage."
            overall=80
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
    if (guess_row == ship_row_main2+1 and guess_col == ship_col_main2+1) or (guess_row == ship_row_main2-1 and guess_col == ship_col_main2-1):
        count2+=1
        if count2==1 and percent2==0:
            print "33.33% damage to main ship"
            overall2=15
            print "15% overall2 damage"
        elif count2==2 and percent2==0:
            print "66.66% damage to main ship"
            overall2=30
            print "30% overall2 damage"
        elif count2==1 and percent2==1:
            print "33.33% damage to main ship"
            print "40% overall2 damage"
            overall2=40
        elif count2==2 and percent2==1:
            print "66.66% damage to main ship"
            print "55% overall2 damage"
            overall2=55
        elif count2==1 and percent2==2:
            print "33.33% damage to main ship"
            print "65% overall2 damage"
            overall2=65
        elif count2==1 and percent2==2:
            print "33.33% damage to main ship"
            print "65% overall2 damage"
            overall2=65
        elif count2==2 and percent2==2:
            print "66.66% damage to main ship"
            print "80% overall2 damage"
            overall2=80
    
    elif (guess_row == ship_row_side21 and guess_col == ship_col_side21) or (guess_row == ship_row_side22 and guess_col == ship_col_side22):
        percent2=percent2+1
        if percent2==1 and count2==0:
            print "You have just sunked my side boat and done 25% overall damage."
            overall2=25
        elif percent2==2 and count2==0:
            print "You have just sunked my side boat and done 50% overall damage."
            overall2=50
        elif percent2==1 and count2==1:
            print "You have just sunked my side boat and done 40% overall damage."
            overall2=40
        elif percent2==2 and count2==1:
            print "You have just sunked my side boat and done 65% overall damage."
            overall2=65
        elif percent2==1 and count2==2:
            print "You have just sunked my side boat and done 55% overall damage."
            overall2=55
        elif percent2==2 and count2==2:
            print "You have just sunked my side boat and done 80% overall damage."
            overall2=80
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
        if overall2>overall:
            print name2+" wins"
        elif overall>overall2:
            print name1+" wins"
        else:
            print "Match draw"
