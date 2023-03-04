import numpy as np
import pandas as pd
import matplotlib as plt

def read_data():
    try:
        data = pd.read_csv("W2_AppleMusic.csv")
        return data
    except Exception as e:
        print(e)
        return None

def print_data(data, n):
    print(data.head(n))
    

if __name__ == "__main__":
    raw_data = read_data()
    print_data(raw_data, 1)
    