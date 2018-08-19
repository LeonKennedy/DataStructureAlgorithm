#include<stdio.h>
#include<stdlib.h>
#include "queue.h"

void InitializeQueue(Queue * pg)
{
    pg->front = NULL;
    pg->rear = NULL;
    pg->items = 0;
}

bool QueueIsFull(const Queue * pg)
{
    return pg->items == MAXQUEUE;
}

bool QueueIsEmpty(const Queue * pg)
{
    return pg->items == 0;
}

bool EnItem(Item item, Queue * pg)
{
    Node * pn;
    pn = (Node *)malloc(sizeof(Node));
    if(pn == NULL){
        fprintf(stderr, "Unable to allocate memory!\n");
        exit(1);
    }
     
    pn->item = item;
    if(QueueIsEmpty(pg)){
        pg->front = pg->rear = pn;
    }

    pg->rear = pn;
    pn->next = pg->front;
    pg->items++;
    return true;
}

bool DeItem(Item * pitem, Queue * pg)
{
    Node * pn;
    if(QueueIsEmpty(pg))
        return false;
    pn = pg->front;
    pg->front = pg->front->next;
    free(pn);
    pg->items--;

    if(pg->items == 0)
        pg->rear = NULL;
    return true;
}

void EmptyTheQueue(Queue * pg)
{
    Item dummy;
    while(!QueueIsEmpty(pg))
        DeItem(&dummy, pg);
}

