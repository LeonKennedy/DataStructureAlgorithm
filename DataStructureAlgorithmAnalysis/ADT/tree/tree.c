#include<stdlib.h>
#include<stdio.h>
#include "tree.h"
#include<string.h>

static int compareItem(Item * i1, Item * i2);
static void insertNode(Node * pn, Node * root);
static Node* makeNode(const Item * pi);
static void deleteNode(Node * pn, Node ** proot);

void InitializeTree(Tree * ptree)
{
    ptree->root = NULL;
    ptree->size = 0;
}

bool TreeIsEmpty(const Tree * ptree)
{
    return ptree->size == 0;
}

bool TreeIsFull(const Tree * ptree)
{
    return ptree->size == MAXITEM;
}
    

int TreeItemCount(const Tree * ptree)
{
    return ptree->size; 
}

bool AddItem(const Item * pi, Tree * ptree)
{
    if(TreeIsFull(ptree)){
        fprintf(stderr, "The Tree is Full!");
        return false;
    }

    if(false){
        fprintf(stderr, "Add a duplicate item!");
        return false;
    }

    Node * tpt;
    tpt = (Node *)malloc(sizeof(Node));
    if(tpt == NULL)
        return false;
    tpt->item = *pi;
    tpt->left = NULL;
    tpt->right = NULL;

    if(ptree->root == NULL) 
        ptree->root = tpt;
    else
        insertNode(tpt, ptree->root); 
        
    ptree->size++;
    return true;
}

bool InTree(const Item * pi, Tree * ptree)
{

}

bool DeleteItem(const Item * pi, Tree * ptree)
{
    Node * tpt;
    tpt = makeNode(pi);
    if(tpt == NULL)
        return false;
    deleteNode(tpt,&(ptree->root));
}

void Traverse(const Tree * ptree, void (* fun)(Item item))
{
    
}

void DeleteAll(Tree * ptree)
{
    
}

static Node* makeNode(const Item * pi)
{
    Node * tpt;
    tpt = (Node *)malloc(sizeof(Node));
    if(tpt == NULL)
        return NULL;
    tpt->item = *pi;
    tpt->left = NULL;
    tpt->right = NULL;
    return tpt;
}

static void insertNode(Node * pn, Node * root)
{
    int rout;
    rout = compareItem(&(pn->item),&(root->item));
    switch(rout){
        case 1:
            if(root->right == NULL)
                root->right = pn;
            else
                insertNode(pn,root->right);
            break;
        case 0:
            return;
        case -1:
            if(root->left == NULL)
                root->left = pn;
            else
                insertNode(pn, root->left);
            break;
    }
}

static void deleteNode(Node * pn, Node ** proot)
{
    int rout;
    rout = compareItem(&(pn->item), &((*proot)->item));
    switch(rout){
        case 1:
            deleteNode(pn,&((*proot)->right));
            break;
        case 0:
            if((*proot)->left == NULL && (*proot)->right == NULL){
                free(*proot);
                *proot = NULL;
                return;
            }
            Node * troot;
            if((*proot)->left == NULL){
                troot = (*proot)->right;
                free(*proot);
                *proot = troot;
                return;
            }
            if((*proot)->right == NULL){
                troot = (*proot)->left;
                free(*proot);
                *proot = troot;
                return;
            }
            //都有
            insertNode((*proot)->right,(*proot)->left);
            troot = (*proot)->left;
            free(*proot);
            *proot = troot;
            return;
            
        case -1:
            deleteNode(pn,&((*proot)->left));
            break;
    }
}

static int compareItem(Item * i1, Item * i2)
{
    if(*i1 > *i2)
        return 1;
    else if(*i1< *i2)
        return -1;
    return 0;
}

