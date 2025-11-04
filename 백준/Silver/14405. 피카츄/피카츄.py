import sys
input = sys.stdin.readline

S = input().strip().split("pi")
for st in S:
    temp = st.split("ka")
    for t in temp:
        ntemp = t.split("chu")
        for n in ntemp:
            if n:
                print("NO")
                exit()

print("YES")