#include <stdio.h>

int main(){
    long a,b,c,zhongjian;
    scanf("%ld%ld%ld", &a, &b, &c);
    if ((b<=a && b>=c)||(b<=c && b>=a)) {
        zhongjian = b;
    } else if ((a<=b && a>=c)||(a<=c && a>=b)){  //判断a是不是中间数
        zhongjian = a;
    } else {
        zhongjian = c;
    }

    printf("%ld\n", zhongjian);
    return 0;
}
