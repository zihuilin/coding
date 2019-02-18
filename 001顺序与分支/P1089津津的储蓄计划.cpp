#include <cstdio>

int main(int argc, char** argv){

#ifdef DEBUG
    if(argc<2 || NULL == freopen(argv[1],"r",stdin)) {
        printf("can't open file\n");
        return -1;
    }
#endif
    int monthIndex = -1;
    int remain = 0;
    int deposit = 0;
    int b;
    for (int i=1; i<=12; i++){
        remain += 300;
        scanf("%d",&b);
        //printf("%d,%d",remain,b);
        if (monthIndex == -1 && b > remain) monthIndex = i;
        remain -= b;
        while (remain>100) {
            remain -= 100;
            deposit += 100;
        //printf(",%d",deposit);
        }
        //printf("\n");
    }
    if (monthIndex != -1)
        printf("-%d",monthIndex);
    else
        printf("%d",remain + (deposit*120)/100);
    return 0;

}
