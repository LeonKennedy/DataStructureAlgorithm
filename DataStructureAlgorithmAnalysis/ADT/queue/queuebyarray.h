#ifndef _QUEUEBYARRAY_H
#define _QUEUEBYARRAY_H

typedef int Element;

struct QueueRecord
{
    int capacity;
    int front;
    int rear;
    int size;
    Element * array;
};

typedef struct QueueRecord Queue;

int isEmpty(Queue *q);
int isFull(Queue *q);
Queue* createQueue(int MaxElements);
void makeEmpty(Queue *q);
void enterQueue(Element x, Queue *q);
void disposeQueue(Queue *q);
void deQueue(Queue *q);

#endif
