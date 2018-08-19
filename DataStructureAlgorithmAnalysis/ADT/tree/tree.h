#ifndef _TREE_H_
#define _TREE_H_
#include<stdbool.h>

#define MAXITEM 20

typedef int Item;
typedef struct node{
    Item item;
    struct node * left;
    struct node * right;
} Node;

typedef struct tree{
    Node * root;
    int size;
} Tree;

void InitializeTree(Tree * ptree);

bool TreeIsEmpty(const Tree * ptree);

bool TreeIsFull(const Tree * ptree);

int TreeItemCount(const Tree * ptree);

bool AddItem(const Item * pi, Tree * ptree);

bool InTree(const Item * pi, Tree * ptree);

bool DeleteItem(const Item * pi, Tree * ptree);

void Traverse(const Tree * ptree, void (* fun)(Item item));

void DeleteAll(Tree * ptree);

#endif
