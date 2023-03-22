def algorithm(A, k):
    n = len(A)
    B = [None] * (n-k)
    for i in range(0, n-k):
        B[i] = 0
        for j in range(0, k):
            B[i] = B[i] + A[i+j]
    print(B)
    return B
        
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    algorithm(arr, 4);