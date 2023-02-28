#include <stdio.h>
#define NAME_LENGTH (256)


int main(int argc, char **argv){
    if (argc <= 1)
        return 1;
    
    printf("What is your name?: ");

    char name[NAME_LENGTH];
    fgets(name, NAME_LENGTH, stdin);

    printf("%s %s", argv[1], name);
}