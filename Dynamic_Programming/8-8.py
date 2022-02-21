# 효율적인 화폐 구성

# 그리디에서 다루었던 거스름돈 문제와 거의 동일
# 단지 화폐 단위에서 큰 단위가 작은 단위의 배수가 아니라는 점만 다르다

# 적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수를 찾으면 됨

# 정수 n, m 입력받기
n, m = map(int, input().split())
# n개의 화폐 단위 정보를 입력받기
array = [int(input()) for _ in range(n)]

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [10001] * (m + 1)

# 다이나믹 프로그래밍 바텀업 진행
dp[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if dp[j - array[i]] != 10001:
            dp[j] = min(dp[j], dp[j - array[i]] + 1)

# 계산된 결과 출력
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])