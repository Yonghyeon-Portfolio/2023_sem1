#include <stdio.h>
#include <string.h>

int main(){
    char input[100];
    printf("Enter a string of length < 100\n\t→ ");
    fgets(input, 100, stdin);

    int length = strlen(input) - 2;
    printf("  (Rev)\t→ ");
    for (int i = length; i >= 0; i--)
        putchar(input[i]);
    putchar('\n');
}