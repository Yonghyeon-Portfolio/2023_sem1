#include <stdio.h>
#include <string.h>

#define GREETING_MAXLEN (16 + 1)
#define NAME_MAXLEN (32 + 1)

int main(int argc, char* argv[]){
    char greeting[GREETING_MAXLEN];
    if (argc == 1){ 
        // no cmd argument is provided (default greeting = Hello)
        strcpy(greeting, "Hello");
    }
    else{ // argc >= 2
        strncpy(greeting, argv[1], GREETING_MAXLEN);
        greeting[GREETING_MAXLEN - 1] = '\0';
    }
    
    printf("What is your name? ");
    char usr_name[NAME_MAXLEN];
    // Get user's name from input, then remove newline
    fgets(usr_name, sizeof(usr_name), stdin);
    int name_len = strlen(usr_name);
    if (usr_name[name_len - 1] == '\n')
        usr_name[name_len - 1] = '\0';
    // Print greeting words
    printf("%s! %s :D\n", greeting, usr_name);
}