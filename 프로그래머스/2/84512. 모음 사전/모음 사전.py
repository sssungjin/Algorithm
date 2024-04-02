from itertools import product

def solution(word):
    arr = []
    words = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        for c in product(words, repeat = i):
            arr.append(''.join(list(c)))
        
    arr.sort()
    return arr.index(word) + 1
