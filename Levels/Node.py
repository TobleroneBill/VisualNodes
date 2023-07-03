import os
import sys
sys.path.append(os.getcwd())    # needed to get modules
from DataStruct import Node, LinkedList
from visualise import VisNode, MouseCheck, LevelManager

import pygame
import random

pygame.init()


#/__________________________/NODES/__________________________/
# Individual
# node = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)

# node.set_next(node2)
# node.set_next(node3)
# node.set_next(node4)
# # node.set_next(Node(100))
# # node.set_next(Node(200))

# nodes = [node,node2,node3,node4]


#Linked List
A = LinkedList()
A.append(1)
A.append(2)
A.append(3)
A.append(4)

A.insert(123,0)

B = LinkedList()
B.append(1)
B.append(2)
B.append(3)
B.append(4)

B.insert(123,1)

C = LinkedList()
C.append(1)
C.append(2)
C.append(3)
C.append(4)

C.insert(123,2)

D = LinkedList()
D.append(1)
D.append(2)
D.append(3)
D.append(4)

D.insert(123,3)

E = LinkedList()
E.append(1)
E.append(2)
E.append(3)
E.append(4)

E.insert(123,4)

F = LinkedList()
F.append(1)
F.append(2)
F.append(3)
F.append(4)

F.insert(123,5)

# Levels can have any amount of Data structures, and it will generate the appropriate visnodes based on regular nodes used
# level = LevelManager((node,node2,node3,node4,1),'Node Testing')
level = LevelManager([D,E],'Node Testing')


level.GameLoop()