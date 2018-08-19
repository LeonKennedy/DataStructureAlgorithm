#include <stdio.h>
#include <stdlib.h>
#include "showArray.h"
void showArray(int[], int);
void createSituation(int situation[] ,  int length)
{
    int i;
    for(i = 0; i<length;i++){
        situation[i] = rand()%10;
    }
    situation[0] = 0;
}

int main(void)
{
    const int n =10;
    int situation[n];
    createSituation(situation,n);
    showArray(situation,n);
    int i;

    int minFloor = 0;
    int minCountFloor=0;
    int n1,n2,n3;
    for(n1=0,n2=situation[0],n3=0,i=1;i<n;i++){
        n3 +=situation[i];
        minCountFloor += i * situation[i];
    }
    for(i = 1; i < n; i++){
        if( n1 + n2 < n3){
            minFloor = i;
            minCountFloor += (n1 + n2 - n3);
            n1 += n2;
            n2 = situation[i];
            n3 -= n2;
        }
        else
            break;
    }
    printf("The best floor is %d, account is %d.\n",minFloor, minCountFloor);
    return 0;
}
