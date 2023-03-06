#include <stdio.h>

int main(){
    const char * ptr = "Hello";
    ptr += 1;
    const char array[] = "hello";
    const char array2[] = { 'h', 'e', 'l', 'l', 'o' };
    const char array3[] = { 'h', 'e', 'l', 'l', 'o', '\0' };
    const char array4[5] = { 'h', 'e', 'l', 'l', 'o' };
    const char array5[6] = { 'h', 'e', 'l', 'l', 'o', 0 };
    const char array6[20] = { 'h', 'e', 'l', 'l', 'o' };
    const char array7[20] = { 0 };
    const char array8[20] = "hello";


printf("%zu %zu\n", sizeof(ptr), sizeof(array));
printf("%zu %zu\n", sizeof(array2), sizeof(array3));
printf("%s %d %zu %zu\n", ptr, *ptr, sizeof(*ptr), sizeof(&array));
printf("%zu %zu\n", sizeof(&array2), sizeof(&array3));

int x[] = { 1, 2, 3 };
int * p1 = x;
int * p2 = x + 1;
printf("%zu %zu\n", sizeof(x[0]), sizeof(x));
printf("p1 value, p2 value: %d %d\n", *p1, *p2);
printf("p1 value with offset: %d\n", *(p1 + 1));
printf("p2 value with offset: %d\n", *(p2 - 1));
printf("p1 value plus scalar: %d\n", (*p1) + 2);
printf("p1 plus offset followed: %d\n", *(p1 + 2));
printf("p1 plus offset followed: %d\n", p1[2]);

}