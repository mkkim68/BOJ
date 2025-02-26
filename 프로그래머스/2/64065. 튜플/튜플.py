def solution(s):
    answer = []
    start = s.replace("{", "").replace("}","").split(",")
    nums = {}
    for n in start:
        if int(n) not in nums:
            nums[int(n)] = 1
            answer.append(int(n))
        else:
            nums[int(n)] += 1
    answer.sort(key=lambda x: -nums[x])
    return answer