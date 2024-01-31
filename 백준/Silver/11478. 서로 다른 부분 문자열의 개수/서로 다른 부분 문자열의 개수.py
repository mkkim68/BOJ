import sys
input = sys.stdin.readline

str = str(input())
ans = set()

for i in range(len(str)):
    for j in range(1, len(str)+1):
        if '\n' not in str[i:j]:
            ans.add(str[i:j])

print(len(ans)-1)
