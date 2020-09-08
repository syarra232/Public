#include <stdio.h>
#include <stdlib.h>

typedef struct _node{
    int data;
    struct node *next;
}node;

void print_list(node *n);
void get_mid(node *h);

int main(void) {
    node *h = NULL;
    for(int i = 0; i < 9; i++) {
        if(h == NULL){
            h = (node *)malloc(sizeof(node));
            h->data = i+1;
            h->next = NULL;
        }
        else {
            node *t = h;
            while(t->next != NULL)
                t = t->next;
            node *n = (node *)malloc(sizeof(node));
            n->data = i+1;
            n->next = NULL;
            t->next = n;
        }
    }
    print_list(h);
    get_mid(h);
    return 0;
}


void print_list(node *n)
{
    while(n != NULL) {
        printf("%d ", n->data);
        n = n->next;
    }
    printf("\n");
}

void get_mid(node *h)
{
    node *s = h, *f = h;
    node *p = NULL;
    while(f && f->next){
        p = s;
        s = s->next;
        f = f->next;
        f = f->next;
        if(f == NULL){
            printf("\nEVEN num of nodes");
            printf("\n MID = %d %d",p->data, s->data);
        }
        else if(f->next == NULL) {
            printf("\nODD num of nodes");
            printf("\n MID = %d",s->data);
        }
    }
}
