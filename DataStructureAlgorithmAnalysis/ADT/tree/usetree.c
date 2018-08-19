#include<stdio.h>

#include "tree.h"

int main(int argv, char * agrc[])
{
    Tree ptree;
    InitializeTree(&ptree);    
    Item it = 5;
    Item it2 = 3;
    Item it3 = 6;

    AddItem(&it, &ptree);
    AddItem(&it2, &ptree);
    AddItem(&it3, &ptree);
    
    printf("%d\n", ptree.size);
    printf("%d", ptree.root->left->item);
}
