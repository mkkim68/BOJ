import sys
input = sys.stdin.readline


def delete(s):
    child = arr[s]
    if not child:
        arr[s] = -1
    else:
        for c in child:
            delete(c)
            arr[s] = -1


N = int(input())
par = list(map(int, input().split()))
del_node = int(input())

# print(par)
arr = [[] for _ in range(N)]
for i in range(N):
    p = par[i]
    if p >= 0:
        arr[p].append(i)
        if i == del_node:
            arr[p].remove(i)

delete(del_node)
# print(arr)
print(arr.count([]))