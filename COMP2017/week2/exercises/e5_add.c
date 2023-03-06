#include <stdio.h>

int main(){
    double num_A;
    double num_B;

    printf("Enter Number 1: ");
    scanf("%lf", &num_A);

    printf("Enter Number 2: ");
    scanf("%lf", &num_B);

    printf("%.2lf + %.2lf = %.2lf\n", num_A, num_B, num_A + num_B);
}