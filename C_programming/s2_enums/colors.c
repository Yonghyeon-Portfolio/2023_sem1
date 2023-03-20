#include <stdio.h>

enum primary_color {red, yellow, blue};

enum primary_color my_color = red;
enum primary_color your_color = blue;

int main(){
    printf("%d %d\n", my_color, your_color);

    // enum primary_color invalid = green;
    // printf("%d\n", invalid);

    // random integer value isn't checked by compiler (careful!!)
    enum primary_color random = 3;
    printf("%d\n", random);
}