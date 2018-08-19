//#pragma c9x on
#ifndef _QUEUE_H_
#define _QUEUE_H_
#include<stdbool.h>

typedef int Item;

#define MAXQUEUE 10
typedef struct node{
    Item item;
    struct node * next;
} Node;

typedef struct queue{
    Node * front;
    Node * rear;
    int items;
} Queue;

/*function:initial the function
 *pre     : pg is point to the queue
 *after   : the queue is initial empoty queue
 */
void InitializeQueue(Queue * pg);

/*function:check the memory is full?
 *pre     : pg is point to the queue
 *after   : the queue is full return true
 */
bool QueueIsFull(const Queue * pg);

/*function: check the queue is empty 
 *pre     : pg is point to the queue
 *after   : the queue is empty return true
 */
bool QueueIsEmpty(const Queue * pg);

/*function: add a item at end of queue
 *pre     : pg is point to the queue
 *after   : the queue is initial empoty queue
 */
bool EnItem(Item item, Queue * pg);

/*function: delete a item at front of queue
 *pre     : pg is point to the queue
 *after   : the queue is initial empoty queue
 */
bool DeItem(Item * pitem, Queue * pg);

void QueueItemCount(const Queue * pg);
 
void EmptyTheQueue(Queue * pg);

#endif
