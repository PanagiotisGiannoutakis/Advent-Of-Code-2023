import re

file_input = open('AdventOfCode_Day01_Input.txt', 'r')
lines = file_input.readlines()
sum = 0
for line in lines:
    line_splitted = re.findall("[0-9]", line)
    print(line_splitted)
    line_number = line_splitted[0] + line_splitted[(len(line_splitted)-1)]
    sum += int(line_number)
    print(line_splitted[0])
    print(line_splitted[(len(line_splitted)-1)])
    print(int(line_number))
print(sum)
