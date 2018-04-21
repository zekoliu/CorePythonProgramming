
def test_score(score):
    if (score < 100 and score >= 90):
        return 'A'
    elif (score < 90 and score >= 80):
        return 'B'
    elif (score < 80 and score >= 70):
        return 'C'
    elif (score < 70 and score >= 60):
        return 'D'
    else:
        return 'F'


score = raw_input("Enter one score: ")
print test_score(eval(score))