from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    
    today_yyyy = int(today[:4])
    today_mm = int(today[5:7])
    today_dd = int(today[8:10])
    
    today_int = today_dd + today_mm * 100 + today_yyyy * 10000
    
    for term in terms:
        term_type, expire_period = term.split()
        
        terms_dict[term_type] = expire_period
    
    print(terms_dict.items())
    
    idx = 1
    
    for privacy in privacies:
        date, term_type = privacy.split()
        yyyy = int(date[:4])
        mm = int(date[5:7])
        dd = int(date[8:10])
        
        expire_period = int(terms_dict[term_type])
        
        print(yyyy, mm, dd, expire_period)
        
        yyyy += expire_period // 12
        
        mm += expire_period % 12
        
        if mm > 12:
            mm = mm % 12
            yyyy += 1
        
        expire_int = dd + mm * 100 + yyyy * 10000
        
        print(expire_int)
        print(today_int)
        if expire_int <= today_int:
            answer.append(idx)
        
        idx += 1
        
    return answer