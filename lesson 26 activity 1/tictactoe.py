import random
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-"*9)
def check_winner(board,player):
    for i in range(3):
        if all(board[i][j]==player for j in range(3)):
            return True
        if all(board[j][i]==player for j in range(3)):
            return True
    if all (board[i][i]==player for i in range(3)):
        return True
    if all (board[i][2-i]==player for i in range(3)):
        return True
    return False
def is_full(board):
    return all(cell!=""for row in board for cell in row)
def player_move(board,player):
    while True:
        try:
            move=int(input(f"player {player},enter ur move(1-9)"))
            if move <1 or move >9:
                print("invalid! pls enter 1-9")
                continue
            row,col=divmod(move-1,3)
            if board[row][col]=="":
                board[row][col]= player
                break
            else:
                print("cell already taken,try again")
        except ValueError:
            print("enter a valid number")
def tic_tac_toe():
    board=[[""for _ in range(3)]for _ in range(3)]
    current_player=random.choice(["x","0"])
    print("welcome to tic tac toe")
    print_board(board)
    while True:
        player_move(board,current_player)
        print_board(board)
        if check_winner(board,current_player):
            print(f"player{current_player}wins!!")
            break
        if is_full(board):
            print("its a draw!!")
            break
        current_player= "0"if current_player=="x"else"x"
if __name__=="__main__":
   tic_tac_toe()