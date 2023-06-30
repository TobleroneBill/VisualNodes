import os
import sys
sys.path.append(os.getcwd())    # needed to get modules
from DataStruct import Node, LinkedList
from visualise import VisNode, MouseCheck, LevelManager

import pygame
import sys




pygame.init()


node = Node(1)
visnode = VisNode(node,(100,100))

node2 = Node(3)
visnod2 = VisNode(node2,(100+100,100))

level = LevelManager([node,node2])

level.GameLoop()