#include <stdio.h>
#include <signal.h>
#include <unistd.h>

int interrupted = 0;

void interrupt_handler(){
    interrupted = 1;
    puts("\nInterrupt signal has been received.");
}

int main(){

    signal(SIGINT, interrupt_handler);
    int idx = 0;
    while (!interrupted){
        printf("waiting...(%.1f s)\n", idx/1000.0);
        usleep(1000);
        idx++;
    }
    printf("Program terminated.\n");
}
