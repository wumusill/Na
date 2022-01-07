col = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

loc_x, loc_y = list(input())
case = 0

move_l = [(2, 1), (2, -1), (-2, 1), (-2, -1), (-1, 2), (1, 2), (-1, -2), (1, -2)]
for x, y in move_l:
    temp_x = col[loc_x] + x
    temp_y = int(loc_y) + y
    if temp_y > 8 or temp_y < 1:
        continue
    elif temp_x < 1 or temp_x > 8:
        continue
    case += 1

print(case)