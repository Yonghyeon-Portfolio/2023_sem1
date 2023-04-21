from sys import path 
import random
import time

path.append("ED_priorQ_list")
path.append("ED_priorQ_heap")
from list_pq import PriorityQueue as PQList
from heap_pq import PriorityQueue as PQHeap

def list_pq_sort(random_arr, print_time = False): # time O(n^2) + expensive space
    start = time.time()
    PQ = PQList()
    for item in random_arr:
        PQ.insert(item, None)
    result = []
    while not PQ.is_empty():
        result.append(PQ.remove_min().get_key())
    if print_time:
        print("LIST PQ sort time: %.2f" %(time.time() - start))
    return result

def heap_pq_sort(random_arr, print_time = False): # efficient O(log n) time
    start = time.time()
    PQ = PQHeap()
    for item in random_arr:
        PQ.insert(item, None)
    result = []
    while not PQ.is_empty():
        result.append(PQ.remove_min().get_key())
    if print_time:
        print("HEAP PQ sort time: %.2f" %(time.time() - start))
    return result

def selection_sort(random_arr, print_time = False):
    start = time.time()
    work_arr = random_arr.copy()
    for i in range(len(work_arr)):
        min_idx = i
        for j in range(i, len(work_arr)):
            if work_arr[j] < work_arr[min_idx]:
                min_idx = j
        work_arr[i], work_arr[min_idx] = work_arr[min_idx], work_arr[i]
    if print_time:
        print("Selection sort time: %.2f" %(time.time() - start))
    return work_arr

def insertion_sort(random_arr, print_time = False):
    start = time.time()
    work_arr = random_arr.copy()
    for i in range(1, len(work_arr)):
        j = i
        elem = work_arr[i]
        while j > 0:
            if work_arr[j-1] > elem:
                work_arr[j] = work_arr[j-1]
                j -= 1
            else:
                break
        work_arr[j] = elem
    if print_time:
        print("Insertion sort time: %.2f" %(time.time() - start))
    return work_arr        

                
def default_sort(random_arr, print_time = False):
    start = time.time()
    work_arr = random_arr.copy()
    work_arr.sort()
    if print_time:
        print("Default sort time: %.2f" %(time.time() - start))
    return work_arr 
                
if __name__ == "__main__":
    n = 100000
    # random_keys = [-1, -2, 1, -3]
    random_keys = [random.randint(-n, n) for i in range(n)]
    
    python_result = default_sort(random_keys, print_time=True)
    pq_heap_result = heap_pq_sort(random_keys, print_time=True)
    # print(pq_heap_result)
    # pq_list_result = list_pq_sort(random_keys, print_time=True)
    # print(pq_list_result)
    # selection_result = selection_sort(random_keys, print_time=True)
    # print(selection_result)
    # insertion_result = insertion_sort(random_keys, print_time=True)
    # print(insertion_result)
    
        