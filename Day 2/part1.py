# Define game constraint
config = { "red": 12, "green": 13, "blue": 14 }
game_rec = 0
with open('input.txt', 'r') as games:

    # Read through each game
    for game in games.readlines():

        # Define game validator
        is_valid = True

        # Separate into matches
        matches = game.split(':')[1].split(';')

        # Check match validity
        for match in matches:

            # Get cubes
            cubes = match.split(',')

            # If an invalid match has been found break the loop
            if not is_valid:
                break
            else:

                # Check each cube color and value against the configuration provided @config={} if config is not met
                # break nested loop
                for cube in cubes:
                    if cube.__contains__("red"):
                        cube_value = int(cube.split(' ')[1])
                        if cube_value > config.get('red'):
                            is_valid = False
                            break
                    elif cube.__contains__("green"):
                        cube_value = int(cube.split(' ')[1])
                        if cube_value > config.get('green'):
                            is_valid = False
                            break
                    elif cube.__contains__("blue"):
                        cube_value = int(cube.split(' ')[1])
                        if cube_value > config.get('blue'):
                            is_valid = False
                            break

        # If game checking has ended and game is valid then add game number
        if is_valid:
            game_rec = game_rec + int(game.split(':')[0].split(' ')[1])

# Sum all the game number values in set
print(game_rec)
