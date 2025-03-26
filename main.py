spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def check_win(spaces, player):
  combinations = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
  for combination in combinations:
    if spaces[combination[0]] == player and spaces[combination[1]] == player and spaces[combination[2]] == player:
      return True
return False