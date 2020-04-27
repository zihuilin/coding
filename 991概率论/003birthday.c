#include <stdio.h>

int main(){
    int n = 1;
    double p = 1;
    int day = 365;
    while (p > 0.5){
        day = 365 - n;
        p = p * day / 365;
        n++;
        printf("%d : %f\n", n, p);
    }
}
