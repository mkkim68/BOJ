import sys
input = sys.stdin.readline

N = int(input())
switch = list(map(int, input().split()))
S = int(input())
for s in range(1, S+1):
    sex, num = map(int, input().split())
    # 남:1 여:2
    if sex == 1:
        for i in range(len(switch)):
            if (i + 1) % num == 0:
                switch[i] = 0 if switch[i] == 1 else 1
    else:
        new_switch = []
        for i in range(0, num+1):
            temp = []
            if num-i-1 >= 0 and num+i <= len(switch) and switch[num-i - 1:num+i] == switch[num-i-1:num+i][::-1]:
                for sw in switch[num-i-1:num+i]:
                    temp.append(0 if sw == 1 else 1)
                new_switch = temp
            else:
                switch[num - i:num + i-1] = new_switch
                break

if len(switch) <= 20:
    print(*switch, sep=' ', end='')
else:
    for i in range(len(switch)):
        if (i + 1) % 20 == 0 and i != len(switch) - 1:
            print(switch[i], end='\n')
        elif (i + 1) % 20 == 0 or i == len(switch) - 1:
            print(switch[i], end='')
        else:
            print(switch[i], end=' ')

