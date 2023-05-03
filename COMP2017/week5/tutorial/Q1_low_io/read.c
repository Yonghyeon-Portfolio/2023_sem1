#include <unistd.h>
#include <fcntl.h>
#define BUF_LEN (10)

int main(){
    int file_descriptor = open("info.txt", O_RDONLY);
    if (file_descriptor == -1)
        return 1; // failed to open
    
    char buffer[10];
    int read_len = -1;
    while ((read_len = read(file_descriptor, buffer, BUF_LEN)) > 0){
        write(STDOUT_FILENO, buffer, read_len);
    }
    
    return 0;
}