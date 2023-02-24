#include <stdio.h>

#define MAX_FERENHEIT 300
#define MIN_FARENHEIT 0
#define STEP_INCREASE 30

int main(){

    for (int f = MIN_FARENHEIT; f <= MAX_FERENHEIT; f+= STEP_INCREASE){
        float c = (f - 32) * 5/9.0;
        printf("%5d°F -> %5.1f°C\n", f, c);
    }
}