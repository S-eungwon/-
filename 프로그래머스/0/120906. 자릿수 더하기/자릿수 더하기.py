def solution(n):
    n_str = str(n)
    answer = 0
    for i in range(len(n_str)):
        answer += int(n_str[i])
    return answer