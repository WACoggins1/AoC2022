rounds = open('rpsRounds.txt', 'r')

rounds = rounds.read().strip().split('\n')

print(rounds)

score = 0
#A (r) B(p) C(s)
#X (r1) Y (p2) Z (s3)
#win = 6, draw = 3, lose = 0
score2 = 0

for k in rounds:
    if k == 'A X':
        score += 4
    elif k == 'A Y':
        score += 8
    elif k =='A Z':
        score += 3
    elif k =='B X':
        score += 1
    elif k =='B Y':
        score += 5
    elif k =='B Z':
        score += 9
    elif k =='C X':
        score += 7
    elif k =='C Y':
        score += 2
    elif k =='C Z':
        score += 6

print("Following conventional methods, you scored: ", score)

#update scoring policy
for k in rounds:
    if k == 'A X':
        score2 += 3
    elif k == 'A Y':
        score2 += 4
    elif k =='A Z':
        score2 += 8
    elif k =='B X':
        score2 += 1
    elif k =='B Y':
        score2 += 5
    elif k =='B Z':
        score2 += 9
    elif k =='C X':
        score2 += 2
    elif k =='C Y':
        score2 += 6
    elif k =='C Z':
        score2 += 7


print("Using the update cipher, you scored: ", score2)
