import sys

input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())

numR = R
numC = C - 1
flag = 1  # 1: 증가, 0: 감소
ansC, ansR = 1, 0
cntR = 0
cntC = 1
while K > 0:
    if K > C * R:
        print(0)
        break
    if K <= numR:
        if flag == 1:
            ansR += K
        else:
            ansR -= K
        print(ansC, ansR)
        break
    elif numR < K <= numR + numC:
        if flag == 1:
            ansR = R - cntR
            ansC += K - numR
        else:
            ansR = cntR
            ansC -= (K - numR)
        print(ansC, ansR)
        break
    K -= (numR + numC)
    numR -= 1
    numC -= 1
    if flag == 1:
        flag = 0
        ansR = R - cntR
        ansC = C - cntC + 1
        cntR += 1
        cntC += 1
    else:
        flag = 1
        ansR = cntR
        ansC = cntC
