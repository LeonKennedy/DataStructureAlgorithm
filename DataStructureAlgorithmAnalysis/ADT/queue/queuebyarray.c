#include <stdlib.h>
#include "queuebyarray.h"

/*
void makeEmpty(Queue *q);
void enterQueue(Element x, Queue *q);
void deQueue(Queue *q);
*/

int isEmpty(Queue *q)
{
    if (q->size == 0)
        return 0;
    return 1;
}

int isFull(Queue *q)
{
    if (q->size == q->capacity)
        return 0;
    return 1;
}

Queue* createQueue(int MaxElements)
{
    Queue *q;
    q = malloc(sizeof(Queue));
    q->capacity = MaxElements;
    q->front = 1;
    q->rear = 0;
    q->array = (int *)malloc(sizeof(Element) * MaxElements);
    return q;
}

void disposeQueue(Queue *q) {
    free(q->array);
    free(q);
}
