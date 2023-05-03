#include <stdint.h>
#include <stddef.h>
#include <stdio.h>

// 4 bytes (signed, unsigned integer)
unsigned a;
int b;

// 1 byte
char c;
uint8_t u8;

// 2 bytes
short d;
uint16_t e; 

// 8+ bytes
long f;
size_t g; // denotes address
long long h;

struct quoll{
    char name[20];
    uint8_t age;
}; // 20 + 1 bytes

struct quokka{
    char* name;
    struct quokka* mom;
    struct quokka* dad;
}; // 8 + 8 + 8 bytes

union mammal{
    struct quoll a;
    struct quokka b;
}; // 24 bytes

int main(){
    printf("4 bytes: %ld %ld\n", sizeof(a), sizeof(b));
    printf("1 byte: %ld %ld\n", sizeof(c), sizeof(u8));

    printf("8 bytes: %ld %ld %ld\n", sizeof(f), sizeof(g), sizeof(h));

    printf("struct union sizes: %ld %ld %ld\n", 
        sizeof(struct quoll), sizeof(struct quokka), sizeof(union mammal));

}


