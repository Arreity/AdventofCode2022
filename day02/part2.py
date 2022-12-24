"""
"""
file1 = open('input', 'r')
Lines = file1.readlines()

"""
Rock:     A 
Paper:    B 
Scissors: C 
"""

sum = 0
for line in Lines:
    # line: A Y
    parts = line.strip().split(' ')
    opponent, hand = parts[0], parts[1]
    

    play = 0
    match opponent:
        case "A":
            match hand:
                case "X":
                    play = 3
                case "Y":
                    play = 1
                case "Z":
                    play = 2
        case "B":
            match hand:
                case "X":
                    play = 1
                case "Y":
                    play = 2
                case "Z":
                    play = 3
        case "C":
            match hand:
                case "X":
                    play = 2
                case "Y":
                    play = 3
                case "Z":
                    play = 1

    outcome = 0  
    match hand:
        case "X":
            outcome = 0
        case "Y":
            outcome = 3
        case "Z":
            outcome = 6
    
    
    round = play + outcome
    sum += round

print(sum)

#x loose y draw z win 
#firt column players
#second columns how round ends r = p + o solve for p
#opponent +
