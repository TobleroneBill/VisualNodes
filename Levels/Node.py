import os
import sys
sys.path.append(os.getcwd())    # needed to get modules
from DataStruct import Node, LinkedList
from visualise import VisNode, MouseCheck, LevelManager

import pygame
import random

pygame.init()


node = Node(1)
visnode = VisNode(node,(100,100))
node2 = Node(3)
node2.ptr = node
visnod2 = VisNode(node2,(100+100,100))

ListTest = LinkedList()
for i in range(10):
    ListTest.append(random.randint(10,100))

ListTest.printNodes()
print(f'Size: {ListTest.size}')

level = LevelManager((node,node2,ListTest),'Node Testing')

level.GameLoop()