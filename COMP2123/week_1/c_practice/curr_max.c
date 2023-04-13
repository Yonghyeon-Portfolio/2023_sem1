#include <stdio.h>

/*
 * Finds the maximum element in an integer array.
 *
 * A: Pointer to the integer array.
 * n: Number of elements in the array.
 *
 * returns: Maximum element in the array, or -1 if the array is empty (n < 1).
 */
int arrayMax(int *array, int arr_size, int *err_flag){
    if (arr_size < 1){ // Check if the array is empty
        *err_flag = 1;
        printf("Error: The given array is empty\n");
        return -1;
    }

    int max = array[0]; // Initialize max with the first element of the array
    for (int i = 1; i < arr_size; i++){
        // Update max if a larger element is found in the array
        if (array[i] > max)
            max = array[i];
    }
    return max; // Return the maximum element in the array
}

int main(){
    // int arr[] = {1, 2, 3, 4, 5}; 
    // int arr[] = {-1, -2, -3, -4, -5}; 
    int arr[] = {};
    int error_occured = 0; // initialise as false(0)
    int max = arrayMax(arr, sizeof(arr)/sizeof(int), &error_occured); 
    if (!error_occured)
        printf("Maximum element: %d\n", max);
    return 1; 
}