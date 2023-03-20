#include <stdio.h>
#include <string.h>


int main(){
    char name[10];
    strcpy(name, "Isaac Kim");
    
    char nickname[20] = "똑똑이";

    printf("%s -- %ld %ld\n", name, strlen(name), sizeof(*name));
    printf("%s -- %ld %ld\n", nickname, strlen(nickname), sizeof(*nickname));
}