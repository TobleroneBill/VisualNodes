# /_______________/Graphical representations of Nodes and Data structures/_______________/

import DataStruct
import NodeColors

import pygame
import sys
import random

# Pygame
pygame.init()
font = pygame.font.Font(None,70)
icon = pygame.image.load(r'C:\Users\JOE\Desktop\Visualisations\DataStructs\Assets\Logo.png')

# Mouse settings
mousePrev = None
mouseDelta = [0,0]
mouseSelected = None

CursorImages = {
    'idle': pygame.image.load('Assets\CursorIdle.png'),
    'click': pygame.image.load('Assets\CursorClick.png'),
}

# Default Node settings
NodeScale = 1
NodeRect = pygame.Rect(0,0,100,100)

# Based on 
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


# Calculates mouse movement
def MouseCheck():
    global mouseDelta,mousePrev
    # Update MouseDelta
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

class LevelManager:
    def __init__(self,DataStruct,WinText,debug=True):
        
        # Pygame stuff
        self.width = 960
        self.height = 540
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(WinText)
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.debug = debug
        pygame.mouse.set_visible(False)


        # Data stuff
        self.data = list(DataStruct)  # Holds the actual Data structure info
        self.visData = self.GenerateVis()         # Holds the visual representations of those data structures

        # Gameplay stuff
        self.selected = None
        self.mouseScreen = CursorImages['idle']

    #/________________________/Setup Methods/________________________/
    def GenerateVis(self):
        visnodes = []
        x,y = 0,0
        # print([node.ptr for node in self.data])
        # loop through any data type given in instructor - Node, linked list etc.
        for index,Class in enumerate(list(self.data)):
            print(index,Class)
            match type(Class):
                # Single Node
                case DataStruct.Node:
                    visnodes.append(
                        VisNode(self.data[index],(random.randint(0,self.width-100),random.randint(0,self.height-100),))
                        )
                case DataStruct.LinkedList:
                    ptr = Class.headNode
                    while ptr:
                        visnodes.append(
                        VisNode(ptr,(random.randint(0,self.width-100),random.randint(0,self.height-100)))
                        )
                        ptr = ptr.ptr
            y += 100
        print([node.value for node in visnodes])
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

                self.clock.tick(60)
                if self.debug:
                    fpsText = font.render(f'{int(self.clock.get_fps())}',0,(255,255,255))
                    self.screen.blit(fpsText,(0,0))

                pygame.display.flip()
    
    def Draw(self):
        MouseCheck()
        for node in self.visData:
            node.Update(self.screen)
        # Draw mouse over all
        self.DrawMouse()

    def DrawMouse(self):
        match pygame.mouse.get_pressed():
            case [0,0,0]:
                self.mouseScreen = CursorImages['idle']
            case [1,0,0]:
                self.mouseScreen = CursorImages['click']
        
        self.screen.blit(self.mouseScreen,(
            # mouse coords - half image coords to center
            pygame.mouse.get_pos()[0]-self.mouseScreen.get_width()//2,  
            pygame.mouse.get_pos()[1]-self.mouseScreen.get_height()//2))

class VisNode:
    """
    Visual Repesentation of nodes
    """
    def __init__(self, Node, Vector2D) -> None:
        self.node = Node
        self.sizeY = NodeRect.height * NodeScale    # will increase based on if it has many pointers

        self.value = f'{self.node.value}'
        self.ptrText = None

        if self.node.ptr != None:
            if type(self.node.ptr) == list:
                
                self.sizeY += 50 * (len(self.node.ptr)-1)
            else:
                self.ptrText = f'{self.node.ptr.value}' # long ass chain :0 
        

        self.rect = pygame.Rect(Vector2D[0],Vector2D[1],NodeRect.width,self.sizeY)
        self.surface = pygame.surface.Surface((100,self.sizeY))

        self.color = NodeColors.RandomColor()
        
        
    def Draw(self, Screen):
        # Node Base 
        self.surface.fill(Colors[0])    # Bottom Half
        pygame.draw.rect(self.surface,self.color,(0,0,100,100//2))          # Top half
        pygame.draw.rect(self.surface,Colors[1],(0,0,100,self.sizeY),5)     # border
        
        # Render Text
        # if dark bg, make text white
        dark = False
        for rgb in self.color:
            if rgb > 128:
                dark = True
                break
        
        if dark:
            self.surface.blit(font.render(self.value,False,Colors[1]),(37,4))    # Value
        else:
            self.surface.blit(font.render(self.value,False,Colors[0]),(37,4))    # Value

        if self.node.ptr != None:
            if type(self.node.ptr) == list:
                yPos = 50
                for pointer in self.node.ptr:
                    self.surface.blit(font.render(f'{pointer.value}',False,(0,0,0)),(37,yPos))
                    yPos += 50
                    
                    
            else:        
                self.surface.blit(font.render(self.ptrText,False,(0,0,0)),(37,50))    # Ptr

        Screen.blit(self.surface,self.rect)
    
    def Update(self,Screen):
        self.Move()
        self.Draw(Screen)

    # will move to mouse pos
    # Issue with ordering - need a system to differentiate whats on top
    def Move(self):
        global mousePrev, mouseDelta, mouseSelected

        # if mousing over and pressing left click
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed() == (1,0,0):
            if mouseSelected == None:
                mouseSelected = self

        if mouseSelected == self:
            self.surface.set_alpha(128)
            self.rect.x += mouseDelta[0]
            self.rect.y += mouseDelta[1]
            if pygame.mouse.get_pressed() != (1,0,0):
                 mouseSelected = None
        else:
            self.surface.set_alpha(256)
        
