def solution(n, words):
    answer = [0, 0]
    last = words[0][-1]
    words_set = set()
    words_set.add(words[0])
    
    for i in range(1, len(words)):
        word = words[i]
        if word[0] != last or word in words_set:
            idx = (i+1) % n
            if idx == 0:
                answer[0] = n
                answer[1] = (i+1)//n
            else:
                answer[0] = idx
                answer[1] = (i+1)//n+1
            break
        words_set.add(word)
        last = word[-1]
    
    return answer