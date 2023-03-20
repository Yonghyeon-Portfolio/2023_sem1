#include <stdio.h>
#include <stdbool.h>

int main(){
    _Bool a = true;
    _Bool b = false;
    bool c = true;
    if (a)
        puts("A is True!");
    if (!b)
        puts("B is False!");
    if (c)
        puts("C is true!");
    return 0;
}