#include <cstdio>

int main(){
    int max = -1;
    int maxDay;
    int a, b;

    for (int i=1; i<=7; i++){
        scanf("%d %d",&a,&b);
        if((a+b)>max) {
            max = a+b;
            maxDay = i;
        }
    }

    printf("%d",maxDay);
    return 0;
}
