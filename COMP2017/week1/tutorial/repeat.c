#include <stdio.h>
#define LINE_SIZE (128)

int main(){
    char buffer[LINE_SIZE];
    while(fgets(buffer, LINE_SIZE, stdin)){
        printf("%s", buffer);
    }
}