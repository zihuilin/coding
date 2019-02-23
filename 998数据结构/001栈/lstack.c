#include <stdio.h>
#include <stdlib.h>

typedef enum {
    false,
    true
}bool;

struct elem {
    int d;
    struct elem* next;
};
struct elem* top = NULL;

bool isEmpty(){
    if (top == NULL)
        return true;
    else
        return false;
}

void push(int d){
    struct elem* e = malloc(sizeof(struct elem));
    e->d = d;
    if (isEmpty()){
        e->next = NULL;
   } else {
        e->next = top;
   }
    top = e;
}

int* peak(){
    if(isEmpty())
       return NULL;
    else
        return = top->d;
}

void pop(int* e){
    if(isEmpty())
        e = NULL;
    else {
        *e = top->d;
        top = top->next;
    }
}

int main() {

    push(5);
    push(3);
    int* d = malloc(sizeof(int));
    peak(d);
    if (d != NULL)
        printf("%d\n",*d);
    pop(d);
    if (d != NULL)
        printf("%d\n",*d);
    pop(d);
    if (d != NULL)
        printf("%d\n",*d);
    pop(d);
    if (d != NULL)
        printf("%d\n",*d);
}
