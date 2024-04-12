import re

def solution(files):
    answer = []
    tmp = [re.split("([0-9]+)", s) for s in files]
    
    sort = sorted(tmp, key = lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(s) for s in sort]