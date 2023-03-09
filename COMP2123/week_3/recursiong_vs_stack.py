from perm_stack import permutations
from perm_stack2 import stack_perm
from tut_permutations import permutations_B
import time
import random

if __name__ == "__main__":
    # arr = [1, 2, 3, 4, 
    # 5, 6, 7, 8, 9]
    arr = "A B C D E F G H I J".split()
    start = time.time()
    resultA = permutations(arr)
    print("Stack Result: %.2fs" % (time.time() - start))
    
    start = time.time()
    resultB = stack_perm(arr)
    print("Stack (2) Result: %.2fs" % (time.time() - start))
    
    start = time.time()
    resultC = permutations_B(arr)
    print("Recursion Result: %.2fs" % (time.time() - start))
    
    num = len(resultA)
    
    print("A:", resultA[10])
    print("B:", resultB[10])
    print("C:", resultC[10])