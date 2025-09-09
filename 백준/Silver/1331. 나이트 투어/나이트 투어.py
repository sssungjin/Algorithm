    
def CtoI(alpha):
    return ord(alpha) - 64

def check(x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)

coordinate = [input() for _ in range(36)]

if len(set(coordinate)) != 36:
    print("Invalid")
else:
    is_valid_tour = True
    
    for i in range(35):
        cur_pos_str = coordinate[i]
        next_pos_str = coordinate[i + 1]
        
        cur_x, cur_y = CtoI(cur_pos_str[0]), int(cur_pos_str[1])
        next_x, next_y = CtoI(next_pos_str[0]), int(next_pos_str[1])
        
        if not check(cur_x, cur_y, next_x, next_y):
            is_valid_tour = False
            break
    
    if is_valid_tour:
        last_pos_str = coordinate[35]
        first_pos_str = coordinate[0]
        
        last_x, last_y = CtoI(last_pos_str[0]), int(last_pos_str[1])
        first_x, first_y = CtoI(first_pos_str[0]), int(first_pos_str[1])
        
        if check(last_x, last_y, first_x, first_y):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
    
        
