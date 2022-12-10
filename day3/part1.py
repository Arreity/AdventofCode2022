import re
"""
ea rucksack 2 large compartments
1 item per sack wrong
lower and upercase different items

comman letter in half of line, get length of line and split
assign number to ea letter
gather sum of duplicates
lower case 1-26
uppercase 27-56
"""
"""                             
    newlist = line()
    size = 2
    for i in range(0, len(line), size):
        newlist.append(line[i:i+size])


    #sum += #(value in dup) 
#def rucksack(l,r):

    #print(f"parts: {l},{r} -- {dup}")
    #test = re.split([''],parts, maxsplit=2)
   # print("Lines{}: {}".format(count, line.strip()))
#in split store

#def get_value(c):
    #lookupmap = { 'a': 1}
    #lookupstr = ".abcdef"

"""
file1 = open('input', 'r')
Lines = file1.readlines()

sum = 0
for line in Lines:
    l,r = line[:len(line)//2], line[len(line)//2:]                    
   
    comp1u = set(l)
    comp2u = set(r)

    doops = comp1u & comp2u

    duplicates = doops

    for duplicate in duplicates:
        if duplicate.isupper():
            value = ord(duplicate) - ord('A') + 27
        else:
            value = ord(duplicate) - ord('a') + 1
        sum += value 

        print(f"letter:{duplicate}, Number:{value}")
    #print(value)
print(sum)


