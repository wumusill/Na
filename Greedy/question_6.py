# 무지의 먹방 라이브
def solution(food_times, k):
    second = 0
    table = 0
    num_table = len(food_times)
    while True:
        if food_times.count(0) == num_table:
            return -1


        if k == second:
            table += 1
            break

        if table == num_table:
            table = 0

        if food_times[table] == 0:
            table += 1
        else:
            food_times[table] -= 1
            second += 1
            table += 1

    if table > num_table:
        return table - num_table
    else:
        return table


print(solution([3, 1, 2], 4))
