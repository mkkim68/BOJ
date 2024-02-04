import sys
input = sys.stdin.readline

W, H = map(int, input().split())
N = int(input())
stores = []
total = 2 * (W + H)
for _ in range(N):
    store = tuple(map(int, input().split()))
    stores.append(store)
    # 방향 (1: 북, 2: 남, 3: 서, 4: 동)
    # 북/남 - 왼쪽 경계로부터 거리, 동/서 - 위쪽 경계로부터 거리
dong = tuple(map(int, input().split()))
distance = 0
for dir, dis in stores:
    if dong[0] == dir:  # 같은 방향에 있을 때
        distance += abs(dong[1] - dis)
    elif dong[0] == 2:  # 다른 방향 & 동근이가 남쪽
        if dir == 3:
            distance += dong[1] + H - dis
        elif dir == 4:
            distance += W - dong[1] + H - dis
        else:
            clk = dong[1] + H + dis
            ctnclk = total - clk
            if clk > ctnclk:
                distance += ctnclk
            else:
                distance += clk
    elif dong[0] == 3:  # 다른 방향 & 동근이가 서쪽
        if dir == 1:
            distance += dong[1] + dis
        elif dir == 2:
            distance += H - dong[1] + dis
        else:
            clk = dong[1] + W + dis
            ctnclk = total - clk
            if clk > ctnclk:
                distance += ctnclk
            else:
                distance += clk
    elif dong[0] == 1:  # 다른 방향 & 동근이가 북쪽
        if dir == 3:
            distance += dong[1] + dis
        elif dir == 4:
            distance += W - dong[1] + dis
        else:
            clk = 2 * W - dong[1] + H - dis
            ctnclk = total - clk
            if clk > ctnclk:
                distance += ctnclk
            else:
                distance += clk
    elif dong[0] == 4:  # 다른 방향 & 동근이가 동쪽
        if dir == 1:
            distance += dong[1] + W - dis
        elif dir == 2:
            distance += H - dong[1] + W - dis
        else:
            clk = 2 * H - dong[1] + W - dis
            ctnclk = total - clk
            if clk > ctnclk:
                distance += ctnclk
            else:
                distance += clk

print(distance)
