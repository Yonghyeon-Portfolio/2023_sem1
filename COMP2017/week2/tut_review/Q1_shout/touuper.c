#include <stdio.h>
#include <ctype.h>

char get_upper_char(){
    char c = getchar();
    if (c == EOF)
        return c;
    else
        return toupper(c);
}

int main(){
    char upperC;
    while ((upperC = get_upper_char()) != EOF){
        printf("%c", upperC);
    }
}