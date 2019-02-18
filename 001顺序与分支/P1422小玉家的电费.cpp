#include <cstdio>

int main(){
    int c;
    float b150 = 0.4463;
    float a150 = 0.4663;
    float a400 = 0.5663;
    
    scanf("%d",&c);

    float answer = c>400 ? a400*(c-400) : 0;

    c= c>400 ? 400 : c;
    answer += c>150 ? a150*(c-150) : 0;

    c= c>150 ? 150 : c;
    answer += c*b150;

    printf("%.1f",answer);
    return 0;
}
