import numpy as np

from math import factorial, e
vec_fac = np.vectorize(factorial)

def e_x(num, n = 10):
    terms = np.full(n + 1, num)
    degrees = np.arange(n + 1) # [1, 2, 3, ... 10]
    result = np.sum(terms ** degrees / vec_fac(degrees))
    return result

if __name__ == "__main__":
    print("Actual value of e^i vs Estimate by Maclaurin Series\n")
    
    power = 3 # random.randint()
    actual_e_power = e ** power
    print(f"Actual value of e^{power}: {actual_e_power:.2f}")
    
    n = 0
    while True:
        try:
            estimate = e_x(power, n)
            print(f"Estimate with {n} terms: {estimate : .2f}    " \
                f"error : {(actual_e_power - estimate)/actual_e_power*100:.2f}%")
        except Exception as E:
            print("Estimate by MacLauren Series stopped due to data storage limit (long)")
            break
        n += 1
