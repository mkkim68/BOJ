import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    a = str(input()[:-1])
    if a[0] == "(" and a[-1] == ")":
        if a.count("(") == a.count(")"):
            open = close = 0
            for s in a:
                if s == "(":
                    open += 1
                elif s == ")":
                    close += 1
                    if open < close:
                        print("NO")
                        break
            if open == close:
                print("YES")
        else:
            print("NO")
    else:
        print("NO")
