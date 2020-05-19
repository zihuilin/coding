#include <stdio.h>

int main(){
    printf("六一，你想得到什么礼物？\n");
    printf("a:乐高;b:飞机；c:娃娃；d：好吃的\n");
    char r;
    scanf("%c", &r);
    switch (r){
        case 'a':
            printf("你选了乐高！\n");
            break;
        case 'b':
            printf("你选了飞机！\n");
            break;
        case 'c':
            printf("你选了娃娃！\n");
            break;
        case 'd':
            printf("你选了好吃的！\n");
            break;
        default:
            printf("你输入的选项不对！\n");
    }
    /*
    if (r == 'a'){
        printf("你选了乐高！\n");
    } else if (r == 'b'){
        printf("你选了飞机！\n");
    } else if (r == 'c'){
        printf("你选了娃娃！\n");
    } else {
        printf("你选了好吃的！\n");
    }
    */
    return 0;
}
