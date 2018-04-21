
f = open('/home/jenenliu/Desktop/test.txt')
vowel_num = 0
consonant = 0
word_num = 0
for line in f:
    # print line
    for word in line:
        # print word
        if word in 'aeiou':
            vowel_num+=1
        elif word not in 'aeiou':
            consonant+=1
        elif word == ' ':
            word_num+=1
f.close()

print  word_num, vowel_num, consonant