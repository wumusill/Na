# 바닥 공사

# 정수 N을 입력받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [0] * n

# 다이나믹 프로그래밍 바텁업
dp[0] = 1
dp[1] = 3
for i in range(2, n):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 796796

# 계산된 결과 출력
print(dp[n-1])