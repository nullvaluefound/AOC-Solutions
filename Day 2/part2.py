import math

with open('input.txt', 'r') as games:

    # Define sum variable and read through input data
    total_powers = 0
    for game in games.readlines():

        # Define local variables
        matches = game.split(':')[1].split(';')
        red_cubes = []
        green_cubes = []
        blue_cubes = []

        # Loop through each match within a game to find the match maximum value
        for match in matches:
            rnds = match.split(',')
            for rnd in rnds:
                cube_items = rnd.split(' ')
                cube_value = cube_items[1]
                cube_color = cube_items[2]

                # Append each color cube and their value to a list
                if cube_color.__contains__('red'):
                    red_cubes.append(int(cube_value))
                elif cube_color.__contains__('green'):
                    green_cubes.append(int(cube_value))
                elif cube_color.__contains__('blue'):
                    blue_cubes.append(int(cube_value))

        # Sort the list to get the maximum value for each color
        red_cubes = sorted(red_cubes)
        green_cubes = sorted(green_cubes)
        blue_cubes = sorted(blue_cubes)

        # Perform AOC instruction which is to get the product of all the maximum values in each color for each game
        # Get game power of cubes
        powers = int(red_cubes.pop()) * int(green_cubes.pop()) * int(blue_cubes.pop())

        # Add to total sum of powers
        total_powers = total_powers + powers

    # Once done looping through all the games present the grand total
    print(total_powers)
