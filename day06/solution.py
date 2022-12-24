"""
add subroutine that detects start of packet marker
start is indicated by a sequence of four characters that are all different
identify first position where the four ost recent received character are all diff
report number of characters from beginning to end of first 4 char
"""
file1 = open('input', 'r')
lines = file1.readlines()

line = lines[0]

#Part 1 
#a = 4

#Part 2
a = 14

for i in range(a,len(line)):
    #print(line)
    start = set(line[i-a:i])
    chunk = line[i-a:i]
    #print(chunk)
    if len(start) == a:
        print(i)
        break

#print(start)
