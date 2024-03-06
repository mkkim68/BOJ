import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
# 1번 칸(0): 올리는 위치, N번 칸(N-1): 내리는 위치
belt = deque(map(int, input().split()))
robots = deque([0] * 2*N)

level = 1
while True:
    upidx, downidx = 0, N-1
    # 1. 회전
    belt.rotate(1)
    robots.rotate(1)
    # 내리기
    if robots[downidx] == 1:
        robots[downidx] = 0
    # 2. 한 칸 이동
    for idx in range(2*N-1, -1, -1):
        if idx == 2*N-1:
            idx = -1
        if robots[idx] == 1 and robots[idx+1] == 0 and belt[idx+1] > 0:
            robots[idx], robots[idx+1] = 0, 1
            if idx+1 == downidx:
                robots[idx+1] = 0
            belt[idx+1] -= 1
    # 3. 로봇 올리기
    if robots[upidx] == 0 and belt[upidx] > 0:
        robots[upidx] = 1
        belt[upidx] -= 1
    # 4. 내구도 검사
    if belt.count(0) >= K:
        break
    level += 1

print(level)