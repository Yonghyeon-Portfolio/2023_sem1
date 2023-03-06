#include <stdio.h>

int main(){
    char character_name[] = "Isaac Kim";
    char* ptr = &character_name[0];
    int character_age = 35;

    printf("There once was a man nameD %s\n", character_name);
    printf("His name starts with %c.\n\n", *ptr);
    printf("He was %d years old\n", character_age);

    printf("%ld %ld\n", sizeof(character_name), sizeof(character_age));
}