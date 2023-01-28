class node:
    def __init__(self, val, next=None, prev=None):
        self.prevNode = prev
        self.nextNode = next
        self.val = val
        
        if val == None: self.empty = True
        else: self.empty = False
    
    def updateNode(self, val, next, prev):
        self.prevNode = prev
        self.nextNode = next
        self.val = val

    def pushFwd(self):
        self.nextNode.val = self.val
        self.val = 0

        if not self.nextNode.isempty():
            self.nextNode.pushFwd()

    def pushBck(self):
        self.prevNode.val = self.val
        self.val = 0

        if not self.prevNode.isempty():
            self.prevNode.pushBck()
    

    """ Inputs: node
        Ouputs: - True (the class is empty)
                - False (the class is not empty) """
    def isempty(self):
        if (self.val == 0) or (self.nextNode == None) or (self.nextNode == None):
            return True
        else:
            return False

if __name__ == "__main__":
    node1 = node(1)
    node2 = node(2, prev=node1)
    node3 = node(3, next=node1, prev=node2)

    print("The first node value is " + str(node1.val))
    print("The first node, accessed from the second is " + str(node2.prevNode.val))


