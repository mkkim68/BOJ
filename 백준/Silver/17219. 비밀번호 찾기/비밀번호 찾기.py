import sys
input = sys.stdin.readline

N, M = map(int, input().split())
info = {}
for _ in range(N):
    site, password = input().split()
    info[site] = password

for _ in range(M):
    site = input().strip()
    print(info[site])