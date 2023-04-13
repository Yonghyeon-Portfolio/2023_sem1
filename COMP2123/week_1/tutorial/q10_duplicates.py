import time
import random

def find_duplicate(A : list[int]):
    if len(A) < 1:
       return None
    sorted_A = sorted(A)
    for i in range(0, len(sorted_A)-1):
        if sorted_A[i] == sorted_A[i+1]:
            return True
    return False

def brute_force(A : list[int]):
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                continue
            if A[i] == A[j]:
                return True
    return False 
            
if __name__ == "__main__":
    test_A = [1, 2, 3, 4, 5]
    test_B = [1, 2, 3, 4, 4, 5]
    find_duplicate(test_A) == False
    find_duplicate(test_B) == True 
    
    # test1
    n = 100; test_time = 1000
    test_ls = [random.randint(-n*1000, n*1000) for i in range(n)]
    start = time.time()
    for i in range(test_time):
        res1 = find_duplicate(test_ls)
    mid = time.time()
    for i in range(test_time):
        res2 = brute_force(test_ls)
    end = time.time()
    assert res1 == res2
    print("Sort then scan: %.3f seconds" % (mid - start))
    print("Brute Force: %.3f seconds" % (end - mid))
    