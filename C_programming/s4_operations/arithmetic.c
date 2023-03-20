#include <stdio.h>
// use -lm flag
#include <math.h>

int main(){
    double a = 8.9;
    double b = 6.0;

    int sum = a + b;
    double sum_d = a + b;
    printf("sum: %d or %.1f\n", sum, sum_d);

    double diff = a - b;
    double prod = a * b;
    double div = a / b;
    // casting to int is same as floor()
    int mod = (int)a % (int)b;
    // error: double mod = a % b;
    printf("%.2f %.2f %.2f %d\n", diff, prod, div, mod);

    double hypotenuse = sqrt(pow(a, 2) + pow(b, 2));
    printf("sqrt(a^2 + b^2) = %.2f\n", hypotenuse);

    // increment, decrement
    int i = 10;
    printf("%d\n", i++);
    printf("%d\n", ++i);
    printf("%d\n", i++);
    printf("%d\n", ++i);    
}   