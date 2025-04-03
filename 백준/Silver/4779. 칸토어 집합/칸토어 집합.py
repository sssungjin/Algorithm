def canto(size, start):
    if size == 1:
        return
    length = size // 3
    
    for i in range(start + length, start + length * 2):
        result[i] = ' '
    
    canto(length, start)
    canto(length, start + length * 2)

while True:
    try:
        N = int(input())
        result = ['-'] * (3 ** N)
        canto(3 ** N, 0)
        print(''.join(result))
    except EOFError:
        break
    except ValueError:
        break
