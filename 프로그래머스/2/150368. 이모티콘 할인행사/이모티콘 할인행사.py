
max_m, max_g = 0, 0
def solution(users, emoticons):
    answer = []
    n, m = len(users), len(emoticons)
    discounts = [10, 20, 30, 40]
    
    # user_arr = [플러스 가입 여부(T/F), 구매 비용]
    def sol(idx, user_arr):
        global max_m, max_g
        if idx == m:
            members, gain = 0, 0
            for ismem, cost in user_arr:
                if ismem:
                    members += 1
                gain += cost
                
            if max_m < members:
                max_m = members
                max_g = gain
            elif max_m == members and max_g < gain:
                max_g = gain
                
            return
        
        for discount in discounts:
            dis_price = emoticons[idx] * (100 - discount) / 100
            new_arr = []
            for i in range(n):
                is_mem, price = user_arr[i]
                perc, limit = users[i]
                new_arr.append(user_arr[i])
                if not is_mem and discount >= perc:
                    new_price = price + dis_price
                    if new_price >= limit:
                        new_arr[i] = [True, 0]
                    else:
                        new_arr[i] = [False, new_price]
            sol(idx+1, new_arr)
            
    sol(0, [[False, 0] for _ in range(n)])
    return [max_m, max_g]