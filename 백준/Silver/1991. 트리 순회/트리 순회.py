import sys
input = sys.stdin.readline


def preorder(T):
    if T:
        print(chr(T+64), end='')
        preorder(L[T])
        preorder(R[T])

        
def inorder(T):
    if T:
        inorder(L[T])
        print(chr(T+64), end='')
        inorder(R[T])


def postorder(T):
    if T:
        postorder(L[T])
        postorder(R[T])
        print(chr(T+64), end='')

N = int(input())
L = [0] * (N+1)
R = [0] * (N+1)
for i in range(1, N+1):
    p, l, r = map(ord, input().split())
    p -= 64
    l -= 64
    r -= 64
    if l > 0:
        L[p] = l
    if r > 0:
        R[p] = r

preorder(1)
print()
inorder(1)
print()
postorder(1)