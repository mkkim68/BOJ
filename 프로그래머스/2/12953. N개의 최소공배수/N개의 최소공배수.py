import math

def solution(arr):
    answer = arr[0]
    
    for i in range(1, len(arr)):
        gcd = math.gcd(answer, arr[i])
        
        answer = (answer * arr[i]) // gcd
    
    return answer