file1 = open('input', 'r')
Lines = file1.readlines()
 
sum = 0
elves = []
#creating list that stores elves with sum of calories, grab 3 max elves
# Strips the newline character
for line in Lines:
    if line == "\n": # when the line is only a newline we've reached a new elf
        elves.append(sum)
        sum = 0
        continue
    sum += int(line)
elves.sort(reverse = True)

print(elves[0]+elves[1]+elves[2])
