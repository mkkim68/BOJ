import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    clothes = {}
    for i in range(n):
        name, category = input().split()
        if category not in clothes:
            clothes[category] = [name]
        else:
            clothes[category].append(name)

    cnt = 1
    for cate in clothes:
        cnt *= len(clothes[cate]) + 1

    print(cnt - 1)

