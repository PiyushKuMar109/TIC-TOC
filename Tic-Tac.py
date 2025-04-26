def sum(a, b, c):
    return a + b + c

def printBoard(xState, zState):
    symbols = [' ', 'X', 'O']  # Add symbols for empty, X, and O
    board = [symbols[x] for x in xState]
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def checkWin(xState, zState):
 # Define all possible winning combinations
 wins = [ [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6] ]

 # Iterate through all possible winning combinations
 for win in wins:
    # Check if x has won the match
    if(sum(xState[win[0]],xState[win[1]],xState[win[2]])==3):
      print("x Won the match")
      return 1

    # Check if z has won the match
    if(sum(zState[win[0]],zState[win[1]],zState[win[2]])==3):
      print("O Won the match")
      return 0

 # If no one has won the match, return -1
 return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    
    while True:
        printBoard(xState, zState)
        if turn == 1:
            print("X's chance")
            value = int(input("Please enter a value: "))
            if xState[value] == 0 and zState[value] == 0:  # Check if the cell is empty
                xState[value] = 1
            else:
                print("Invalid move. The cell is already occupied.")
                continue
        else:
            print("O's chance")
            value = int(input("Please enter a value: "))
            if xState[value] == 0 and zState[value] == 0:  # Check if the cell is empty
                zState[value] = 1
            else:
                print("Invalid move. The cell is already occupied.")
                continue

        cwin = checkWin(xState, zState)
        if cwin != -1:
            print("Match over")
            break
        turn = 1 - turn
