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
    /*Node* head = createNode(1);
    Node* neck = createNode(7);
    Node* tip = createNode(5);
    Node* end = createNode(56);
    head->nextptr = neck;
    neck->nextptr = tip;
    //head = appendNode(neck, head);
    //head = appendNode(tip, head);
    //head = appendNode(head, tip);
    
    //printf("%d\n", head->val);
    printList(head);
    //printf("%d\n", 5);
    return(0);
    */
   Node* neck = createNode(1);
   Node* head = createNode(2);
   head = appendNode(head, neck);
   return(0);

}
// Function that returns the pointer of the newly, created node (works)
Node* createNode(int a) {
    Node* nodee;
    nodee = (Node*) malloc(sizeof(Node));
    nodee->val = a;
    nodee->nextptr = NULL;
    return(nodee);
}

/*// Function that appends a node to the end of a singly linked list
Node* appendNode(Node* addedNode, Node* headList) {
    Node* copy = createNode(1);
    copy->nextptr = headList;
    
    //Traverse through the linked list
    while (headList != NULL) {
        headList = headList->nextptr;
    }

    // Set the final node to point to the addedNode
    headList->nextptr = addedNode;
    copy = copy->nextptr;
    return copy;
}*/

Node* appendNode(Node* headNode, Node* newNode) {
    Node* copy = createNode(1);
    copy->nextptr = headNode;
    printf("%d", copy->val);
    
    //Traverse the linked list
    while (headNode != NULL) {
        printf("%d\n", headNode->val);
        headNode = headNode->nextptr;
    }

    // Set final boi in the linkedlist to point to the new node
    headNode->nextptr = newNode;
    
    //Go from the copy to the headNode
    copy = copy->nextptr;
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

// Function that prints out the linked list (works)
void printList(Node* listStart) {
    while (listStart != NULL) {
        printf("%d\n", listStart->val);
        listStart = listStart->nextptr;
    }
}

// Right now the problem is with appendNode