import sys

def dfs_stack(graph, start):
    visited = set()  # 방문한 노드를 저장할 집합
    stack = [start]  # 탐색 시작 노드를 스택에 추가

    while stack:
        vertex = stack.pop()  # 스택의 가장 위에 있는 노드를 꺼낸다
        if vertex not in visited:
            print(vertex, end=' ')  # 방문한 노드를 출력
            visited.add(vertex)  # 방문 처리

            # 인접 노드를 스택에 추가한다.
            # reversed를 사용하는 이유: 스택인 LIFO이기 때문에,
            # 그래프에 정의된 순서를 그대로 따라가려면 역순으로 넣어야 한다.
            stack.extend(reversed(graph[vertex]))


def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# 예시 그래프 (인접 리스트)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS:")
dfs_stack(graph, 'A')
