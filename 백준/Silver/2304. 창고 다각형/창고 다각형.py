import sys
input = sys.stdin.readline

N = int(input())
sticks = []
for _ in range(N):
    L, H = map(int, input().split())
    sticks.append([L, H])

sticks.sort(key=lambda x: x[0])

max_i = max_h = 0
for stick in sticks:
    if max_h < stick[1]:
        max_i, max_h = sticks.index(stick), stick[1]


max_s = 0
cansee1 = []
cansee_x = []
for i in range(N-1, max_i, -1):
    if i == N-1:
        cansee1.append(sticks[i][1])
        cansee_x.append(sticks[i][0]-sticks[i-1][0])
        max_s = sticks[i][1]
    elif sticks[i][1] <= max_s:
        cansee_x[-1] += (sticks[i][0]-sticks[i-1][0])
    elif sticks[i][1] > max_s:
        max_s = sticks[i][1]
        cansee1.append(sticks[i][1])
        cansee_x.append(sticks[i][0] - sticks[i - 1][0])

max_s = 0
cansee2 = []
cansee2_x = []
for i in range(max_i):
    if i == 0:
        cansee2.append(sticks[i][1])
        cansee2_x.append(sticks[i+1][0]-sticks[i][0])
        max_s = sticks[i][1]
    elif sticks[i][1] <= max_s:
        cansee2_x[-1] += (sticks[i+1][0]-sticks[i][0])
    elif sticks[i][1] > max_s:
        max_s = sticks[i][1]
        cansee2.append(sticks[i][1])
        cansee2_x.append(sticks[i+1][0] - sticks[i][0])

area = 0
for i in range(len(cansee1)):
    area += cansee1[i] * cansee_x[i]

for i in range(len(cansee2)):
    area += cansee2[i] * cansee2_x[i]


area += max_h
print(area)