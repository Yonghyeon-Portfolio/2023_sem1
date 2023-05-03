#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <time.h>
#include <string.h>

void handler(int sig){
    time_t mytime = time(NULL);
    char * time_str = ctime(&mytime);
    time_str[strlen(time_str)-1] = '\0';
    printf("Current Time : %s\n", time_str);
}

int interrupted = 0;
void end_prog_handler(int sig){
    interrupted = 1;
}

int main(){
    signal(SIGUSR1, handler);
    signal(SIGINT, end_prog_handler);
    while (!interrupted){
        sleep(1);
    }
    puts("\nShutting down..");
}