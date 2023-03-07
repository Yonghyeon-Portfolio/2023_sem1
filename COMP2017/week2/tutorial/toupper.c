#include <stdio.h>
#include <ctype.h>

int main(){
    char c;
    while (1){
        c = getchar();
        if (c == EOF)
            break;
        putchar(toupper(c));
    }
}