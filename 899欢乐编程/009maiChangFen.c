#include <stdio.h>

int main(){
    printf("肠粉6元一条，要几条？\n");
    int a;
    scanf("%d", &a);
    float money = a * 6;
    printf("请问是不是学生？(是回复y，不是回复n)\n");

    char r;
    scanf(" %c", &r);
    if (r == 'y')
        money = money * 0.88;
    printf("请问是不是VIP？(是回复y，不是回复n)\n");
    scanf(" %c", &r);
    if (r == 'y')
        money = money * 0.98;

    printf("你要付%.2f元。\n", money);
    
    return 0;
}
