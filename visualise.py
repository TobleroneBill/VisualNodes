import DataStruct

import pygame
import sys
import random

pygame.init()
font = pygame.font.Font(None,70)

# Mouse settings
mousePrev = None
mouseDelta = [0,0]
mouseSelected = False

# Default Node settings
NodeScale = 1
NodeRect = pygame.Rect(0,0,100,100)

# Colors for interaction
Colors = (

(213, 210, 189),    # White
(26, 22, 23),       # Black
(121, 125, 108),    # Grey

(189, 117, 82),     # Orange
(164, 89, 65),      # Wierd Red
(98, 97, 74),       # Brown
(201, 56, 29),      # Red

(57, 129, 90),      # Dark Green
(172, 186, 148),    # Bright Green
)

# Colors for the tops of nodes
RandomColors = (
(74, 109, 82),
(49, 93, 57),
(41, 97, 74),
(41, 93, 74),
(205, 76, 32),
(246, 186, 74),
(24, 80, 49),
(8, 56, 24),
(49, 109, 82),
(238, 186, 90),
(24, 76, 32),
(205, 72, 32),
(213, 60, 24),
(32, 80, 41),
(24, 68, 41),
(8, 52, 24),
(222, 190, 98),
(213, 170, 82),
(189, 52, 24),
(82, 113, 90),
(238, 186, 82),
(82, 125, 98),
(230, 170, 74),
(238, 178, 49),
(49, 101, 65),
(180, 52, 16),
(189, 48, 16),
(222, 186, 98),
(0, 48, 24),
(49, 97, 74),
(230, 178, 90),
(82, 121, 98),
(82, 117, 98),
(230, 190, 98),
(57, 121, 82),
(213, 161, 65),
(57, 117, 82),
(49, 85, 57),
(65, 101, 74),
(32, 72, 49),
(205, 56, 16),
(32, 68, 41),
(74, 129, 98),
(0, 44, 16),
(197, 64, 8),
(74, 113, 90),
(222, 186, 90),
(189, 64, 24),
(197, 48, 16),
(222, 170, 74),
(41, 101, 65),
(197, 56, 24),
(213, 165, 57),
(49, 117, 74),
(32, 97, 57),
(32, 101, 65),
(57, 93, 74),
(57, 105, 82),
(230, 170, 57),
(57, 101, 65),
(238, 182, 74),
(189, 60, 24),
(65, 125, 90),
(230, 174, 49),
(49, 113, 82),
(49, 113, 74),
(230, 174, 41),
(57, 97, 65),
(32, 89, 57),
(32, 89, 65),
(197, 52, 24),
(74, 125, 90),
(222, 182, 82),
(32, 93, 65),
(41, 105, 65),
(197, 60, 16),
(238, 190, 90),
(230, 178, 49),
(57, 105, 65),
(65, 109, 74),
(57, 105, 74),
(230, 174, 57),
(65, 109, 82),
(213, 174, 82),
(222, 170, 49),
(57, 101, 74),
(222, 174, 65),
(222, 178, 65),
(41, 97, 57),
(230, 182, 90),
(41, 97, 65),
(41, 105, 74),
(49, 101, 74),
(222, 174, 41),
(49, 105, 74),
(222, 178, 74),
(41, 93, 65),
(230, 182, 82),
(222, 165, 57),
(222, 165, 65),
(41, 89, 57),
(57, 125, 90),
(57, 113, 74),
(57, 113, 82),
(222, 165, 41),
(32, 80, 57),
(230, 174, 74),
(230, 174, 82),
(222, 178, 82),
(65, 133, 90),
(57, 109, 82),
(213, 178, 82),
(222, 178, 57),
(41, 85, 57),
(74, 117, 98),
(213, 174, 74),
(189, 52, 8),
(230, 182, 65),
(65, 125, 82),
(74, 117, 90),
(189, 52, 16),
(57, 113, 90),
(65, 117, 82),
(65, 129, 90),
(222, 178, 90),
(213, 170, 74),
(238, 178, 82),
(230, 182, 98),
(65, 105, 74),
(65, 121, 82),
(65, 105, 82),
(41, 109, 74),
(57, 97, 74),
(8, 60, 32),
(189, 56, 24),
(189, 56, 16),
(32, 93, 57),
(238, 178, 74),
(197, 60, 24),
(213, 170, 65),
(222, 174, 82),
(57, 109, 74),
(205, 48, 16),
(230, 178, 57),
(238, 182, 82),
(230, 170, 49),
(230, 170, 41),
(41, 93, 57),
(189, 60, 16),
(222, 170, 65),
(49, 101, 82),
(222, 165, 49),
(41, 89, 65),
(49, 97, 57),
(197, 64, 24),
(222, 170, 57),
(222, 182, 74),
(41, 85, 49),
(222, 174, 49),
(65, 117, 90),
(222, 174, 57),
(197, 56, 16),
(197, 56, 8),
(41, 109, 65),
(222, 182, 90),
(230, 178, 74),
(49, 109, 74),
(230, 178, 65),
(238, 178, 65),
(197, 52, 16),
(74, 121, 90),
(222, 170, 41),
(238, 190, 98),
(222, 174, 90),
(49, 105, 65),
(230, 186, 82),
(57, 125, 82),
(49, 97, 65),
(65, 113, 90),
(230, 174, 65),
(65, 113, 82),
(57, 117, 90),
(230, 178, 82),
(65, 121, 90),
(74, 125, 98),
(205, 52, 16),
(32, 85, 57),
(74, 121, 98),
(16, 60, 32),
(222, 174, 74),
(230, 182, 74),
(65, 109, 90),
(230, 170, 65),
(49, 109, 65),
(197, 68, 32),
(180, 60, 16),
(197, 68, 24)
)

