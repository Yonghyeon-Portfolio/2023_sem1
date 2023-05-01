#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct varchar{
    char *content;
    int length;
};

int append_nstr(struct varchar *dest, char *str, int len){
    if (len <= 0)
        return 0;
    // Assumes len represents the length of str without 
    // accounting for terminating null character \0.
    dest->length += len;
    dest->content = realloc(dest->content, sizeof(char) * dest->length);
    strncat(dest->content, str, len); // terminates with \0
    return 1;
}

int format(char *dest, char prev_char, int streak){
    for (int i = 0; i < 10; i++)
        dest[i] = '\0';
    dest[0] = '(';
    dest[1] = prev_char;
    dest[2] = ',';
    dest[3] = ' ';
    // n = (1 ~ 99999)
    sprintf(dest + 4, "%d", streak);
    int format_len = strlen(dest);
    dest[format_len] = ')';
    return format_len + 1;
}

int encode(char *raw_str, struct varchar *result){
    int raw_str_len = strlen(raw_str);
    if (raw_str_len < 1)
        return 0;
    
    char prev_char = raw_str[0];
    int streak = 1;
    char encoded_cell[10];
    for (int i = 1; i < raw_str_len; i++){
        if (raw_str[i] == prev_char){
            streak ++;
        } else{
            int cell_len = format(encoded_cell, prev_char, streak);
            append_nstr(result, encoded_cell, cell_len);
            printf("cell: %s\n", encoded_cell);
            prev_char = raw_str[i];            
            streak = 1;
        }
    }
    int cell_len = format(encoded_cell, prev_char, streak);
    append_nstr(result, encoded_cell, cell_len);
    return 1;
}

int main(){
    struct varchar *vc = malloc(sizeof(struct varchar));
    vc->content = malloc(sizeof(char));
    vc->content[0] = '\0';
    vc->length = 1;

    char *str1 = "a";
    encode(str1, vc);
    printf("Before : %s\n", str1);
    printf("After  : %s\n", vc->content);

    
}
