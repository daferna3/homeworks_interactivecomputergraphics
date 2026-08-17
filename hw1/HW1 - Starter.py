#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COSC 4370 Homework #1
This is the starter code for the first homework assignment.
It should run as is and will serve as the starting point for development.
"""

import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# question for the professor: how many comments would you like explaining my code? please let me know for the next one :]


def Cube():
    d = 0.55 #ToDo: This is the default but is too large and needs to be changed
    verticies = (
        (d, -d, -d),
        (d, d, -d),
        (-d, d, -d),
        (-d, -d, -d),
        (d, -d, d),
        (d, d, d),
        (-d, -d, d),
        (-d, d, d)
        )

    edges = (
        (0,1), (0,3), (0,4), (2,1), (2,3), (2,7),
        (6,3), (6,4), (6,7), (5,1), (5,4), (5,7)
        )
    glColor(1,1,1) # Draw the cube in white
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
    
def Tetrahedron():
    d = 0.55
    verticies = ( # 4 verticies
        (-d, d, d),
        (d, -d, d),
        (d, d, -d),
        (-d, -d, -d)
        )

    edges = ( #6 edges
    (0, 1), (0, 2), (0, 3),
    (1, 2), (1, 3), (2, 3)
    )
    glColor(1,1,1) # Draw in white
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
    
def Octahedron(): # 6 verticies
    d = 1
    verticies = (
        (0, 0, d),
        (0, 0, -d),
        (d, 0, 0),
        (-d, 0, 0),
        (0, d, 0),
        (0, -d, 0), 
        )

    edges = ( # 12 edges
        (0, 2), (0, 4), (0, 3), (0, 5),
        (1, 2), (1, 4), (1, 3), (1, 5),
        (2, 4), (4, 3), (3, 5), (5, 2)
        )
    glColor(1,1,1) # Draw in white
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
    
def Dodecahedron(): # 20 vertices
    d = 0.55 #ToDo: This is the default but is too large and needs to be changed 

    calc = (1 + math.sqrt(5)) / 2
    a = 1 / calc
    verticies = (
        (-1, -1, -1),
        (-1, -1,  1),
        (-1,  1, -1),
        (-1,  1,  1),
        ( 1, -1, -1),
        ( 1, -1,  1),
        ( 1,  1, -1),
        ( 1,  1,  1),
        (0, -a, -calc),
        (0, -a,  calc),
        (0,  a, -calc),
        (0,  a,  calc),
        (-a, -calc, 0),
        (-a,  calc, 0),
        ( a, -calc, 0),
        ( a,  calc, 0),
        (-calc, 0, -a),
        ( calc, 0, -a),
        (-calc, 0,  a),
        ( calc, 0,  a)
        )
    
    verticies = tuple((x*d, y*d, z*d) for x, y, z in verticies)

    edges = ( # 30 edges :(
        (0,8), (0,12), (0,16),
        (1,9), (1,12), (1,18),
        (2,10), (2,13), (2,16),
        (3,11), (3,13), (3,18),
        (4,8), (4,14), (4,17),
        (5,9), (5,14), (5,19),
        (6,10), (6,15), (6,17),
        (7,11), (7,15), (7,19),
        (8,10), (9,11), (12,14),
        (13,15), (16,18), (17,19)
        )
    glColor(1,1,1) # Draw the cube in white
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
    
def Icosahedron(): # 12 vertices
    d = 0.55 #ToDo: This is the default but is too large and needs to be changed 
   
    calc = (1 + math.sqrt(5)) / 2
    a = 1 / calc
    verticies = (
        (-1,  calc, 0),
        ( 1,  calc, 0),
        (-1, -calc, 0),
        ( 1, -calc, 0),
    
        (0, -1,  calc),
        (0,  1,  calc),
        (0, -1, -calc),
        (0,  1, -calc),
    
        ( calc, 0, -1),
        ( calc, 0,  1),
        (-calc, 0, -1),
        (-calc, 0,  1)
        )
    
    verticies = tuple((x*d, y*d, z*d) for x, y, z in verticies)

    edges = ( # 30 edges :(
        (0,1), (0,5), (0,7), (0,10),
        (0,11), (1,5), (1,7), (1,8),
        (1,9), (2,3), (2,4), (2,6),
        (2,10), (2,11), (3,4), (3,6),
        (3,8), (3,9), (4,5), (4,9),
        (4,11), (5,9), (5,11), (6,7),
        (6,8), (6,10), (7,8), (7,10),
        (8,9), (10,11)
        )
    glColor(1,1,1) # Draw the cube in white
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def Axes():
    glBegin(GL_LINES)
    glColor(1,0,0) # Red for the x-axis
    glVertex3fv((0,0,0))
    glVertex3fv((1.5,0,0))
    glColor(0,1,0) # Green for the y-axis
    glVertex3fv((0,0,0))
    glVertex3fv((0,1.5,0))
    glColor(0,0,1) # Blue for the z-axis
    glVertex3fv((0,0,0))
    glVertex3fv((0,0,1.5))
    glEnd()


def Circle():
    glPushMatrix()
    glLoadIdentity()
    glOrtho(-2, 2, -2, 2, -2, 2)
    glColor(1,0,1) # Purple for the limits
    glBegin(GL_LINE_LOOP)
    for i in range(36):
        angle = 2.0 * math.pi * i / 36
        x = math.cos(angle)
        y = math.sin(angle)
        glVertex3fv((x, y, 0))
    glEnd()
    glPopMatrix()
    

def main():
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption('Homework #1 - Denisse Fernandez') #ToDo: Change this 
    glOrtho(-2, 2, -2, 2, -2, 2)
    glMatrixMode(GL_MODELVIEW)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        keys = pygame.key.get_pressed()
        
        if keys[K_1]:
            Tetrahedron()
        elif keys[K_2]:
            Cube()
        elif keys[K_3]:
            Octahedron()
        elif keys[K_4]:
            Dodecahedron()
        elif keys[K_5]:
            Icosahedron()
        Axes() # Draw the axes
        Circle() # Draw the limit circle
        
        pygame.display.flip()
        pygame.time.wait(10)


main()

# currently: make the shapes change per button press, determine verticies and edges for each