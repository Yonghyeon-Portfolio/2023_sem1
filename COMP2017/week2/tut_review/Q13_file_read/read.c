#include <stdio.h>

int main(){
    FILE *fp;
    fp = fopen("hello.txt", "r");

    char str[10];
    while (fgets(str, 10, fp)){
        printf("%s", str);
    }

    fclose(fp);
    return 1;
}