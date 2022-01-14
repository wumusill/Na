# 퀵 정렬은 기준을 설정한 다음 큰 수와 작은 수를 교환한 후, 리스트를 반으로 나누는 방식
# 교환하기 위한 '기준'을 바로 피벗이라고 표현
# 퀵 정렬을 수행하기 전 피벗을 어떻게 설정할 것인지 미리 설정해야 함
# 피벗을 설정하고 리스트를 분할하는 방식에 따라 여러 가지 방식으로 구분
# 가장 대표적인 분할 방식인 호어 분할(Hoare Partition)
# 호어 분할에서는 리스트의 첫 번째 데이터를 피벗으로 정함

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:    # 원소가 1개인 경우 종료
        return
    pivot = start       # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:    # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:               # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)


# 파이썬의 장점을 살린 퀵 정렬
# 위의 퀵 정렬의 분할 방식과는 조금 다름
# 피벗과 데이터를 비교하는 비교 연산 횟수가 증가하므로 시간 면에서는 조금 비효율적
# 하지만 더 직관적이고 기억하기 쉬움

def quick_sort_2(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]    # 피벗은 첫 번째 원소
    tail = array[1:]    # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]     # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]     # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort_2(left_side) + [pivot] + quick_sort_2(right_side)

print(quick_sort_2(array))

# 퀵 정렬의 시간 복잡도 : 평균적으로 O(NlogN)
# 최악의 경우 : O(N^2)
# 데이터가 무작위로 입력되는 경우 빠르게 동작할 확률이 높음
# 가장 왼쪽 데이터를 피벗으로 삼을 때
# 이미 데이터가 정렬되어 있는 경우에는 매우 느리게 작동
