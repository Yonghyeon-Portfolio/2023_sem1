#include <stdio.h>

#define UPPER_LIMIT 300
#define LOWER_LIMIT 0
#define STEP 20

int main(){
    /* table starts with lowest farenheit temperature*/
    float farenheit = LOWER_LIMIT;
    float celsius;

    while(farenheit <= UPPER_LIMIT){
        celsius = (farenheit -32) * 5 / 9.0;
        printf("%3.0f  %5.1f\n", farenheit, celsius);
        farenheit += STEP;
    }
}