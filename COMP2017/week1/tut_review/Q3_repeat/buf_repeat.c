#include <stdio.h>
#define BUFFER_LEN (32 + 1)

int main(){
    char buffer[BUFFER_LEN];
    while (fgets(buffer, sizeof(buffer), stdin)){
        printf("%s", buffer);
    }
}