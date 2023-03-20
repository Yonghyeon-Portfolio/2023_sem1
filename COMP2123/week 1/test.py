import time
import random
from single_stock_trade import trade_dates_1
from single_stock_trade import trade_dates_2

def produce_random_list(n):
    ls = []
    for i in range(n):
        ls.append(random.randint(-n, n))
    return ls

if __name__ == "__main__":
    testcase_A = [3, -2, -5, -8, 3, 9, 15, -3, 9]
    testcase_B = [-1, -2, -3, -4]
    testcase_C = [1, 2, 3, 4, 5]
    testcase_D = [1, 2, 3, 1, -2,-5, -2, 1, 2, 3]
    testcase_E = [0, 0, 0, 0, 0, -1, 1, -1, 1]
    rand_testcase_A = produce_random_list(50)
    rand_testcase_B= produce_random_list(100)
    rand_testcase_C = produce_random_list(1000)
    rand_testcase_D = produce_random_list(10000)
    rand_testcase_E = produce_random_list(100000)
    
    # print(trade_dates_1(testcase_A))
    # print(trade_dates_1(testcase_B))
    # print(trade_dates_1(testcase_C))
    # print(trade_dates_1(testcase_D))
    # print(trade_dates_1(testcase_E))
    
    # print(trade_dates_2(testcase_A))
    # print(trade_dates_2(testcase_B))
    # print(trade_dates_2(testcase_C))
    # print(trade_dates_2(testcase_D))
    # print(trade_dates_2(testcase_E))
    
    start = time.time()
    print(trade_dates_1(rand_testcase_A))
    print(trade_dates_1(rand_testcase_B))
    print(trade_dates_1(rand_testcase_C))
    print(trade_dates_1(rand_testcase_D))
    print("method 1: %.2fs" %(time.time() - start))
    
    start = time.time()
    print(trade_dates_2(rand_testcase_A))
    print(trade_dates_2(rand_testcase_B))
    print(trade_dates_2(rand_testcase_C))
    print(trade_dates_2(rand_testcase_E))
    print("method 2: %.2fs" %(time.time() - start))
    