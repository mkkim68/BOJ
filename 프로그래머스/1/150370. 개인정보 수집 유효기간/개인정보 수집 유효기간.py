def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split(".")))
    
    term_dict = dict()
    for i in range(len(terms)):
        term = terms[i].split()
        term[1] = int(term[1])
        term_dict[term[0]] = int(term[1])
    
    for i in range(len(privacies)):
        privacy = privacies[i].split()
        year, month, day = map(int, privacy[0].split("."))
        term = privacy[1]
        
        new_month = month + term_dict[term]
        new_year = year + new_month // 12
        new_month %= 12
        
        if new_month == 0:
            new_month = 12
            new_year -= 1
            
        if new_year > today[0]:
            continue
        elif new_year < today[0]:
            answer.append(i+1)
        else:
            if new_month > today[1]:
                continue
            elif new_month < today[1]:
                answer.append(i+1)
            else:
                if day <= today[2]:
                    answer.append(i+1)
            
    return answer