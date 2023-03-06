#include <stdio.h>

int atoi(const char s[]){
    int total = 0;
    int num;
    int inverse = 0;
    for (int i = 0; s[i] != 0; i++){
        num = s[i] - 48;
        if (num == -3)
            inverse = 1;
        else
            total = total * 10 + (s[i]-48);
    }
    if (inverse)
        return total * -1;
    return total;
}

int main(){
    int res = atoi("-45602");
    res = atoi("");
    printf("%d\n", res);
    return 0;
}