file1 = open('input.txt', 'r')
Lines = file1.readlines()

raw_gameboard = Lines[0:8]
raw_gameboard.reverse()
#print(raw_gameboard)

def create_gameboard():
    gameboard = [[],[],[],[],[],[],[],[],[]]

    for line in raw_gameboard:

        line = line.rstrip('\n')

        part1 = line[1]
        #print(part1)
        part2 = line[5]
        #print(part2)
        part3 = line[9]
        #print(part3)
        part4 = line[13]
        #print(part4)
        part5 = line[17]
        #print(part5)
        part6 = line[21]
        #print(part6)
        part7 = line[25]
        #print(part7)
        part8 = line[29]
        #print(part8)
        part9 = line[33]
        #print(part9)

        if part1 != ' ':
            gameboard[0].append(part1)
            #print(part1)
            
        if part2 != ' ': 
            gameboard[1].append(part2)
            #print(part2)

        if part3 != ' ':
            gameboard[2].append(part3)
            #print(part3)
        if part4 != ' ':
            gameboard[3].append(part4)
            #print(part3)

        if part5 != ' ':
            gameboard[4].append(part5)
        #print(part3)

        if part6 != ' ':
            gameboard[5].append(part6)
        #print(part3)

        if part7 != ' ':
            gameboard[6].append(part7)
        #print(part3)

        if part8 != ' ':
            gameboard[7].append(part8)
        #print(part3)

        if part9 != ' ':
            gameboard[8].append(part9)
        #print(part3)

    #print(gameboard)
    return gameboard
gameboard = create_gameboard()
#print(gameboard)    

raw_instructions = Lines[10:]
#print(raw_instructions)

for line in raw_instructions:

    second_set = line.rstrip('\n').split(' ')
    howmany = int(second_set[1])
    takestack = int(second_set[3])
    givestack = int(second_set[5])

    t = []
    for i in range (0,howmany):
        step1 = gameboard[takestack-1].pop()
        t.append(step1)
    gameboard[givestack-1].extend(t[::-1])
      

#print(gameboard)
print("JRVNHHCSJ")
for stack in gameboard:
    print(stack[-1])
    #print(gameboard)

    #take howmany from takestack, remove from take stack, add to givestack



    #print(howmany,takestack,givestack)







#print(gameboard)

#print(gameboard)

    #for i, element in enumerate(line):
        #print(f"{i}: {element}") 