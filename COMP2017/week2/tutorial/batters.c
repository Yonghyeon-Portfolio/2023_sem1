#include <stdio.h>

int main(){
    char firstname[63];
    char lastname[63];
    int score;
    for (int i = 1; i <= 10; i++){
        scanf("%s %s %d", firstname, lastname, &score);
        if (score == 0)
            printf("%d. %c. %s: Duck\n", i, firstname[0], lastname);
        else
            printf("%d. %c. %s: %d\n", i, firstname[0], lastname, score);
    }
}