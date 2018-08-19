#include<stdio.h>
#include<stdlib.h>
#include "list.h"


void InitializeList(List * plist)
{
    *plist = NULL;
}

bool ListIsEmpty(List * plist)
{
    if(*plist == NULL)
        return true;
    else
        return false;
}

bool ListIsFull(const List * plist)
{
    List pt;
    bool full;
    pt = (List)malloc(sizeof(Node));
    if(pt == NULL)
        full = false;
    else
        full = true;
    free(pt);
    return full;
}

unsigned int ListItemCount(const List * plist)
{   
    if(*plist == NULL)
        return 0;
    int num = 1;
    List scan = *plist;
    while(scan->next != NULL){
        scan = scan->next;
        num++;
    }
    return num;
}

bool AddItem(Item item, List * plist)
{
    List pnew;
    List scan = *plist;

    pnew = (Node *)malloc(sizeof(Node));
    if (pnew == NULL)
        return false;
    pnew->item = item;
    pnew->next = NULL;
    if (scan == NULL)
       *plist = pnew;
    else{
        while(scan->next != NULL)
            scan = scan->next;
        scan->next = pnew;
    }
    return true;
}

void Traverse(const List * plist, void (* pfun) (Item item))
{
    List pnode = *plist;
    while(pnode != NULL){
        (* pfun)(pnode->item);
        pnode = pnode->next;
    }
}

void EmptyTheList(List * plist)
{
    List psave = *plist;
    while(*plist != NULL){
        psave = (*plist)->next;
        free(*plist);
        *plist = psave;
    }
}
