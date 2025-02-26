import sys
input = sys.stdin.readline

N = int(input())
students = list(map(int, input().split()))
students.sort()
M = len(students)
ans = 1e9
for i in range(M//2):
    a, b = students[i], students[M-1-i]
    ans = min(a + b, ans)

print(ans)