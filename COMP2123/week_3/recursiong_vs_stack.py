from perm_stack import permutations
from tut_permutations import permutations_B
import time

if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1, 2, 3 ,3, 3]
    
    start = time.time()
    resultA = permutations(arr)
    print("Stack Result: %.2f" % (time.time() - start))
    
    start = time.time()
    resultB = permutations_B(arr)
    print("Recursion Result: %.2f" % (time.time() - start))
    