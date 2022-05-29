def solution(lottos, win_nums):
    
    '''
    로또 l과 당첨 w의 교집합 계산
    
    6개라면 최소등수=최대등수=1
    
    그 외라면
    최소등수=교집합 원소수; 최대등수=교집합 원소수+lottos에서 0의 개수(0이 다 맞았다는 가정)
    '''
    
        
    
    lo_set = set(lottos)
    win_set = set(win_nums)
    # 리스트를 set로 변환
    
    
    lo_inter = lo_set & win_set
    # lottos와 win_nums의 교집합
    inter_cnt = len(lo_inter)
    # 교집합의 원소수 = 최소 당첨 내용
    
    
    max_cnt = inter_cnt + lottos.count(0)
    # 최대 당첨 내용
    
    
    
    min_rank, max_rank = 0, 0
    
    # 최소 등수 반환
    if inter_cnt == 6:
        min_rank = 1
    elif inter_cnt == 5:
        min_rank = 2
    elif inter_cnt == 4:
        min_rank = 3
    elif inter_cnt == 3:
        min_rank = 4
    elif inter_cnt == 2:
        min_rank = 5
    else:
        min_rank = 6
    
    
    # 최대 등수 반환
    if max_cnt == 6:
        max_rank = 1
    elif max_cnt == 5:
        max_rank = 2
    elif max_cnt == 4:
        max_rank = 3
    elif max_cnt == 3:
        max_rank = 4
    elif max_cnt == 2:
        max_rank = 5
    else: max_rank = 6
        
        
    answer = [max_rank, min_rank]

    
    return answer
    
    
    
'''
다른 사람 풀이
https://programmers.co.kr/learn/courses/30/lessons/77484/solution_groups?language=python3
'''
