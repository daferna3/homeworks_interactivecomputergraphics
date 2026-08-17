#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COSC 4370 Homework #2
"""

import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

mercuryAngle = 0
venusAngle = 0
earthAngle = 0
moonAngle = 0
marsAngle = 0
    
# good source: https://thepythoncodingbook.com/2021/09/29/simulating-orbiting-planets-in-a-solar-system-using-python-orbiting-planets-series-1/

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
    
    

    
def Sun():
    glPushMatrix()

    glTranslatef(0, 0, 0)
    #glScalef(2.0, 2.0, 2.0)
    glColor3f(1,1,0)
    Sphere(2.0)
    
    Circles(3.9)
    Circles(7.2)
    Circles(10)
    Circles(15)

    glPopMatrix()
    
def Planet(radius, color):
    glColor3f(*color)
    Sphere(radius)
  
    
def Mercury():
    glPushMatrix()
    glRotatef(mercuryAngle, 0, 0, 1)
    glTranslatef(3.9, 0, 0) # AU
    Planet(0.38, (1,0,0)) #draw
    glPopMatrix()
    
def Venus():
    glPushMatrix()
    glRotatef(venusAngle, 0, 0, 1)
    glTranslatef(7.2, 0, 0) # AU
    Planet(0.95, (0,1,0)) # draw
    glPopMatrix()
    
def Moon():
    glPushMatrix()
    glRotatef(moonAngle, 0, 0, 1)
    glTranslatef(1.5, 0, 0) # AU
    Planet(0.27, (1,1,1)) # draw
    glPopMatrix()
    
    
def Earth():
    glPushMatrix()
    glRotatef(earthAngle, 0, 0, 1)
    glTranslatef(10, 0, 0) # AU
    Planet(1.00, (0,0,1)) #draw
    Circles(1.5)
    Moon()
    glPopMatrix()
    

def Mars():
    glPushMatrix()
    glRotatef(marsAngle, 0, 0, 1)
    glTranslatef(15, 0, 0) # AU
    Planet(0.53, (1,0,0)) #draw
    glPopMatrix() 
    




def Axes():
    glBegin(GL_LINES)
    glColor3f(1,0,0) # Red for the x-axis
    glVertex3fv((0,0,0))
    glVertex3fv((1.5,0,0))
    glColor3f(0,1,0) # Green for the y-axis
    glVertex3fv((0,0,0))
    glVertex3fv((0,1.5,0))
    glColor3f(0,0,1) # Blue for the z-axis
    glVertex3fv((0,0,0))
    glVertex3fv((0,0,1.5))
    glEnd()


def Circles(radius):
    glBegin(GL_LINE_LOOP)
    glColor3f(1,1,1)
    for i in range(36):
        angle = 2.0 * math.pi * i / 36
        x = math.cos(angle)
        y = math.sin(angle)
        glVertex3f(x * radius, y * radius, 0)
    glEnd()
    

def main():
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    pygame.display.set_caption('Homework #2 - Denisse Fernandez') 
    glOrtho(-20, 20, -20, 20, -20, 20)
    glMatrixMode(GL_MODELVIEW)
    
    viewAngle = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        #glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glRotatef(-viewAngle, 1, 0, 0)
        keys = pygame.key.get_pressed()
        

        
        if keys[K_UP]:
            viewAngle -= 1
        if keys[K_DOWN]:
            viewAngle += 1
            
        viewAngle = max(0, min(90, viewAngle))
        global mercuryAngle, venusAngle, earthAngle, moonAngle, marsAngle

        Axes() # Draw the axes
        Sun()
        
        mercuryAngle += (365.26 / 87.97)
        venusAngle   += (365.26 / 224.70)
        earthAngle   += (365.26 / 365.26)
        moonAngle    += (365.26 / 27.3)
        marsAngle    += (365.26 / 686.98)
        
        Mercury()
        Venus()
        Earth()
        Mars()
        
        pygame.display.flip()
        pygame.time.wait(10)


main()