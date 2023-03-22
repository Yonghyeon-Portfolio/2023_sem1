#include <stdio.h>

int main(){
    int minutes = 0;
    printf("Minute -> Days/Years Converter\n Enter number of mniutes: ");
    scanf("%d", &minutes);

    double hours = minutes / 60.0;
    double days = hours / 24.0;
    double years = days / 365.0;

    printf("%d minutes is equivalent to %.3f days\n", minutes, days);
    printf("%d minutes is equivalent to %.3f years\n", minutes, years);

}