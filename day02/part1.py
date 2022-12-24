"""

a rock
b paper
c scissors

x rock
y paper
z scissors

total score sum of ea round
score for a single round shape chosen
plus the score for hte outcome
1 rock
2 paper
3 scissors

0 loss
3 draw
6 win

rock = 1
paper = 2
scissors = 3


dict[
    a,rock
    b,paper
    c,scissors
    x,rock
    y,paper
    z,scissors
]

"""
file1 = open('input', 'r')
Lines = file1.readlines()

player = 0
you = 0

# dict with values
# scores = 
# {1:rock, 
# 2:paper, 
# 3:scissors}

"""
Rock:     A X
Paper:    B Y
Scissors: C Z
"""

sum = 0
for line in Lines:
    # line: A Y
    parts = line.strip().split(' ')
    l, r = parts[0], parts[1]

    outcome = 0
    match l:
        case "A":
            match r:
                case "X":
                    outcome = 3
                case "Y":
                    outcome = 6
                case "Z":
                    outcome = 0
        case "B":
            match r:
                case "Y":
                    outcome = 3
                case "Z":
                    outcome = 6
                case "X":
                    outcome = 0
        case "C":
            match r:
                case "Z":
                    outcome = 3
                case "X":
                    outcome = 6
                case "Y":
                    outcome = 0

    play = 0  
    match r:
        case "X":
            play = 1
        case "Y":
            play = 2
        case "Z":
            play = 3
    
    round = play + outcome
    sum += round

print(sum)