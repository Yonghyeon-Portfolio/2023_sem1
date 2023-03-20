#include <stdio.h>
#include <stdbool.h>

int main(){
    bool p = true;
    bool q = false;
    printf("p = %d, q = %d\n", p, q); // false
    printf("p and q = %d\n", p && q); // false
    printf("p or q = %d\n", p || q); // true
    printf("p and not q = %d\n", p && !q); // true
    printf("not p or q = %d\n", !p || q); // false

}