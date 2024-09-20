def solution(s1, s2):
    answer = len([string for string in s1 if (string in s2)])
    return answer