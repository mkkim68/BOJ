import sys
input = sys.stdin.readline

L = int(input())
string = input()[:-1]

index = [i for i in range(1, 27)]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha_dict = {alphabet[i]:index[i] for i in range(26)}

ans = 0
for s in range(len(string)):
    ans += alpha_dict[string[s]] * 31 ** s

if ans // 1234567891 > 0:
    ans %= 1234567891

print(ans)