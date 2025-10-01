path = "C:\\Users\giann\Desktop\Day 02\AdventOfCode_Day02_Input.txt"
with open(path) as file:
    lines = [line.rstrip() for line in file]
sum = 0
for line in lines:
    sumGame = 0
    games = line.split(": ")[1]
    bags = games.split("; ")
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    for bag in bags:
        cubes = bag.split(", ")
        for cube in cubes:
            number_of_cubes = int(cube.split(" ")[0])
            if "red" in cube:
                if number_of_cubes >= maxRed:
                    maxRed = number_of_cubes
            elif "green" in cube:
                if number_of_cubes >= maxGreen:
                    maxGreen = number_of_cubes
            elif "blue" in cube:
                if number_of_cubes >= maxBlue:
                    maxBlue = number_of_cubes
            else:
                maxRed = 1
                maxGreen = 1
                maxBlue = 1
    sumGame = maxRed * maxGreen * maxBlue
    sum += sumGame

print(sum)