#include <stdio.h>

int main(){
    // decimal integers
    int int_A = 105;
    short int_B = -999;
    printf("%d %d -- %ld %ld\n", int_A, int_B, sizeof(int_A), sizeof(int_B));

    // hexadeximal integers
    int int_C = 0x105;
    short int_D = -0x999;
    printf("%d %d -- %ld %ld\n", int_C, int_D, sizeof(int_C), sizeof(int_D));

    // floats and doubles
    float float_A = 0.001;
    float float_B = 1e-3;
    printf("%f %f A == B: %d\n", float_A, float_B, (float_A == float_B));

    double double_A = 1.32e10;
    printf("%10.2f %ld\n", double_A, sizeof(double_A));

    // default data types
    printf("%ld %ld %ld\n", sizeof(13), sizeof(25.0), sizeof(25.0f));

}