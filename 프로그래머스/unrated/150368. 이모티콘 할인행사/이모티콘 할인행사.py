from itertools import product

def dc_price(dc_prod, emoticons):
    lst = []
    for idx,i in enumerate(emoticons):
        lst.append(i*(100-dc_prod[idx]) * 0.01)
    return lst

def solution(users, emoticons):
    
    answer = []
    dc = [10, 20, 30, 40]
    
    for prod in list(product(dc,repeat=len(emoticons))):
        dc_prod = list(prod)
        #prices = dc_price(dc_prod, emoticons)
        tmp1, tmp2 = 0, 0
        for percent, money in users:
            total = 0
            for pro, emo in zip(dc_prod, emoticons):
                if pro >= percent:
                    total += emo * (100-pro) * 0.01
            if total >= money:
                tmp1 += 1
            else:
                tmp2 += total
        answer.append([tmp1, tmp2])
    answer.sort(key = lambda x : (-x[0], -x[1]))
    return answer[0]