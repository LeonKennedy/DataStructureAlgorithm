#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "list.h"

void main(int argc, char * argv[])
{
    
    List start;
    Item temp;
    InitializeList(&start);

    if (ListIsFull(&start)){
        fprintf(stderr, "No memory available!Bye\n");
        exit(1);
    }

    puts("Enter first movies title:");
    while(gets(temp.title) != NULL && temp.title[0] != '\n'){
        puts("Enter your rating <0-10>: ");
        scanf("%d", &temp.rating);
        while(getchar() != '\n')
            continue;
        if(AddItem(temp,&start) == false){
            fprintf(stderr, "Problem allocating memory\n");
            break;
        }

        if(ListIsFull(&start)){
            puts("The list now full.");
            break;
        }
        puts("Enter next movie title (empty line to stop): ");
}
   
    
}
