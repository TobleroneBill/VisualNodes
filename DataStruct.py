
class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.ptr = None
    
    def set_next(self,Node):
        if self.ptr is not None:
            if type(self.ptr) == list:
                self.ptr = self.ptr + [Node]
            else:
                self.ptr = [self.ptr] + [Node]
        else:
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
    

    def insert(self,value,index):
        # head
        if index <= 0:
            next = self.headNode
            self.headNode = Node(value)
            self.headNode.ptr = next
            self.size +=1
            return
        if index > self.size:
            self.append(value)
            return

        # loop to index (will never be OOB)
        ptr = self.headNode
        for i in range(index-1):
            ptr = ptr.ptr
        
        #insert
        insertNode = Node(value)
        insertNode.ptr = ptr.ptr
        ptr.ptr = insertNode



    def printNodes(self):
            node = self.headNode
            while node:
                print(node.value)
                node = node.ptr
