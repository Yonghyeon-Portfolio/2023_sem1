#include <stdio.h>
#define BUF_LEN (16)

struct counter{
    unsigned int chrs;
    unsigned int word;
    unsigned int line;
};

void update_counter(struct counter* ctr, char *str){
    char c;
    for (int i = 0; i < BUF_LEN; i++){
        c = str[i];
        if (c == '\0')
            break;
        ctr->chrs += 1;
        if (c == ' ')
            ctr->word += 1;
        else if (c == '\n'){
            ctr->line += 1;
            ctr->word += 1;
        }
    }
}

void print_counter(struct counter* ctr){
    printf("%4d %4d %4d\n", ctr->line, ctr->word, ctr->chrs);
    ctr->chrs = 0;
    ctr->word = 0;
    ctr->line = 0;
}

int main(int argc, char *argv[]){
    char buffer[BUF_LEN];
    struct counter ctr = {0, 0, 0};
    if (argc == 1){
        while (fgets(buffer, BUF_LEN, stdin) != NULL){
            update_counter(&ctr, buffer);
        }
        print_counter(&ctr);
        return 0;
    }
    for (int i = 1; i < argc; i++){
        FILE *fp = fopen(argv[i], "r");
        if (fp == NULL){
            printf("Unable to open the file: %s\n", argv[i]);
            continue;
        }
        while (fgets(buffer, BUF_LEN, fp) != NULL){
            update_counter(&ctr, buffer);
        }
        print_counter(&ctr);
    }
    return 0;
}