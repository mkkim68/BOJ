import sys
input = sys.stdin.readline


def find_next_top(dice_num, prev_top):
    cur_dice = dices[dice_num]
    for key in cur_dice:
        btm_num = cur_dice[key]
        if btm_num == prev_top:
            if key == 'A':
                top_num = cur_dice['F']
                top_key = 'F'
            elif key == 'B':
                top_num = cur_dice['D']
                top_key = 'D'
            elif key == 'C':
                top_num = cur_dice['E']
                top_key = 'E'
            elif key == 'D':
                top_num = cur_dice['B']
                top_key = 'B'
            elif key == 'E':
                top_num = cur_dice['C']
                top_key = 'C'
            elif key == 'F':
                top_num = cur_dice['A']
                top_key = 'A'
            return top_num, key, top_key



def find_max(idx, btm_key, top_key):
    cur = dices[idx]
    max_num = 0
    for k in cur:
        if k != btm_key and k != top_key:
            if cur[k] > max_num:
                max_num = cur[k]
    return max_num


N = int(input())
dices = {}
for i in range(1, N+1):
    # A - F 순서대로 입력
    dice = {}
    temp = list(map(int, input().split()))
    for j in range(6):
        dice[chr(j+65)] = temp[j]
    dices[i] = dice

# A, F / B, D/ C, E
# 1번 주사위 맨 위가 A - F인 경우(6가지)
answer = []
first_dice = dices[1]
for key in first_dice:  # 맨 아래 주사위 기준
    btm_num = first_dice[key]
    cnt = 0
    if key == 'A':
        top_num = first_dice['F']
        top_key = 'F'
    elif key == 'B':
        top_num = first_dice['D']
        top_key = 'D'
    elif key == 'C':
        top_num = first_dice['E']
        top_key = 'E'
    elif key == 'D':
        top_num = first_dice['B']
        top_key = 'B'
    elif key == 'E':
        top_num = first_dice['C']
        top_key = 'C'
    elif key == 'F':
        top_num = first_dice['A']
        top_key = 'A'
    max_num = find_max(1, key, top_key)
    cnt += max_num
    dice_idx = 2
    while dice_idx <= N:
        top_num, btm, top = find_next_top(dice_idx, top_num)  # 각 주사위 top, btm키, top키
        new_max = find_max(dice_idx, btm, top)
        cnt += new_max
        dice_idx += 1
    answer.append(cnt)

print(max(answer))