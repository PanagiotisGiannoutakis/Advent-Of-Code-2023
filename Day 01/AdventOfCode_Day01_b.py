import re

file_input = open('AdventOfCode_Day01_Input.txt', 'r')
lines = file_input.readlines()
sum = 0
for line in lines:
    line_splitted = re.findall(
        "[0-9]|oneight|threeight|fiveight|sevenine|nineight|twone|eightwo|one|two|three|four|five|six|seven|eight|nine", line)
    print(line)
    print(line_splitted)
    for index, splitted in enumerate(line_splitted, start=0):
        match splitted:
            case "one":
                line_splitted[index] = "1"
            case "two":
                line_splitted[index] = "2"
            case "three":
                line_splitted[index] = "3"
            case "four":
                line_splitted[index] = "4"
            case "five":
                line_splitted[index] = "5"
            case "six":
                line_splitted[index] = "6"
            case "seven":
                line_splitted[index] = "7"
            case "eight":
                line_splitted[index] = "8"
            case "nine":
                line_splitted[index] = "9"
            case "oneight":
                line_splitted[index] = "1"
                line_splitted.insert(index+1, "8")
            case "threeight":
                line_splitted[index] = "3"
                line_splitted.insert(index+1, "8")
            case "fiveight":
                line_splitted[index] = "5"
                line_splitted.insert(index+1, "8")
            case "sevenine":
                line_splitted[index] = "7"
                line_splitted.insert(index+1, "9")
            case "nineight":
                line_splitted[index] = "9"
                line_splitted.insert(index+1, "8")
            case "twone":
                line_splitted[index] = "2"
                line_splitted.insert(index+1, "1")
            case "eightwo":
                line_splitted[index] = "8"
                line_splitted.insert(index+1, "2")
    line_number = line_splitted[0] + line_splitted[(len(line_splitted)-1)]
    print(line_splitted)
    print(line_splitted[0])
    print(line_splitted[(len(line_splitted)-1)])
    print(int(line_number))

    sum += int(line_number)
print(sum)

