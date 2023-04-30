#include <stdio.h>
#include <string.h>

#define  MAX_INPUT_SIZE (100 + 1)

int main(){
    char line[MAX_INPUT_SIZE];
    while (fgets(line, sizeof(line), stdin)){
        // line's len : 1 ~ 100 (max-input-size)
        int input_len = strlen(line); 

        char rev_line[input_len + 1];
        rev_line[input_len] = '\0';
        for (int i = 0; i < input_len; i++)
            rev_line[input_len - i - 1] = line[i];
        
        // new line char handling
        if (rev_line[0] == '\n')
            printf("%s\n", rev_line + 1);
        else
            printf("%s", rev_line);
    }
}