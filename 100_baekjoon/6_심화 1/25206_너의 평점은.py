subject = []
score = []
grade = []

for i in range(20):
    sub, sco, gra = input().split()

    subject.append(sub)
    score.append(sco)
    grade.append(gra)

tmp = 0
score_sum = 0

for i in range(20):

    result = 0.0

    if grade[i] == 'P':
        pass

    else:
        if grade[i] == 'A+':
            result = 4.5

        elif grade[i] == 'A0':
            result = 4.0

        elif grade[i] == 'B+':
            result = 3.5

        elif grade[i] == 'B0':
            result = 3.0

        elif grade[i] == 'C+':
            result = 2.5

        elif grade[i] == 'C0':
            result = 2.0

        elif grade[i] == 'D+':
            result = 1.5

        elif grade[i] == 'D0':
            result = 1.0

        elif grade[i] == 'F':
            result = 0.0

        tmp += int(score[i][0]) * result
        score_sum += int(score[i][0])

print(round(tmp / score_sum, 6))

