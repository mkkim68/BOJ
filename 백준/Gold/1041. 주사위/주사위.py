import sys
input = sys.stdin.readline

N = int(input())
dice = list(map(int, input().split()))
A, B, C, D, E, F = dice

min_num, max_num = min(dice), max(dice)
if N <= 1:
    print(sum(dice) - max_num)
else:
    min_three = min(A+B+C, A+E+C, A+E+D, A+B+D, C+E+F, C+B+F, F+B+D, F+E+D)
    min_two = min(A+B, A+C, A+D, A+E, F+B, F+C, F+D, F+E, C+E, E+D, D+B, B+C)
    if N == 2:
        print((min_two + min_three) * 4)
    else:
        ans = min_three * 4 + min_two * (8 * (N-2) + 4) + min_num * (5 * (N-2) ** 2 + 4 * (N-2))
        print(ans)

