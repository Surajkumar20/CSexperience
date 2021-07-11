#include <iostream>
#include <cstdlib>
using namespace std;

// Create a data structure / node
struct Linkedlist {
    public:
        int val;
        struct nextptr *next;
};

// Change the name of the data type
typedef struct Linkedlist *node;

// Function to create a node
node createNode() {
    node temp; 
    temp = (node) malloc(sizeof(struct Linkedlist));
    temp->next = NULL;
    return temp;
}

// Function that can add a node to an existing node
node addNode(node head, int newvalue) {
    node 
}
