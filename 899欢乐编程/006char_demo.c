#include <stdio.h>

int main(){
    char c;  //声明了一个字符变量c
    c = 'c'; //将字符'c'存放到变量c里
    printf("%c\n", c); //输出变量c的值
    
    int i = c; //将c的ASCII码值放到i里
    printf("%d\n", i);

    c = i + 3; //i+3: i后面再数3个字符
    printf("%c\n", c); //输出变量c的值

    printf("%d\n", c); //输出变量c的值

    return 0;
}
