def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher)-len(cipher)%code, code):
        answer += cipher[i]
    return answer