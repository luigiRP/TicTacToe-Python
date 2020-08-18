

def play(position, current_player,board):

    board[int(position)-1] = current_player
    return board


def check_for_winner(board, current_player):
    # your code here
    
    winning_combinations=[
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    for i in winning_combinations:
        [a,b,c]=i
        if board[a]!='-' and board[b]!='-' and board[c]!='-' and board[a]==board[b] and board[b]==board[c]:
            print(current_player + " Won!")
            return True
        
    return False

  


def new_game(board):
    # your code here
    for i in range(len(board)):
        board[i] = "-"
    return board


def print_board(board,current_player):
    if current_player == "O":
        current_player = "X"
    else:
        current_player = "O"
    print(f"""
    Current board ({current_player} turn):

    [{board[0]}] [{board[1]}] [{board[2]}]
    [{board[3]}] [{board[4]}] [{board[5]}]
    [{board[6]}] [{board[7]}] [{board[8]}]
    """)


def main():
    current_player = "O"
    stop = False
    board = [
        "-", "-", "-",
        "-", "-", "-",
        "-", "-", "-",
    ]
    
    while stop == False:
        command = input("What do you want?: ")
        if command == "reset":
            current_player = "O"
            board=new_game(board)
            print_board(board, current_player)
        elif "play " in command:
            command = command.split()
            
            if int(command[1]) < 1 or int(command[1]) > 9:
                print("Input not valid, try again")
            elif board[int(command[1])-1] != "-":
                print("Position already played")
            else:
                if current_player == "O":
                    current_player = "X"
                else:
                    current_player = "O"
                board=play(command[1], current_player, board)
                print_board(board, current_player)
                if check_for_winner(board, current_player):
                    current_player = "O"
                    board=new_game(board)
                    print_board(board, current_player)
        elif command == "stop":
            stop = True

    
main()
