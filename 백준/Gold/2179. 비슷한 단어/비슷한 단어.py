import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
nums = [i for i in range(N)]

def combi(idx, arr):
    global ans1, ans2, cnt

    if len(arr) == 2:
        i1, i2 = arr
        word1, word2 = words[i1], words[i2]
        M = min(len(word1), len(word2))
        for i in range(M):
            if word1[i] != word2[i]:
                if i > cnt:
                    cnt = i
                    ans1, ans2 = i1, i2
                break
        else:
            if cnt < M:
                cnt = M
                ans1, ans2 = i1, i2
        return

    for i in range(idx, N):
        if not visited[i]:
            if len(arr) == 0 or (len(arr) == 1 and words[i][0] == words[arr[0]][0]):
                visited[i] = 1
                combi(i+1, arr+[i])
                visited[i] = 0



ans1, ans2 = -1, -1
cnt = -1
visited = [0] * N

combi(0, [])
print(words[ans1])
print(words[ans2])