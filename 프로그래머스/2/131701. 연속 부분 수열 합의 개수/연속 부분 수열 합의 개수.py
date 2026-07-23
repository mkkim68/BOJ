def solution(elements):
    answer = 0
    num_set = set()
    n = len(elements)
    num_set.add(sum(elements))
    elements = elements + elements

    prefix_sum = [0]
    for i in range(2*n):
        prefix_sum.append(prefix_sum[i]+elements[i])
    
    for length in range(1, n):
        for start in range(n):
            subsum = prefix_sum[length+start] - prefix_sum[start]
            num_set.add(subsum)
    
    return len(num_set)