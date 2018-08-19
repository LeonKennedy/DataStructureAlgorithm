#include<stdio.h>
//#include "queue.h"
#include "queuebyarray.h"
int main(int argv, char * arvc[])
{
//    Queue line;
//    InitializeQueue(&line);
    Queue * pqueue;
    pqueue = createQueue(5);
    disposeQueue(pqueue);
    return 0;
}
