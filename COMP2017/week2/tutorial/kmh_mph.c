#include <stdio.h>
#define M (0.621371)

int main(){
    float kmh = 0;
    float hours = 0;

    printf("What is your current km/h: ");
    scanf("%f", &kmh);
    printf("How many hours are you traveling for?: ");
    scanf("%f", &hours);

    float distance_km = kmh * hours;
    float mph = kmh * M;
    float distance_mi = mph * hours;
    
    printf("You will cover: %.2f km (%.2f mi)\n", distance_km, distance_mi);
    printf("While traveling at %.2fkm/h (%.2f mph)\n", kmh, mph);


}