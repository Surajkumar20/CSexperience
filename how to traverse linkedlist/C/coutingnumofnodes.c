#include <stdlib.h>
#include <stdio.h>
#define LEN 5

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
    int array[LEN] = {1,2,3,4,5};
    //Node* head = createList(array);
    Node* head;
    Node* neck;
    Node* tip;
    head->val = 1; 
    head->nextptr = neck;
    neck->val = 2; 
    neck->nextptr = tip;
    tip->val = 3;
    tip->nextptr = NULL; 
    
    printf("%d\n", neck->val);
    printList(head);
    printf("%d\n", 5);
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

// Function that creates a linked list from an array input of integers and number of nodes wanted
Node* createList(int a[]) {
    int len = LEN;
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

    while (a[i] < 100) {
        i++;
    }
    return(i + 1);
}

// Function that prints out the linked list
void printList(Node* listStart) {
    while (listStart->nextptr != NULL) {
        printf("%d\n", listStart->val);
        listStart = listStart->nextptr;
    }
}
