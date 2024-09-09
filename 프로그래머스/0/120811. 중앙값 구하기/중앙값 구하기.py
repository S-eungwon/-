def solution(array):
    array.sort()
    index = (len(array)-1)/2
    answer = array[int(index)]
    return answer