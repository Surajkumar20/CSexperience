class node:
    def __init__(self, val=0, nNode=None, name="Suraj") -> None:
        self.nextNode = nNode
        self.val = val
        self.name = name

    def point(self, pointedNode):
        self.nextNode = pointedNode
        pointedNode.nextNode = self

if __name__ == "__main__":
    node1 = node(1, name="Ranjan")
    node2 = node(2, name="Suraj")
    node1.point(node2)

    print("The {} node is pointing to {}".format(node1.name, node1.nextNode.name))
    print("The {} node is pointing to {}".format(node2.name, node2.nextNode.name))
