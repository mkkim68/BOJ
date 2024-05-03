def solution(edges):
    new_node, stick, eight = 0, 0, 0
    
    nodes = {} # go, come
    for s, e in edges:
        if s not in nodes:
            nodes[s] = [1, 0]
        else:
            nodes[s][0] += 1
        if e not in nodes:
            nodes[e] = [0, 1]
        else:
            nodes[e][1] += 1
    
    # print(nodes)
    for key in nodes:
        go, come = nodes[key]
        if come == 0 and go >= 2:
            new_node = key
        elif go >= 2:
            eight += 1
        elif go == 0:
            stick += 1
            
    answer = [new_node, nodes[new_node][0]-stick-eight, stick, eight]
    return answer