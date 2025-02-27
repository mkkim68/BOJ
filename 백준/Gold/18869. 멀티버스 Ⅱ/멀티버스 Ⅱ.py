import sys
input = sys.stdin.readline

M, N = map(int, input().split())
planets = {}
cnt = 0
for _ in range(M):
    planet = list(map(int ,input().split()))
    temp = sorted(set(planet))

    coord_to_compressed = {value: idx for idx, value in enumerate(temp)}
    compressed = tuple([coord_to_compressed[value] for value in planet])

    if compressed in planets:
        cnt += planets[compressed]
        planets[compressed] += 1
    else:
        planets[compressed] = 1

print(cnt)