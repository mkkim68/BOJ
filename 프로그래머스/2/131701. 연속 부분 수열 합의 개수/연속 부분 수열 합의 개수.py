def solution(elements):
    answer = 0
    num_set = set()
    n = len(elements)
    num_set.add(sum(elements))
    elements = elements + elements

    prefix_sum = [0]
    for i in range(2*n):
        prefix_sum.append(prefix_sum[i]+elements[i])
    
    for i in range(1, n+1):
        for j in range(i, 2*n+1):
            now = prefix_sum[j] - prefix_sum[j-i]
            num_set.add(now)
    
    return len(num_set)