#include <stdio.h>

int main(){
    /*
    << : bits moved left by the number specified
    >> : bits moved right by the number specified
    */
    unsigned int a = 0b00111100; // 60
    unsigned int b = 0b00001101; // 13

    // 1111 0000 = 240
    printf("Left shift: %d\n", a << 2);
    // 0000 1111 = 15
    printf("Right shift: %d\n", a >> 2);
    // 1111 0000 0000 = 4095 - 255 = 3840
    printf("Right shift: %d\n", a << 6);
    // 0000 0000 = 0
    printf("Right shift: %d\n", a >> 6);


}