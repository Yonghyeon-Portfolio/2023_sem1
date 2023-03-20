#include <stdio.h>

int main(int argc, char *argv[]){
    int number_of_args = argc;
    char *program_name = argv[0];
    char *argument_1 = argv[1];
    
    printf("Number of cmd line arguments: %d\n", number_of_args);
    printf("File name: %s\nArgument 1: %s\n", program_name, argument_1);
}