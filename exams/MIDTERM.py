#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COSC 4370 MIDTERM
"""

import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

x = 100
redAngle = 0
blueAngle = 120
greenAngle = 240
    

def Sphere(radius, lat_bands=20, long_bands=20):
    glBegin(GL_TRIANGLES)

    for i in range(lat_bands):
        # latitude
        lat0 = math.pi * (-0.5 + i / lat_bands)
        lat1 = math.pi * (-0.5 + (i + 1) / lat_bands)

        z0 = radius * math.sin(lat0)
        zr0 = radius * math.cos(lat0)

        z1 = radius * math.sin(lat1)
        zr1 = radius * math.cos(lat1)

        for j in range(long_bands):
            # longitude
            lon0 = 2 * math.pi * (j / long_bands)
            lon1 = 2 * math.pi * ((j + 1) / long_bands)

            # corners
            v1 = (
                zr0 * math.cos(lon0),
                zr0 * math.sin(lon0),
                z0
            )

            v2 = (
                zr1 * math.cos(lon0),
                zr1 * math.sin(lon0),
                z1
            )

            v3 = (
                zr1 * math.cos(lon1),
                zr1 * math.sin(lon1),
                z1
            )

            v4 = (
                zr0 * math.cos(lon1),
                zr0 * math.sin(lon1),
                z0
            )

            # tri 1
            glVertex3fv(v1)
            glVertex3fv(v2)
            glVertex3fv(v3)

            # tri 2
            glVertex3fv(v1)
            glVertex3fv(v3)
            glVertex3fv(v4)

    glEnd()
    
    

    
def Yellow():
    glPushMatrix()

    glTranslatef(0, 0, 0)
    # glScalef(x, x, x)
    glColor3f(1,1,0)
    Sphere(x)


    glPopMatrix()
    
def Small(radius, color):
    glColor3f(*color)
    Sphere(radius)
  
    
def Red():
    glPushMatrix()
    glColor3f(1,0,0)
    Circles(2*x)
    glRotatef(redAngle, 0, 0, 1)
    glTranslatef(2*x, 0, 0)
    Small(x/4, (1,0,0))
    glPopMatrix()
    
    
def Blue():
    glPushMatrix()
    glRotatef(60,0,1,0)
    glColor3f(0,0,1)
    Circles(2*x)
    glRotatef(blueAngle,0,0,1)
    glTranslatef(2*x,0,0)
    Small(x/4,(0,0,1))
    glPopMatrix()
    

def Green():
    glPushMatrix()
    glRotatef(60,1,0,0)
    glColor3f(0,1,0)
    Circles(2*x)
    glRotatef(greenAngle,0,0,1)
    glTranslatef(2*x,0,0)
    Small(x/4,(0,1,0))
    glPopMatrix()
    


def Circles(radius):
    glBegin(GL_LINE_LOOP)
    for i in range(36):
        angle = 2.0 * math.pi * i / 36
        x = math.cos(angle)
        y = math.sin(angle)
        glVertex3f(x * radius, y * radius, 0)
    glEnd()
    

def main():
    pygame.init()
    global x
    display = (5*x,5*x)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    pygame.display.set_caption('Midterm - Denisse Fernandez') 
    glOrtho(-2.5*x, 2.5*x, -2.5*x, 2.5*x, -5*x, 5*x)
    glMatrixMode(GL_MODELVIEW)
    
    viewAngle_x = 0
    viewAngle_y = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        #glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glRotatef(viewAngle_x, 1, 0, 0)
        glRotatef(viewAngle_y, 0, 1, 0)
        keys = pygame.key.get_pressed()
        

        
        if keys[K_UP]:
            viewAngle_x -= 1
        if keys[K_DOWN]:
            viewAngle_x += 1
        if keys[K_LEFT]:
            viewAngle_y -= 1
        if keys[K_RIGHT]:
            viewAngle_y += 1
            
        global redAngle, blueAngle, greenAngle
        
        if keys[K_r]:
            redAngle = 0
            blueAngle = 120
            greenAngle = 240
            viewAngle_x = 0
            viewAngle_y = 0
            
        viewAngle_x = max(-45, min(45, viewAngle_x))
        viewAngle_y = max(-45, min(45, viewAngle_y))
        
        redAngle += 5
        blueAngle += 6
        greenAngle += 7
        
        Yellow()
        Red()
        Blue()
        Green()
    
        
        pygame.display.flip()
        pygame.time.wait(10)


main()