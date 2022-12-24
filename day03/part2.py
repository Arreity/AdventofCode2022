file1 = open('input', 'r')
lines = file1.readlines()

total = 0

for i in range(0, len(lines), 3):
    set_of_three = lines[i:i+3]

    common_letters = set()

    for string in set_of_three:

        #common_letters = set()

        s = string.rstrip()
        unique_letters = set(s)
        #print(set_of_three)

        if string == set_of_three[0]:
            common_letters = unique_letters
            #print(common_letters)
        else:
            common_letters = common_letters.intersection(unique_letters)
        # Update common_letters_all to be the intersection of common_letters_all and common_letters
        #common_letters_all = unique_letters.intersection(common_letters)

    print(common_letters)
    

    letter = list(common_letters)[0]

    if letter.isupper():
        value = ord(letter) - ord('A') + 27
    else:
        value = ord(letter) - ord('a') + 1
    total += value

print(total)

#print(common_letters_list, total)
    # Print the letter and its value to check if they are being computed correctly
    # print(f"letter: {letter}, value: {value}")




