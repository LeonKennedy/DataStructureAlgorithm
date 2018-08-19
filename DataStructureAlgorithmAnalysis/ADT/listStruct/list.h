#ifndef LIST_H_
#define LIST_H_
#include<stdbool.h>  /* C99特性 */

#define TSIZE 45

struct film{
    char title[TSIZE];
    int rating;
};

typedef struct film Item;
typedef struct node{
    Item item;
    struct node * next;
} Node;

typedef Node * List;

/*function: initillize the list
 *pre     : plist point the list
 *after   : list is null
 */
void InitializeList(List * plist);


/*function: check list is emplty
 *pre     : plist point the list
 *after   : full return true, not full return false
 */
bool ListIsEmpty(List * plist);

/*function: check list is full
 *pre     : plist point the list
 *after   : null return true, not null return false
 */
bool ListIsFull(const List * plist);


/*function: count the item
 *pre     : plist point the list
 *after   : return the number of item
 */
unsigned int ListItemCount(const List * plist);

/*function: add item into node
 *pre     : plist point the list
 *after   : if added return ture
 */
bool AddItem(Item item, List * plist);

/*function: 将一个函数作用与列表中每个项目
 *pre     : plist point the list
            pfun point to the function
 *after   : if added return ture
 */
void Traverse(const List * plist, void (* pfun) (Item item));

/*function: free the plist mem
 *pre     : plist point the list
 *after   : free the point mem and plist point null
 */
void EmptyTheList(List * plist);


#endif
