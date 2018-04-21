
input_word = raw_input('please input word: ')

length = len(input_word)

for i in range(length):
    if input_word[i].islower():
        print input_word[i].upper(),
    else:
        print input_word[i].lower(),