#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ASCII_start (32)
#define ASCII_end (126)

char rand_char(){
    // 32 ~ 126 ASCII code
    int r = rand();
    r = ASCII_start + (r % (ASCII_end - ASCII_start + 1));
    return (char)r;
}

int main(int argc, char *argv[]){
    if (argc < 2){
        puts("Specify the length of password via " \
            "command line argument when you run the program.");
        return 0;
    }

    srand(time(NULL));
    for (int i = 0; i < atoi(argv[1]); i++)
        putchar(rand_char());
    putchar('\n');
    return 1;
}