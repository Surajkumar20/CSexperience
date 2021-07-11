#include <stdlib.h>
#include <stdio.h>

Node* createNode(int);
Node* appendNode(Node*, Node*);

struct node {
    int val;
    struct node* nextptr;
};
typedef struct node Node;

// Function that returns the pointer of the newly, created node
Node* createNode(int a) {
    Node* nodee;
    nodee = (Node*) malloc(sizeof(Node));
    nodee->val = a;
    nodee->nextptr = NULL;
    return(nodee);
}

// Function that appends a node to a singly linked list
Node* appendNode(Node* addedNode, Node* headList) {
    Node* copy = headList;
    
    //Traverse through the linked list
    while (headList != NULL) {
        headList = headList->nextptr;
    }

    // Set the final node to point to the addedNode
    headList->nextptr = addedNode;
    return copy;
}