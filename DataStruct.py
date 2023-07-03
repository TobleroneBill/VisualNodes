
class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.ptr = None
    
    def set_next(self,Node):
        self.ptr = Node

class LinkedList:
    def __init__(self,head = None) -> None:
        self.headNode = head
        self.size = 0
    
    # add to end
    def append(self,value):
        if self.headNode == None:
            self.headNode = Node(value)
        else:
            addNode = self.headNode
            while addNode.ptr:
                addNode = addNode.ptr
            addNode.ptr = Node(value)
        self.size +=1

    # Apply function to all nodes
    def iterate(self,func):
        pass

    def printNodes(self):
            node = self.headNode
            while node:
                print(node.value)
                node = node.ptr
