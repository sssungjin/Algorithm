import numpy as np
def solution(arr1, arr2):
    answer = np.array(arr1) + np.array(arr2)
    li = answer.tolist()
    return li