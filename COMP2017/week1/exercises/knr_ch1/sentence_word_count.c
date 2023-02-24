#include <stdio.h>

int main(){
    int character_count = 0;
    int word_count = 0;
    int blank_space = 0;
    char c;
    int prev_blank = 0;
    while((c = getchar()) != 'q'){
        if (c == ' ' || c == '\t'){
            if (prev_blank == 0)
                word_count += 1;
            prev_blank = 1;
            blank_space += 1;
        }
        else if (c == '\n'){
            word_count += 1;
            printf("words: %3d chrs: %3d blank: %3d\n",
                word_count, character_count, blank_space);
            character_count = 0;
            word_count = 0;
            blank_space = 0;
        }
        else{
            prev_blank = 0;
            character_count += 1;
        }
        
    }
}