#include <stdio.h>
#include <stdlib.h>

#define SIZE (100)

void print_arr(int* arr){
     for (int i = 0; i < SIZE; i++){
        if (i % 10 == 0 && i != 0)
            putchar('\n');
        printf("%d ", arr[i]);
    }
    putchar('\n');
}

int main(){
    int* arr = malloc(SIZE * sizeof(int));
    if (arr == NULL)
        return 1;
    for (int i = 0; i < SIZE; i++){
        arr[i] = 5;
    }
    puts("Before freeing...");
    print_arr(arr);

    puts("After freeing...");
    free(arr);
    print_arr(arr);
}