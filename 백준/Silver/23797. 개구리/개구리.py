import sys
input = sys.stdin.readline

s = input().strip()

waiting_for_k = 0
waiting_for_p = 0

total_frogs = 0

for char in s:
    if char == 'K':
        if waiting_for_k > 0:
            waiting_for_k -= 1
            waiting_for_p += 1
        else:
            total_frogs += 1
            waiting_for_p += 1
    else:  # char == 'P'
        if waiting_for_p > 0:
            waiting_for_p -= 1
            waiting_for_k += 1
        else:
            total_frogs += 1
            waiting_for_k += 1

print(total_frogs)
