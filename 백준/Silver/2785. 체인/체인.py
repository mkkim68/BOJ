import sys
input = sys.stdin.readline

N = int(input())
chains = list(map(int, input().split()))
chains.sort()
cnt = 0
for chain in chains:
    if chain == N-1:
        print(cnt + chain)
        break
    elif chain > N-1:
        print(cnt + N-1)
        break
    else:
        N -= chain + 1
        cnt += chain

