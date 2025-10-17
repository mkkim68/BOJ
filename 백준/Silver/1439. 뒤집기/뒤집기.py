import sys
input = sys.stdin.readline

S = input().strip()
temp1, temp2 = S.split("1"), S.split("0")

arr1, arr2 = [], []
for temp in temp1:
    if temp:
        arr1.append(temp)

for temp in temp2:
    if temp:
        arr2.append(temp)

print(min(len(arr1), len(arr2)))