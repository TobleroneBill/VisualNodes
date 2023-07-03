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
node = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node.set_next(node2)
node.set_next(node3)
node.set_next(node4)

nodes = [node,node2,node3,node4]


#Linked List
ListTest = LinkedList()
for i in range(4):
    ListTest.append(random.randint(10,100))

ListTest.printNodes()
print(f'Size: {ListTest.size}')

# Levels can have any amount of Data structures, and it will generate the appropriate visnodes based on regular nodes used
level = LevelManager((node,node2,node3,node4,ListTest),'Node Testing')

level.GameLoop()