#include <stdio.h>

int read_input(double *cur_speed, double *travel_time){
    printf("What is your current km/h: ");
    if (scanf("%lf", cur_speed) != 1 || *cur_speed < 0)
        return 0;
    printf("How many hours are you traveling for: ");
    if (scanf("%lf", travel_time) != 1 || *travel_time < 0)
        return 0;
    return 1;
}

int main(){
    // Ask for current speed in kilometres per hour
    double cur_speed, travel_time;
    int read_success = read_input(&cur_speed, &travel_time);
    if (!read_success){
        printf("Invalid input was detected. Exiting program...\n");
        return 0;
    }

    double cur_speed_mph = cur_speed / 1.609;
    double cover_distance_km = cur_speed * travel_time;
    double cover_distance_mi = cur_speed_mph * travel_time;

    printf("\nYou will cover: %.2f km (%.2f mi)\n", cover_distance_km, cover_distance_mi);
    printf(" while traveling at %.2f km/h (%.2f mph)\n", cur_speed, cur_speed_mph);
}