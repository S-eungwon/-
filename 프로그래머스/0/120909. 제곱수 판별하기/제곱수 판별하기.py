import numpy as np

def solution(n):
    n = np.sqrt(n)
    if int(n) == n:
        answer = 1
    else:
        answer = 2
    return answer