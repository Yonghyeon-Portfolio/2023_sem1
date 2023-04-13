import numpy as np
import time

def Q5(Arr : list[int]):
    result = []
    for i in range(len(Arr)):
        row = []
        for j in range(i, len(Arr)):
            row.append(sum(Arr[i:j+1])/(j-i+1))
        result.append(row)
    return result

def Q6(A: list[int]):
    if len(A) < 1:
        print("Input array should not be empty")
        return None
    # below array will store sumulative sum of elements 
    # of A from index 0 upto i.
    cumsum = np.zeros(len(A), dtype=int)
    cumsum[0] = A[0] 
    for i in range(1, len(A)):
        cumsum[i] = cumsum[i - 1] + A[i]
    result = np.zeros((len(A), len(A)), dtype=float)
    for i in range(0, len(A)):
        cum_sum_minus = cumsum[i]
        for j in range(i, len(A)):
            result[i][j] = cumsum[j] / (j - i + 1) # average
            cumsum[j] = cumsum[j] - cum_sum_minus
    return result

if __name__ == "__main__":
    test_list = list(range(4000))
    start = time.time()
    # Testing Q6 algorithm
    res6 = Q6(test_list)
    end_6 = time.time()
    print(f"Q6 Algorithm took %.3f seconds" %(end_6 - start))
    # Testing Q5 algorithm
    res5 = Q5(test_list)    
    end_5 = time.time()
    print(f"Q5 Algorithm took %.3f seconds" %(end_5 - end_6))
    print("%.2f times faster" %((end_5 - end_6) / (end_6 - start)))
        
    
    
    