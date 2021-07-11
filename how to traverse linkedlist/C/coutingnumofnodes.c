#include <stdlib.h>
#include <stdio.h>

struct node {
    int val;
    struct node* nextptr;
};
typedef struct node Node;

Node* createNode(int);
Node* appendNode(Node*, Node*);
Node* createList(int []);
void printList(Node*);
int length(int []);

int main(void) {
    int array[5] = {1,2,3,4,5};
    Node* head = createList(array);
    printList(head);
    return(0);
}
// Function that returns the pointer of the newly, created node
Node* createNode(int a) {
    Node* nodee;
    nodee = (Node*) malloc(sizeof(Node));
    nodee->val = a;
    nodee->nextptr = NULL;
    return(nodee);
}

// Function that appends a node to the end of a singly linked list
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

// Function to show that the two above functions work
void printList(Node* listStart) {
    while (listStart->nextptr != NULL) {
        printf("%d\n", listStart->val);
    }
}

// Function that creates a linked list from an array input of integers and number of nodes wanted
Node* createList(int a[]) {
    int len = length(a);
    Node* header = createNode(a[0]);
    int i;

    for (i = 1; i < len; i++) {
        Node* temp = createNode(a[i]);
        header = appendNode(temp, header);
    }

    return(header);
}

// Function that returns length of an integer array
int length(int a[]) {
    int i = 0;

    while (a[i] != NULL) {
        i++;
    }
    return(i + 1);
}
