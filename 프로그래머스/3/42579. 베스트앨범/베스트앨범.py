from collections import defaultdict

def solution(genres, plays):
    answer = []
    dic = defaultdict(list)
    
    idx = 0
    
    genre_set = set(genres)
   # print(genre_set)
    
    genre_plays = defaultdict(int)
    
    for genre, play in zip(genres, plays):
        #print(genre, play)
        genre_plays[genre] += play
        dic[genre].append((play, idx))
        idx += 1
    
    new_arr = []
    for key, val in genre_plays.items():
        new_arr.append((val, key))
    
    new_arr.sort(reverse = True)
   # print(new_arr)
    
    for key, val in dic.items():
        dic[key].sort(key = lambda x: (-x[0], x[1]))
    #    print(key, val)
    
    for plays, genre in new_arr:
        if len(dic[genre]) >= 2:
            for i in range(2):
               # print((dic[genre][i][1]))
                answer.append(dic[genre][i][1])
        else:
            answer.append(dic[genre][0][1])
        
    return answer