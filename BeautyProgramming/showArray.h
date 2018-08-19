#include <stdio.h>
void showArray(int cakes[], int length)
{
    int i;
    for(i=0;i<length;i++)
        printf("%d ",cakes[i]);
    putchar('\n');
}
