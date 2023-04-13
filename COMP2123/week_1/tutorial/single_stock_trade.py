import time
from collections import deque

def sum_up_arr(ls_A):
    ls_B = [0]
    for i in range(len(ls_A)):
        ls_B.append(ls_B[i] + ls_A[i])
    return ls_B

def trade_dates_1(daily_fluctuations):
    '''
    It is assumed that stocks are 
    - bought at the start of day (before any fluctuation happends)
    - sold at the end of day (after all fluctuation has happended)
    '''
    ovr_performance = sum_up_arr(daily_fluctuations)
    max_gap = 0
    buy_sell_point = (None, None)
    for i in range(0, len(ovr_performance)-1):
        for j in range(i+1, len(ovr_performance)):
            profit = ovr_performance[j] - ovr_performance[i]
            if profit > max_gap:
                max_gap = profit
                buy_sell_point = (i+1, j)
    return buy_sell_point
    
def trade_dates_2(daily_fluctuations):
    '''
    It is assume that stocks are 
    - bought at the start of day (before any fluctuation happends)
    - sold at the end of day (after all fluctuation has happended)
    '''
    
    ovr_performance = sum_up_arr(daily_fluctuations)
    minimums = [0]
    buy_date = [0]
    maximums =  deque([ovr_performance[-1]])
    sell_date = deque([len(ovr_performance)-1])
    
    
    for i in range(1, len(ovr_performance)-1):
        if ovr_performance[i] < minimums[-1]:
            minimums.append(ovr_performance[i])
            buy_date.append(i)
        else:
            minimums.append(minimums[-1])
            buy_date.append(buy_date[-1])
            
    for i in range(len(ovr_performance)-2, 0, -1):
        if ovr_performance[i] > maximums[-1]:
            maximums.appendleft(ovr_performance[i])
            sell_date.appendleft(i)
        else:
            maximums.appendleft(maximums[-1])
            sell_date.appendleft(sell_date[0])
    maximums = list(maximums) 
    sell_date = list(sell_date)
    
    max_gap = 0
    buy_sell_point = (None, None)
    for i in range(len(buy_date)):
        profit = maximums[i] - minimums[i]
        if profit > max_gap:
            max_gap = profit
            buy_sell_point = (buy_date[i] + 1, sell_date[i])
    return buy_sell_point
    
    
        
    

    