import numpy as np
import time

def Q5(Arr : list[int]):
    result = np.zeros((len(Arr), len(Arr)), dtype=float)
    for i in range(len(Arr)):
        for j in range(i, len(Arr)):
            result[i][j] = sum(Arr[i : j+1]) / (j+1 - i)
    return result

def Q6(A: list[int]):
    if len(A) < 1:
        print("Input array should not be empty")
        return None
    # below array will store sumulative sum of elements 
    # of A from index 0 upto i.
    cumsum = np.zeros(len(A), dtype=float)
    cumsum[0] = A[0] 
    for i in range(1, len(A)):
        cumsum[i] = cumsum[i - 1] + A[i]
    result = np.zeros((len(A), len(A)), dtype=float)
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            result[i][j] = cumsum[j] / (j+1 - i) # average
        cumsum -= cumsum[i]

    return result

if __name__ == "__main__":
    test_list = list(range(1, 5))
    start = time.time()
    # Testing Q6 algorithm
    res6 = Q6(test_list)
    print(res6)
    end_6 = time.time()
    print(f"Q6 Algorithm took %.3f seconds" %(end_6 - start))
    # Testing Q5 algorithm
    res5 = Q5(test_list)    
    print(res5)
    end_5 = time.time()
    print(f"Q5 Algorithm took %.3f seconds" %(end_5 - end_6))
    try:
        print("%.2f times faster" %((end_5 - end_6) / (end_6 - start)))
    except ZeroDivisionError:
        print("same performance")
    
    
    