current_player = "X"
stop = False
board = [
    "-","-","-",
    "-","-","-",
    "-","-","-",
]

def play(position):
    global current_player
    # your code here
    if board[position] != "-":
        print("Already plaid")
        return None

    board[position] = current_player
    if check_for_winner() == True:
        print("🥳 We have a winner!: "+current_player)
        stop = True
        return None
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def check_for_winner():
    global current_player
    # your code here
    cp = current_player
    b = board
    if ((b[0] == cp and b[1] == cp and b[2] == cp) or
    (b[3] == cp and b[4] == cp and b[5] == cp) or
    (b[6] == cp and b[7] == cp and b[8] == cp) or

    (b[0] == cp and b[3] == cp and b[6] == cp) or
    (b[1] == cp and b[4] == cp and b[7] == cp) or
    (b[2] == cp and b[5] == cp and b[8] == cp) or
    
    (b[0] == cp and b[4] == cp and b[8] == cp) or
    (b[6] == cp and b[4] == cp and b[2] == cp)):
        return True
    return False

def new_game():
    # your code here
    pass

def print_board():
    print(f"""
    Current board ({current_player} turn):

    [{board[0]}] [{board[1]}] [{board[2]}]
    [{board[3]}] [{board[4]}] [{board[5]}]
    [{board[6]}] [{board[7]}] [{board[8]}]
    """)

while stop == False:
    command = input("What do you want?: ")

    if command == "stop":
        stop = True
    if command == "print":
        print_board()
    if command == "play":
        position = input("Position:")
        play(int(position))
        print_board()
    # add commands here (if needed)
