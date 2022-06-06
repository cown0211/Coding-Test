import re

def solution(s):
    answer = re.sub("one", "1", s)
    answer = re.sub("two", "2", answer)
    answer = re.sub("three", "3", answer)
    answer = re.sub("four", "4", answer)
    answer = re.sub("five", "5", answer)
    answer = re.sub("six", "6", answer)
    answer = re.sub("seven", "7", answer)
    answer = re.sub("eight", "8", answer)
    answer = re.sub("nine", "9", answer)
    answer = re.sub("zero", "0", answer)
    answer = int(answer)
    return answer
