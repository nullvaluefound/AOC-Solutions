config = { "red": 12, "green": 13, "blue": 14 }
game_rec = set()
with open('input.txt', 'r') as games:

    for game in games.readlines():
        is_valid = True
        matches = game.split(':')[1].split(';')
        for match in matches:
            rounds = match.split(',')
            if not is_valid:
                break
            else:
                for game_round in rounds:
                    if game_round.__contains__("red"):
                        if int(game_round.split(' ')[1]) > config.get('red'):
                            is_valid = False
                            break
                    elif game_round.__contains__("green"):
                        if int(game_round.split(' ')[1]) > config.get('green'):
                            is_valid = False
                            break
                    elif game_round.__contains__("blue"):
                        if int(game_round.split(' ')[1]) > config.get('blue'):
                            is_valid = False
                            break
        if is_valid:
            game_rec.add(int(game.split(':')[0].split(' ')[1]))
print(sum(sorted(game_rec)))
