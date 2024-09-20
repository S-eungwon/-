def solution(array):
    answer = []
    answer.append(sorted(array)[-1])
    for index,num in enumerate(array):
        if num == answer[0]:
            answer.append(index)
            break
    return answer