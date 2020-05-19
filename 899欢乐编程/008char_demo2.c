#include <stdio.h>

int main(){
    printf("你是不是学生?（是回复y，不是回复n）\n");
    char r;
    scanf("%c", &r);
    if (r == 'y'){
        printf("你好，学生！\n");
    }else {
        printf("哦，你不是学生哟！\n");
    }
    return 0;
}
