#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(){
    printf("Hello my pid is %d\n", getpid());
    
    int result = execl("/bin/echo", "echo", "hello", "world", NULL);
    if (result < 0){
        perror("Error executing new process");
    }
    else{
        puts("This part is overwritten. Hence, is never called in reality)");
    }
    return 0;
}