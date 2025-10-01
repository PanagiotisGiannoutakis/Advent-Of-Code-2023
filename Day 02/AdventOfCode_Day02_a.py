path = "C:\\Users\giann\Desktop\Day 02\AdventOfCode_Day02_Input.txt"
with open(path) as file:
    lines = [line.rstrip() for line in file]
sum = 0
for line in lines:
    games = line.split(": ")[1]
    bags = games.split("; ")
    flag = True
    for bag in bags:
        cubes = bag.split(", ")
        for cube in cubes:
            number_of_cubes = cube.split(" ")
            if "green" in cube:
                if int(number_of_cubes[0]) <= 13:
                    flag = True
                else:
                    flag = False
                    break
            elif "blue" in cube:
                if int(number_of_cubes[0]) <= 14:
                    flag = True
                else:
                    flag = False
                    break
            elif "red" in cube:
                if int(number_of_cubes[0]) <= 12:
                    flag = True
                else:
                    flag = False
                    break
            else:
                print("aaa")
        if flag == False:
            break
    
    if flag == True:
        sum += int(line.split(" ")[1].split(":")[0])
    else:
        sum += 0
print(sum)