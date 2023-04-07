import time
from collections import deque

def with_array(n, method):
    start = time.time()
    ls = []
    for i in range(n):
        ls.append(i)
    if method == "FIFO":
        for i in range(n):
            # print(ls)
            ls.pop(0)
    elif method == "LIFO":
        for i in range(n):
            # print(ls)
            ls.pop()
    return time.time() - start
        
def with_queue(n, method):
    start = time.time()
    que = deque()
    for i in range(n):
        que.append(i)
    if method == "FIFO":
        for i in range(n):
            # print(que)
            que.popleft()
    elif method == "LIFO":
        for i in range(n):
            # print(que)
            que.pop()
    return time.time() - start

if __name__ == "__main__": 
    NUM = 100000
    array_result = with_array(NUM//10, "FIFO")
    queue_result = with_queue(NUM, "FIFO")
    
    print("%sList result: %.3f\nQueue Result: %.3f"
          %("---First In First Out---\n", array_result, queue_result))

    array_result = with_array(NUM, "LIFO")
    queue_result = with_queue(NUM, "LIFO")
    
    print("%sList result: %.3f\nQueue Result: %.3f"
          %("---Last In First Out---\n", array_result, queue_result))
    