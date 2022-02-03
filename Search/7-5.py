# 부품 찾기 p.197
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 'yes'
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 'no'

n = int(input())
n_l = list(map(int, input().split()))
n_l.sort()

m = int(input())
m_l = list(map(int, input().split()))

for i in m_l:
    print(binary_search(n_l, i, 0, n-1), end=' ')

##############################################################################
# 계수 정렬의 개념을 이용해서 문제를 풀 수도 있다
# 모든 원소의 번호를 포함할 수 있는 크기의 리스트를 만든 뒤
# 리스트의 인덱스에 직접 접근하여 특정한 번호의 부품이 매장에 존재하는지 확인

# N(가게의 부품 개수)을 입력받기
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

# M(손님이 확인 요쳥한 부품 개수)을 입력받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))
# 손님이 확인 요쳥한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

##############################################################################
# 집합 자료형을 이용해서 문제를 해결할 수 있다
# 집합 자료형은 단순히 특정한 데이터가 존재하는지 검사할 때에 매우 효과적

# N(가게의 부품 개수)을 입력받기
n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))

# M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')