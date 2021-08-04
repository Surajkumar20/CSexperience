#include <iostream>
#include <stdlib.h>
#include <cstdlib>
#include <vector>
using namespace std;

// Create a data structure / node
struct Point {
    public:
        int val;
        struct Point *next;
};

// Change the name of the data type
typedef struct Point node;

node* createNode(int);
node* appendNode(node*, node*);
node* makeLinkedList(vector<int>);
void printer(node*);


int main(void) {
    vector<int> v1;
    node* header;
    v1 = {1, 3, 6, 10};
    header = makeLinkedList(v1);
    printer(header);
    
    return 0;
}


// Function to create a node (this function works)
node* createNode(int value) {
    node* temp; 
    temp = (node*) malloc(sizeof(struct Point));
    temp->next = NULL;
    temp->val = value;
    return temp;
}

// Function that can add a node to an existing node (this function works)
node* appendNode(node* head, node* newNode) {
    node* temp = head;

    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;

    return(head);   
}

// Function that will create a linked list, it uses a vector of integers
node* makeLinkedList(vector<int> values) {
    node* head = createNode(values[0]);
    node* temp;
    int length = values.size(); int i = 1;

    while (i < length) {
        temp = createNode(values[i]);
        head = appendNode(head, temp);
        i += 1;
    }

    return(head);
}

// Function that prints out the linked list (this function works)
void printer(node* Head) {
    node* temp = createNode(0);
    temp = Head;

    while (temp != NULL) {
        cout << "The value is " << temp->val << endl;
        temp = temp -> next;
    }
}


