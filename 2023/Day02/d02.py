
def parse_input(puz):
  games = {}
  for line in puz:
    line = line.replace("Game ", "")
    game_id, pulls = line.split(": ")
    game_id = int(game_id)
    games[game_id] = []
    for pull in pulls.split("; "):
      meda_data = {}
      for cubes in pull.split(", "):
        number, color = cubes.split(" ")
        meda_data[color] = int(number)
      games[game_id].append(meda_data)
  return games

def check_game(game):
  criteria = {'green': 13, 'blue': 14, 'red': 12}
  for cubes in game:
    for color, number in cubes.items():
      if number > criteria[color]:
        return False
  return True

def find_min(game):
  criteria = {'green': 0, 'blue': 0, 'red': 0}
  for cubes in game:
    for color, number in cubes.items():
      if number > criteria[color]:
        criteria[color] = number
  cubic = 1
  for color, number in criteria.items():
    cubic *= number
  return cubic

def check_Cubes(games):
  cum_sum = 0
  cum_sum_2 = 0
  for game_id, pulls in games.items():
    cum_sum_2 += find_min(pulls)
    if check_game(pulls):
      cum_sum += game_id
  print(f"Answer 1: {cum_sum}")
  print(f"Answer 2: {cum_sum_2}")





puz_string = []
with open("input.txt", "r") as file:
  for line in file:
    line = line.strip('\n')
    puz_string.append(line)

puz1 = parse_input(puz_string)
check_Cubes(puz1)