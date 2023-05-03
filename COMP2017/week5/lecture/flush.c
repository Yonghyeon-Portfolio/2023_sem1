#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

int main(){
    // Create (if not exists) and write to file.txt 
        //(644 : read, write for owner, read-only for others)
    int fd = open("file.txt", O_CREAT | O_WRONLY, 0644);
    if (fd == -1){
        perror("Error opening file");
        return 1;
    }
    write(fd, "1", 1);
    close(fd);
    // char msg[] = "Hello World, my dear friends!\nWelcome home!\n";
    // for (int i = 0; i < sizeof(msg); i++){
    //     write(f)
    // }
}