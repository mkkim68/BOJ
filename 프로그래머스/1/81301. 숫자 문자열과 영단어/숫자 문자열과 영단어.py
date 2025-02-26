def solution(s):
    answer = s
    nums ={
        'zero':'0',
        'one':'1', 
        'two':'2', 
        'three':'3', 
        'four':'4', 
        'five':'5', 
        'six':'6', 
        'seven':'7', 
        'eight':'8', 
        'nine':'9'
    }
    for n in nums:
        a = answer.split(n)
        temp = ''
        if len(a) == 1:
            continue
        else:
            for i in range(len(a)):
                temp += a[i]
                if i < len(a)-1:
                    temp += nums[n]
        answer = temp
    return int(answer)