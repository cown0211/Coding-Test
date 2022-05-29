def solution(id_list, report, k):
    
    # report에서 중복값 제거, 같은 사람이 같은 사람 신고하면 카운트 안함
    new_report = list(set(report))
    
    # rpt:신고자, rpted:불량이용자
    rpt,rpted = [],[]
    for i in range(0, len(new_report)):
        rpt.append(new_report[i].split(" ")[0])
        rpted.append(new_report[i].split(" ")[1])
    
    # id_list 기준, 신고당한 횟수 카운트
    cnt = []
    for i in id_list:
        cnt.append(rpted.count(i))
    
    # id_list 기준, 정지 당한 횟수
    n = []
    for i in range(0, len(cnt)):
        tmp = 0
        if cnt[i] >= k:
            tmp += 1
            n.append(tmp)
        else:
            n.append(0)
            
    # 정지당한 사람
    stp = []
    for i in range(0, len(n)):
        if n[i] >= 1: stp.append(id_list[i])

    # 정지 당한 사람의 인덱스
    idx = [i for i, x in enumerate(rpted) if x in stp]
    
    # 메일을 받아볼 사람
    mail = []
    for i in range(0, len(idx)):
        mail.append(rpt[idx[i]])
    
    # id_list 기준으로 받아볼 메일의 개수
    answer = []
    for i in id_list:
        answer.append(mail.count(i))
        
    return answer

'''
참고
https://blockdmask.tistory.com/469
https://velog.io/@daybreak/Python%EC%97%90%EC%84%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A4%91%EB%B3%B5%EC%A0%9C%EA%B1%B0
https://www.delftstack.com/ko/howto/python/find-all-indices-of-element-in-list-python/

다른 사람 풀이
https://programmers.co.kr/learn/courses/30/lessons/92334/solution_groups?language=python3
'''
