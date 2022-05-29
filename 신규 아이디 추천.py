import re

def solution(new_id):
    
    # 1단계 대문자->소문자
    answer = new_id.lower()
    
    # 2단계 a-z, 0-9, -_. 제외한 나머지 삭제
    answer = re.sub("[^a-z0-9\-_.]", "", answer)

    # 3단계 .이 2개 이상일 경우 . 한개로 대체
    answer = re.sub("\.+", ".", answer)
    
    # 4단계 문자열 양 옆의 . 제거
    answer = answer.strip(".")
    
    # 5단계 빈 문자열일 경우 "a"로 대체
    if not answer: answer = "a"
    
    # 6단계 길이가 16 이상이면 15번까지, .으로 끝나면 . 제거
    if len(answer) >= 16:
        answer = answer[:15].rstrip(".")
    
    # 7단계 길이가 2 이하라면 3이 될 때까지 마지막 문자 끝에 반복해서 붙임
    if len(answer) <= 2:
        while len(answer) <= 2:
            answer = answer + answer[-1]
    
    
    return answer
  
  
  
  '''
  참고
  https://wikidocs.net/4308
  https://ponyozzang.tistory.com/335
  https://stcodelab.com/m/22
  https://rk1993.tistory.com/entry/Python%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%96%91-%EB%81%9D-%EA%B3%B5%EB%B0%B1-%EB%98%90%EB%8A%94-%EB%AC%B8%EC%9E%90-%EC%A0%9C%EA%B1%B0-striplstriprstrip
  https://appia.tistory.com/417
  
  다른 사람 풀이
  https://programmers.co.kr/learn/courses/30/lessons/72410/solution_groups?language=python3
  '''
