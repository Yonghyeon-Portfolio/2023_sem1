#include <stdio.h>
#include <string.h>

int main(){
    char *input1 = "tofu island";
    char *input2 = "tofu island";
    char *input3 = "Tofu island";
    char *input4 = "Tofu islanD";

    // input1 vs input2
    printf("%d\n", strcmp(input1, input2));
    if (!strcmp(input1, input2))
        printf("Input 1 and 2 are equal\n");

    // input3 vs input4   
    printf("%d\n", strcmp(input3, input4));
    if (!strcmp(input3, input4))
        printf("Input 3 and 4 are equal");
}