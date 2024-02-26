import sys
input = sys.stdin.readline

def max_enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p >= 1 and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


def max_deq():
    if not heap[1]:
        return 0
    else:
        global last
        tmp = heap[1]
        heap[1] = heap[last]
        heap[last] = 0
        last -= 1
        p = 1
        c = p * 2
        while c <= last:
            if c+1 <= last and heap[c] < heap[c+1]:
                c += 1
            if heap[p] < heap[c]:
                heap[p], heap[c] = heap[c], heap[p]
                p = c
                c = p * 2
            else:
                break
        return tmp


N = int(input())
heap = [0] * (N+1)
last = 0
for _ in range(N):
    x = int(input())
    if x == 0:
        print(max_deq())
    else:
        max_enq(x)


