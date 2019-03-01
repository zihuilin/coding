#include <cstdio>

const int MAXN = 100;
int a[MAXN];
int top = -1;

void push (int e)
{
    if(top >= MAXN)
        printf("Stack overflow in push()");
    top++;
    a[top] = e;
}

bool isEmpty()
{
    if(top==-1)
        return true;
    else
        return false;
}

int peak()
{
    if(isEmpty())
        printf("Stack underflow in top()");
    return a[top];
}

int pop()
{
    if(isEmpty())
        printf("Stack underflow in pop()");
    return a[top--];
}

int main()
{
    push(5);
    push(3);
    printf("%d\n",peak());
    printf("%d\n",pop());
    printf("%d\n",pop());

    return 0;
}
