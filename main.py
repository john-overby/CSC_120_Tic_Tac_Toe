board = [
  ["-", "-", "-"],
  ["-", "-", "-"],
  ["-", "-", "-"]
]

user = True # when true it refers to x, otherwise o
turns = 0

def print_board(board):
  for row in board:
    for slot in row:
      print(f"{slot} ", end="")
    print()
