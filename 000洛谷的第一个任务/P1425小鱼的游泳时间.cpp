#include <cstdio>

int main(){
	int a,b,c,d,e,f;
	scanf("%d %d %d %d",&a,&b,&c,&d);
	f=(60*c+d)-(60*a+b);
	e=f/60;
	f=f%60;
	printf("%d %d",e,f);
	return 0;
}
