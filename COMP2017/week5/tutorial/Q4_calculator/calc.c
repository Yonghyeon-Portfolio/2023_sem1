#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define WARN (1)

typedef int (*calc)(int, int);

int prev_result = 0;
int oprs_performed = 0;

int get_num_input(int *num){
    char num_str[13];
    if (scanf("%13s", num_str) != 1){
        if (WARN) 
            printf("Error: Scanning from stdin failed\n");
        return 0;
    }
    if (!strcmp(num_str, "%")){
        if (oprs_performed == 0){
            if (WARN)
                printf("Error: previous result does not exist: %s\n", num_str);
            return 0;
        }
        *num = prev_result;
        return 1;
    }
    char *end_ptr;
    *num = strtol(num_str, &end_ptr, 10);
    if (*end_ptr != '\0'){
        if (WARN)
            printf("Error: casting to integer failed: %s -> %d\n", num_str, *num);
        return 0;
    }
    return 1;
}

struct operation{
    int a;
    int b;
    calc opr_func;
};

int oadd(int a, int b){
    prev_result = a + b;
    oprs_performed += 1;
    return prev_result;
}
int osub(int a, int b){
    prev_result = a - b;
    oprs_performed += 1;
    return prev_result;
}
int omul(int a, int b){
    prev_result = a * b;
    oprs_performed += 1;
    return prev_result;
}
int odiv(int a, int b){
    prev_result = a / b;
    oprs_performed += 1;
    return prev_result;
}

int get_oprline(struct operation *o){
    int n1, n2;
    char opr_name[4];

    int s1, s2, s3;
    s1 = scanf("%4s", opr_name) == 1;
    s2 = get_num_input(&n1);
    s3 = get_num_input(&n2);
    if (!(s1 && s2 && s3)){
        return 0;
    }

    o->a = n1;
    o->b = n2;

    if (!strcmp(opr_name, "ADD"))
        o->opr_func = oadd;
    else if (!strcmp(opr_name, "SUB"))
        o->opr_func = osub;
    else if (!strcmp(opr_name, "MUL"))
        o->opr_func = omul;
    else if (!strcmp(opr_name, "DIV"))
        o->opr_func = odiv;
    else{
        if (WARN)
            printf("Error: operand <%s> does not exist\n", opr_name);
        return 0;
    }
    return 1;
}

int main(){
    struct operation o;
    while (1){
        if (!get_oprline(&o))
            continue;
        printf("%d\n", o.opr_func(o.a, o.b));
    }
}