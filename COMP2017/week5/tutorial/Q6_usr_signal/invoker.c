#include <stdio.h>
#include <signal.h>

int main(){
    int pid;
    if(!scanf("%d", &pid))
        return 0;
    
    kill(pid, SIGUSR1);
}
