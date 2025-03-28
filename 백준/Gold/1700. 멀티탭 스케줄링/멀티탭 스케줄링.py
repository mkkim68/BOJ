import sys
input = sys.stdin.readline

N, K = map(int, input().split())
devices = list(map(int, input().split()))
multi = [0] * N
cnt = 0
for i in range(K):
    if devices[i] in multi:
        continue
    else:
        for j in range(N):
            if multi[j] == 0:
                multi[j] = devices[i]
                break
        else:
            idx, first = -1, -1
            for j in range(N):
                try:
                    tidx = devices[i+1:].index(multi[j])
                except:
                    tidx = 1000
                if first < tidx:
                    idx = j
                    first = tidx
            multi[idx] = devices[i]
            cnt += 1

print(cnt)
