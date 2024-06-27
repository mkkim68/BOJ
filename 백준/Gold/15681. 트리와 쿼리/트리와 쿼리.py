import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def tree(currentNode, parent):
    for node in edges[currentNode]:
        if node != parent:
            tree(node, currentNode)
            size[currentNode] += size[node]


N, R, Q = map(int, input().split())  # 정점의 수, 루트 번호, 쿼리 수
edges = {i: [] for i in range(1, N+1)}
for _ in range(N-1):
    U, V = map(int, input().split())
    edges[U].append(V)
    edges[V].append(U)

size = [1] * (N + 1)
tree(R, -1)

for _ in range(Q):
    q = int(input())
    print(size[q])