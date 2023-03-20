#include <stdio.h>

int main(){
    short int a = 1;
    long int b = 2;
    unsigned int c = 3;
    printf("%ld %ld %ld\n", sizeof(a), sizeof(b), sizeof(c));

    long double e = 1.7e80;
    printf("%ld\n", sizeof(e));
}