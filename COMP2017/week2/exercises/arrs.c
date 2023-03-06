#include <stdio.h>

int main(){
    int nums[5] = {12, 15, 20, 30, 5};
    int * ptr = &nums[2];

    printf("%d %d\n", *ptr, *(ptr+1));
    printf("%p %p\n", ptr, ptr+1);
}