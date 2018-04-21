import random

all_situaion = ['stone', 'sciors', 'cloth']

player = int(raw_input('Please out first: '))

computer = random.randint(0, 3)

if (player == computer):
    print 'player out', all_situaion[player], 'computer out', all_situaion[computer], 'player and computer tie'
elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print 'player out', all_situaion[player], 'computer out', all_situaion[computer], ', player victory'
elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print 'player out', all_situaion[player], 'computer out', all_situaion[computer], ', computer victory'
