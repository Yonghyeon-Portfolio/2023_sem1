#include <stdio.h>

int main(){
    /*
    & : binary and
    | : binary or
    ^ : binary xor
    ~ : binary ones complement
    */
   unsigned int a = 0b00111100; // 60
   unsigned int b = 0b00001101; // 13
   
    // & : 00001100 = 12
    printf("Binary AND: %d\n", a & b);
    // | : 00111101 = 61
    printf("Binary OR: %d\n", a | b);
    // ^ : 00110001 = 49
    printf("Binary XOR: %d\n", a ^ b);
    // ~ : 11000011 = 
    printf("One's complement: %d\n", ~a);

}