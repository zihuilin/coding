#include <cstdio>

void permute(char str[], int s, int e)
{
	if (s==e)
	{
		for(int i=0;i<=e;i++) printf("%c",str[i]);
		printf("\n");
	}
	else
	{
		int temp;
		for (int j=s;j<=e;j++)
		{
            temp=str[j];
            for(int k=j;k>s;k--)
                str[k]=str[k-1];
            str[s]=temp;

			permute(str,s+1,e);	
            
            temp=str[s];
            for(int k=s;k<j;k++)
                str[k]=str[k+1];
            str[j]=temp;
		}
	}

}

int main(){
	//char str[3] = {'a','b','c'};
	char str[4] = {'a','b','c','d'};
	permute(str,0,3);
	return 0;
}


