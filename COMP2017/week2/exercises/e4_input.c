#include <stdio.h>
#include <stdlib.h>

int main(){
    /*
    int age;
    printf("Enter your age: ");
    scanf("%d", &age);
    printf("You were born in year %d or %d\n", 2023-age-1, 2023-age);

    float wam;
    printf("Enter your WAM: ");
    scanf("%f", &wam);
    printf("Your WAM is %.2f\n", wam);
    */

    char name[20];
    printf("Enter your name: ");
    // note that pointer is already address (no need to put ampersand)
    // scanf("%s", name);
    // Above code cannot handle white spaces in name
    fgets(name, 20, stdin);
    printf("Your name is %s", name);

    char name2[20];
    printf("Enter your name: ");
    fgets(name2, 20, stdin);
    printf("Your name is %s.", name2);


    return 0;
}