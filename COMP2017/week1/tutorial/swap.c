#include <stdio.h>

void swap(int* a, int* b) {
    int temp = *a;
        printf("%d %d %d %p %p\n", temp, *a, *b, a, b);
    *a = *b;
    *b = temp;
    return;
}
int main(void) {
    int a = 2;
    int b = 3;
    swap(&a, &b); //Specify the variables to swap
    printf("ab: %d %d\n", a, b); // should print 3 2
    return 0;
}