# Calculates mouse movement
def MouseCheck():
    global mouseDelta,mousePrev
    if mousePrev == None:
        mousePrev = pygame.mouse.get_pos()
    elif pygame.mouse.get_pos() != mousePrev:
        mouseDelta = [pygame.mouse.get_pos()[0] - mousePrev[0],pygame.mouse.get_pos()[1] - mousePrev[1]]
        mousePrev = pygame.mouse.get_pos()
    else:
        mouseDelta = [0,0]

# Keeps track of:
#   - Things selected
#   - Data structures
#   - BG settings
#
class LevelManager:
    def __init__(self,DataStruct):
        # Pygame stuff
        self.width = 960
        self.height = 540
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Nodes Testing")
        self.clock = pygame.time.Clock()

        # Data stuff
        self.data = DataStruct  # Holds the actual Data structure info
        self.visData = self.GenerateVis()         # Holds the visual representations of those data structures

        # Gameplay stuff
        self.selected = None

    #/________________________/Setup Methods/________________________/
    def GenerateVis(self):
        visnodes = []
        x,y = 0,0
        # loop through any data type given in instructor - Node, linked list etc.
        for index,ClassName in enumerate(list(self.data)):
            # print((type(ClassName)))
            match type(ClassName):
                # Single Node
                case DataStruct.Node:
                    visnodes.append(VisNode(self.data[index],(random.randint(0,self.width-100),random.randint(0,self.height-100))))
                case DataStruct.LinkedList:
                    pass
            y += 100
        return visnodes

    #/________________________/Update Methods/________________________/
    def GameLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

                #BG
                self.screen.fill(Colors[6])
                pygame.draw.rect(self.screen,(57, 129, 90),(10,10,self.width-20,self.height-20))
                # Draw Nodes
                self.Draw()


                pygame.display.flip()
                self.clock.tick(60)
    
    def Draw(self):
        MouseCheck()
        for node in self.visData:
            node.Update(self.screen)


class VisNode:
    """
    Visual Repesentation of nodes
    """

    def __init__(self, Node, Vector2D) -> None:
        self.node = Node
        self.sizeY = NodeRect.height * NodeScale    # will increase based on if it has many pointers
        self.rect = pygame.Rect(Vector2D[0],Vector2D[1],NodeRect.width,self.sizeY)
        self.surface = pygame.surface.Surface((100,self.sizeY))
        
        self.value = f'{self.node.value}'
        self.ptr = f'{self.node.ptr}'

        self.pressed = False
        self.color = random.choice(RandomColors)

    def Draw(self, Screen):
        
        # Node Base 
        self.surface.fill(Colors[0])    # Bottom Half
        pygame.draw.rect(self.surface,self.color,(0,0,100,100//2))          # Top half
        pygame.draw.rect(self.surface,Colors[1],(0,0,100,self.sizeY),5)     # border
        
        # Render Text
        self.surface.blit(font.render(self.value,False,Colors[1]),(37,4))    # Value
        # self.surface.blit(font.render(self.ptr,False,Colors[1]),(37,4))    # Ptr

        Screen.blit(self.surface,self.rect)
    
    def Update(self,Screen):
        self.Move()
        self.Draw(Screen)

    # will move to mouse pos
    # Issue with ordering - need a system to differentiate whats on top
    def Move(self):
        global mousePrev, mouseDelta

        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed() == (1,0,0):
            self.pressed = True

        if self.pressed:
            self.surface.set_alpha(128)
            self.rect.x += mouseDelta[0]
            self.rect.y += mouseDelta[1]
            if pygame.mouse.get_pressed() != (1,0,0):
                self.pressed = False

        else:
            self.surface.set_alpha(256)
        
        return self.pressed
