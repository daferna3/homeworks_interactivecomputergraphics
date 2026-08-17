# -*- coding: utf-8 -*-
"""
HOMEWORK 3 - DENISSE FERNANDEZ
    
"""

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import pywavefront
import numpy as np

teapot = pywavefront.Wavefront('teapot.obj', create_materials = True, collect_faces = True)

vertices = teapot.vertices

faces = teapot.mesh_list[0].faces





COLORS = ((1,0,0), (0,0,1), (1,0,0), (0,0,1))

def norm(v0, v1, v2):
    A = np.array(v0)
    B = np.array(v1)
    C = np.array(v2)
    
    U = B - A
    V = C - A
    
    normal = np.cross(U, V)
    magnitude = np.linalg.norm(normal)
    
    if magnitude == 0:
        return (0.0, 0.0, 0.0)
        
    done = normal / magnitude
    
    return (float(done[0]), float(done[1]), float(done[2]))


normals = []
for face in faces:
    v0 = vertices[face[0]]
    v1 = vertices[face[1]]
    v2 = vertices[face[2]]
    normals.append(norm(v0, v1, v2))


def Teapot():
    for face, normal in zip(faces, normals):
        glBegin(GL_POLYGON) 
        glNormal3fv(normal)
        
        for vertex_index in face:
            glVertex3fv(vertices[vertex_index])
            
        glEnd()
        
        glColor3fv((1,1,1))
        

def main():
    global SURFACES

    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    clock = pygame.time.Clock()

    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, (display[0]/display[1]), 0.1, 100)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -90)
    
    
    #glLightfv(GL_LIGHT0, GL_POSITION,  (5, -10, 0, 1)) # point light from the below (red)
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0, 0, 1, 1))
    
    #glLightfv(GL_LIGHT1, GL_POSITION,  (-5, 10, 0, 1))  # point light from the above (blue)
    glLightfv(GL_LIGHT1, GL_AMBIENT,   (0, 0, 0, 1))
    glLightfv(GL_LIGHT1, GL_DIFFUSE,   (1, 0, 0, 1))

    glEnable(GL_DEPTH_TEST) 
    
    glEnable(GL_LIGHTING)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0, 0, 0, 1))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )

    angle = 0

    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()      
    
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            
            glTranslatef(0, -5, -50) # zoom out
            
            glRotatef(35, 1, 0, 0) # move up
            
            # glTranslatef(0, 10, -10) # move back
            
            
            
            # glScalef(1, 0, 1)
                        
            glLightfv(GL_LIGHT0, GL_POSITION,  (-20, 20, 15, 1)) # point light from the below (red)
                        
            glLightfv(GL_LIGHT1, GL_POSITION,  (20, -20, 15, 0)) # point light from the above (blue)
    
            angle = (angle + 1) % 360
            glRotatef(angle, 0, 1, 0)
            
            glRotatef(-90, 1, 0, 0) # rotate teapot
            
            Teapot()
    
            pygame.display.flip()
            clock.tick(50)

main()