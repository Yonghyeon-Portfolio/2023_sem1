#include <stdio.h>

struct BatsmanInfo{
    char first_name[100 + 1];
    char last_name[100 + 1];
    int score;
};

int read_input(struct BatsmanInfo *info){
    if (scanf("%s %s %d", info->first_name, info->last_name, &info->score) == 3)
        return 1;
    return 0;
}

int main(){
    // Get input from stdin
    struct BatsmanInfo batsmen[10];
    int retrived = 0;
    for (int i = 0; i < 10; i++){
        if (!read_input(&batsmen[i]))
            continue;
        retrived++;
    }

    // Format the input and print to stdout
    for (int i = 0; i < retrived; i++){
        printf("%d. %c. %s: ", i+1, batsmen[i].first_name[0], batsmen[i].last_name);
        if (batsmen[i].score <= 0)
            printf("Duck\n");
        else
            printf("%d\n", batsmen[i].score);
    }
    return 1;
}