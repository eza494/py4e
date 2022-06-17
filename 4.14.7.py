try:
    Grade = float(input('Enter Score: '))
except :
    print('Bad Score')
    exit()

def computegrade(grade):
    if grade > 1 or grade< 0:
        return 'Bad Score'
    elif grade >=0.9:
        return 'A'
    elif grade >=0.8:
        return 'B'
    elif grade >=0.7:
        return 'C'
    elif grade >= 0.6:
        return 'D'
    elif grade <0.6 :
        return 'F'

score = computegrade(Grade)
print(score)
