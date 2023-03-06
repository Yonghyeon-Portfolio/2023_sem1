#include <stdio.h>

int main(){
    char character_name[] = "용현";
    int character_age = 35;

    printf("There once was a man nameD %s\n", character_name);
    printf("He was %d years old\n", character_age);

    printf("%ld %ld\n", sizeof(character_name), sizeof(character_age));
}