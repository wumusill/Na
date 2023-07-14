# 위상정렬
# 순서가 정해져 있는 작업을 차례로 수행해야 할 때 그 순서를 결정해주기 위해 사용하는 알고리즘
# 위상 정렬은 여러 개의 답이 존재할  수 있음
# DAG(Directed Acyclic Graph)에만 적용 가능 : 사이클이 발생하지 않는 방향 그래프
# 사이클이 발생하는 경우 위상 정렬 불가능
# 큐와 스택 두 가지를 활용하여 구현 가능

# 진입 차수 : 특정 노드로 들어가는 간선의 개수
# 진출 차수 : 특정 노드에서 나가는 간선의 개수

# 1. 진입 차수가 0인 정점을 큐에 삽입
# 2. 큐에서 원소를 꺼내 연결된 모든 간선을 제거
# 3. 간선 제거 이후 진입 차수가 0이 된 정점을 큐에 삽입
# 4. 큐가 빌 때까지 2 ~ 3번 과정을 반복

# 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재하는 것
# 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상 정렬의 결과

from collections import deque

# 노드와 간선의 개수 입력
v, e = map(int, input().split())

# 모든 노드에 대한 진입 차수 기록, 0으로 초기화
indegree = [0] * (v + 1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    # a에서 b로 이동 가능
    graph[a].append(b)
    # 진입 차수 기록
    indegree[b] += 1


# 위상 정렬 함수
def topology_sort():
    # 위상 정렬 결과물을 기록할 리스트
    result = []
    q = deque()
    # 처음 시작할 때 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내서 기록
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 모든 간선 제거
        # 연결된 노드들의 진입 차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 진입 차수가 0인 새로운 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬 결과물 출력
    for i in result:
        print(i, end=' ')


topology_sort()