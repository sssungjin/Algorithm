from itertools import permutations

n = int(input())

permu = list(permutations(range(1,n+1), n))

for i in permu:
    #print(i)
    for j in range(len(i)):
        if j != len(i) - 1:
            print(i[j], end=" ")
        else:
            print(i[j], end="\n")
