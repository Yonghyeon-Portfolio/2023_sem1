#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>

int interrupted = 0;

void sigint_handler(int signal){
    putchar('\n');
}

void end_handler(int signal){
    interrupted = 1;
}

int input_handler(int argc, char *argv[]){
    if (argc != 2){
        puts("One system argument must be provided");
        exit(1);
    }
    char *end_ptr;
    long o = strtol(argv[1], &end_ptr, 10);
    if (*end_ptr != '\0'){
        printf("Given argument is not a number: %s\n", argv[1]);
        exit(1);
    }
    return (int)o;
}

int main(int argc, char *argv[]){
    int wait_sec = input_handler(argc, argv);
    signal(SIGUSR1, end_handler);
    signal(SIGINT, sigint_handler);

    while (!interrupted && (wait_sec > 0)){
        puts("child process running...");
        sleep(1);
        wait_sec --;
    }
    if (!wait_sec)
        puts("Timeout: terminating child process");
    else
        puts("Child terminated before timeout");
    return 0;
}