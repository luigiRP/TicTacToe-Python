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

def check_for_winner():
    # your code here
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
    # add commands here (if needed)
