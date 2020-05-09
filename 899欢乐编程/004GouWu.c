#include <stdio.h>

int main(){
    int a, b;
    float c;
    scanf("%d%d", &a, &b);
    if (a>=6 || b>=200) {
        c = b * 0.9;
    }else {
        c = b; //不能打折
    }
    printf("%.2f", c);
    return 0;
}
