def solution(numbers):
    answer = []
    # levels = [1]
    # prev = 1
    # for i in range(1, 50):
    #     prev += 2**i
    #     levels.append(prev)
    # print(levels)
    # print(len(bin(10**15)))
    
    def find_level(num):
        lv, cnt = 0, 0
        while cnt < num:
            cnt += 2 ** lv
            lv += 1
        # for i in range(50):
        #     pass
        return [lv, cnt-num]
    
    # 루트가 1인지 체크
    # 1이면 자식 노드 체크 없이 서브노드로 재귀
    # 0이면 자식 노드가 있는지 체크
    # ㄴ없으면 false, 있으면 true 리턴
    def check(bin_num, level):
        length = len(bin_num)
        have_root = bin_num[length//2]
        if level >= 2:
            if have_root == '1':
                return min(check(bin_num[length//2+1:], level-1), check(bin_num[:length//2], level-1))
            else:
                if '1' in bin_num[:length//2]:
                    return 0
                if '1' in bin_num[length//2+1:]:
                    return 0
                return 1
        else:
            return 1
                
    for number in numbers:
        bin_num = bin(number)[2:]
        # 트리 레벨 찾기
        lv, cnt = find_level(len(bin_num))  # 트리 레벨, 나머지
        bin_num = "0"*cnt + bin_num
        # 이진 트리 가능 여부
        is_possible = check(bin_num, lv)
        answer.append(is_possible)
        
    return answer