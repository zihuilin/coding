#include <stdio.h>

int comb(int n, int r){
    if (n==r || r==0)
        return 1;
    else
        return comb(n-1, r-1) + comb(n-1, r);
}

int main(){
    int n = 5;
    int r = 3;

    /*
    int res = 1;
    for (int i=n; i>(n-r); i--)
        res = res * i;

    for (int i=1; i<=r; i++)
        res = res / i;
        */
    int res = comb(n, r);

    printf("%d\n", res);
    return 0;
}
