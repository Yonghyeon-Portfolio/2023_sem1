#include <stdio.h>
#include <unistd.h>
#include <signal.h>

int interrupted = 0;

void parent_end(int siganl){
    sleep(3);
    interrupted = 1;
}

void child_end(int signal){
    sleep(2);
    interrupted = 1;
}

void grandchild_end(int signal){
    sleep(1);
    putchar('\n');
    interrupted = 1;
}

int main(){
    int ancestor = getpid();

    int childA = fork();
    if (childA)
        printf("I'm %d, and just gave birth to %d\n", getpid(), childA);

    if (getpid() != ancestor)
        sleep(1);

    int childB = fork();
    if (childB)
        printf("I'm %d, and just gave birth to %d\n", getpid(), childB);

    if (childA && childB)
        signal(SIGINT, parent_end);
    else if (childA || childB)
        signal(SIGINT, child_end);
    else 
        signal(SIGINT, grandchild_end);
    
    while (!interrupted){
        usleep(1000);
    }
    
    printf("Process %d has terminated\n", getpid());
    return 0;
}