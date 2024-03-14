total_credit = 0
total_score = 0

sco = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

for i in range(20):
    subject, credit, score = input().split()
    print(subject, credit, score)

    if score == 'P':
        continue
    elif score == 'A+':
        total_credit += float(credit)
        total_score += sco[0] * float(credit)
    elif score == 'A0':
        total_credit += float(credit)
        total_score += sco[1] * float(credit)
    elif score == 'B+':
        total_credit += float(credit)
        total_score += sco[2] * float(credit)
    elif score == 'B0':
        total_credit += float(credit)
        total_score += sco[3] * float(credit)
    elif score == 'C+':
        total_credit += float(credit)
        total_score += sco[4] * float(credit)
    elif score == 'C0':
        total_credit += float(credit)
        total_score += sco[5] * float(credit)
    elif score == 'D+':
        total_credit += float(credit)
        total_score += sco[6] * float(credit)
    elif score == 'D0':
        total_credit += float(credit)
        total_score += sco[7] * float(credit)
    elif score == 'F':
        total_credit += float(credit)
        total_score += sco[8] * float(credit)

if total_credit != 0:
    print(f"{total_score / total_credit:.6f}")
else:
    print(0.000000)