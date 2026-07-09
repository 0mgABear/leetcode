#Implementing Tic Tac Toe in Python - Prep for Interview
def isWin(board):
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
      return board[i][0]
  for i in range(3):
    if board[0][i] == board[1][i] == board[2][i] and board[i][0] != "":
      return board[0][i]
  if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]) and board[1][1] != "":
    return board[1][1]
  return None 

def isValidBoard(board):
  count_x = sum(row.count("X") for row in board)
  count_o = sum(row.count("O") for row in board)
  if count_x != count_o and count_x != count_o + 1:
        return False

  winner = isWin(board)
  if winner == "X":
    return count_x == count_o + 1      
  elif winner == "O":
    return count_x == count_o
  # no winner - just check counts
  return True

def main():
    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
    
    turns = ["X", "O"]
    current_turn = 0
    
    def isValidMove(i, j, board):
      if i < 0 or i > 2 or j < 0 or j > 2:
          return False
      if board[i][j] != "":
          return False
      return True
    
    def isFull(board):
        return all(board[i][j] != "" for i in range(3) for j in range(3))
    
    while isWin(board) is None and not isFull(board):
        current = turns[current_turn]
        
        x = int(input(f"Player {current}, enter row (e.g. 0 1): "))
        y = int(input(f"Player {current}, enter col (e.g. 0 1): "))

        if isValidMove(x, y, board):
            board[x][y] = current
            current_turn = (current_turn + 1) % 2
        else:
            print("Invalid move, try again")
    
    winner = isWin(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("Draw!")

main()




