#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <signal.h>

int pid;

void end_child_sig_handler(int signal){
    printf("Sending signal to pid: %d\n", pid);
    if (pid > 0)
        kill(pid, SIGUSR1);
}

int main(int argc, char *argv[]){
    if (argc != 2){
        puts("Provide one system argument (waiting time for its child)");
        return 1;
    }
    pid = fork();
    signal(SIGINT, end_child_sig_handler);
    
    if (pid == 0){
        execl("./childp", "childp", argv[1], NULL);
        perror("excel failed");
        return 1;
    }
    else if (pid < 0){
        perror("fork failed");
        return 1;
    }
    else {
        int status;
        waitpid(pid, &status, 0);
        if (WIFEXITED(status)) {
            printf("Child exited with status %d\n", WEXITSTATUS(status));
        } else if (WIFSIGNALED(status)) {
            printf("Child terminated by signal %d\n", WTERMSIG(status));
        }   
    }
    return 0;
}