def solution(today, terms, privacies):
    answer = []
    t_year,t_month,t_date = today.split('.')

    for i in range(len(privacies)):
        a,b = privacies[i].split()
        year,month,date = a.split('.')
        for j in range(len(terms)):
            #x = A, y = 6
            x,y = terms[j].split()
            if b == x:
                tmp1,tmp2,tmp3 = int(year), int(month), int(date)
                tmp1 += int(y) // 12
                tmp2 += int(y) % 12
                if tmp2 > 12:
                    tmp1 += 1
                    tmp2 -= 12
                tmp3 -= 1
                if tmp3 == 0:
                    tmp3 = 28
                    tmp2 -= 1
                if tmp1 < int(t_year):
                    answer.append(i+1)
                elif tmp1 == int(t_year):
                    if tmp2 < int(t_month):
                        answer.append(i+1)
                    elif tmp2 == int(t_month):
                        if tmp3 < int(t_date):
                            answer.append(i+1)
                    
                
    return answer