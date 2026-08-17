#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COSC 4370 Homework #4
"""

import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *



def Cube():
    vertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
                (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))
    
    
    edges = ((0,1), (0,3), (0,4), (2,1), (2,3), (2,7), (6,3), (6,4),
             (6,7), (5,1), (5,4), (5,7))
    
    texture_coords = [((0, 0), (1/3, 0), (1/3, 1/2), (0, 1/2)),
                      ((0, 1/2), (1/3, 1/2), (1/3, 1), (0, 1)),
                      ((1/3, 0), (2/3, 0), (2/3, 1/2), (1/3, 1/2)),
                      ((1/3, 1/2), (2/3, 1/2), (2/3, 1), (1/3, 1)),
                      ((2/3, 0), (1, 0), (1, 1/2), (2/3, 1/2)),
                      ((2/3, 1/2), (1, 1/2), (1, 1), (2/3, 1))]
    
    
    surfaces = ((0,1,2,3), (3,2,7,6), (6,7,5,4), (4,5,1,0), (1,5,7,2), (4,0,3,6))
    
    glBegin(GL_QUADS)
    for surface_index, surface in enumerate(surfaces):
        for vertex_index, vertex in enumerate(surface):
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(vertices[vertex])
    glEnd()
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    
# end of cube
    
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
    
    surfaces = ((0, 1, 2), (0, 2, 3), (0, 3, 1), (1, 3, 2))

    texture_coords = [((1/4, 1/2), (0, 0), (1/2, 0)),
        ((3/4, 1/2), (1/2, 0), (1, 0)),
        ((1/4, 1),   (0, 1/2), (1/2, 1/2)),
        ((3/4, 1),   (1/2, 1/2), (1, 1/2))]

    glBegin(GL_TRIANGLES)
    for surface_index, surface in enumerate(surfaces):
        for vertex_index, vertex in enumerate(surface):
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(verticies[vertex])
    glEnd()
    
# end of tetrahedron
    
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

    texture_coords = [((1/8, 1/2), (0, 0), (1/4, 0)),
        ((3/8, 1/2), (1/4, 0), (2/4, 0)),
        ((5/8, 1/2), (2/4, 0), (3/4, 0)),
        ((7/8, 1/2), (3/4, 0), (1, 0)),
        ((1/8, 1), (0, 1/2), (1/4, 1/2)),
        ((3/8, 1), (1/4, 1/2), (2/4, 1/2)),
        ((5/8, 1), (2/4, 1/2), (3/4, 1/2)),
        ((7/8, 1), (3/4, 1/2), (1, 1/2))]
    
    surfaces = ((0, 2, 4), (0, 4, 3), (0, 3, 5), (0, 5, 2),
        (1, 4, 2), (1, 3, 4), (1, 5, 3), (1, 2, 5)
    )

    glBegin(GL_TRIANGLES)
    for surface_index, surface in enumerate(surfaces):
        for vertex_index, vertex in enumerate(surface):
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(verticies[vertex])
    glEnd()
    
# end of octahedron
    
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

    edges = (
        (0, 8), (0, 12), (0, 16),
        (1, 9), (1, 12), (1, 18),
        (2, 10), (2, 13), (2, 16),
        (3, 11), (3, 13), (3, 18),
        (4, 8), (4, 14), (4, 17),
        (5, 9), (5, 14), (5, 19),
        (6, 10), (6, 15), (6, 17),
        (7, 11), (7, 15), (7, 19),
        (8, 10), (9, 11), (12, 14),
        (13, 15), (16, 18), (17, 19)
    )
    
    surfaces = (
        (0, 8, 4, 14, 12),
        (16, 2, 10, 8, 0),
        (0, 12, 1, 18, 16),
        (12, 14, 5, 9, 1),
        (1, 9, 11, 3, 18),
        (13, 15, 6, 10, 2),
        (16, 18, 3, 13, 2),
        (3, 11, 7, 15, 13),
        (4, 8, 10, 6, 17),
        (17, 19, 5, 14, 4),
        (19, 7, 11, 9, 5),
        (6, 15, 7, 19, 17)
    )

    # 4x3 Grid Texture Atlas for 12 Pentagonal Faces
    p_uv = ((0.5, 0.95), (0.95, 0.62), (0.78, 0.10), (0.22, 0.10), (0.05, 0.62))
    w, h = 1/4, 1/3
    texture_coords = tuple(
        tuple(((i % 4) * w + u * w, (i // 4) * h + v * h) for u, v in p_uv)
        for i in range(12)
    )

    glColor3f(1, 1, 1)
    for surface_index, surface in enumerate(surfaces):
        glBegin(GL_POLYGON)
        for vertex_index, vertex in enumerate(surface):
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(verticies[vertex])
        glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
    
# end of dodecahedron
    
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
    
    surfaces = (
        (0, 11, 5), (0, 5, 1), (0, 1, 7), (0, 7, 10), (0, 10, 11),
        (1, 5, 9), (5, 11, 4), (11, 10, 2), (10, 7, 6), (7, 1, 8),
        (3, 9, 4), (3, 4, 2), (3, 2, 6), (3, 6, 8), (3, 8, 9),
        (4, 9, 5), (2, 4, 11), (6, 2, 10), (8, 6, 7), (9, 8, 1)
    )

    tot_tri = ((0.5, 1.0), (0.0, 0.0), (1.0, 0.0)) # total face triangles
    w, h = 1/5, 1/4
    texture_coords = tuple(
        tuple(((i % 5) * w + u * w, (i // 5) * h + v * h) for u, v in tot_tri)
        for i in range(20)
    )

    glColor3f(1, 1, 1)
    glBegin(GL_TRIANGLES)
    for surface_index, surface in enumerate(surfaces):
        for vertex_index, vertex in enumerate(surface):
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(verticies[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

# end of icosahedron


def loadTexture(texture_name):
    textureSurface = pygame.image.load(texture_name)
    textureSurface = pygame.transform.flip(textureSurface, True, False)
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid


def main():
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption('Homework #4 - Denisse Fernandez')

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])
    
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(80, (display[0]/display[1]), 0.1, 50.0)
    
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, -3, 0, 0, 0, 0, 0, 0, 1)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glLoadIdentity()
    
    cube_texture = loadTexture('cube_texture.png')
    tet_texture= loadTexture('tet_texture.png')
    oct_texture = loadTexture('oct_texture.png')
    dod_texture = loadTexture('dod_texture.png')
    ico_texture = loadTexture('ico_texture.png')
    
    angle = 0 # Rotation angle about the vertical axis
    glColor(1,1,1,1)

    # apply view matrix
    glMultMatrixf(viewMatrix)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)


    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        # glRotatef(1, 1, 1, 1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        keys = pygame.key.get_pressed()
        
        glPushMatrix()
        glColor(1,1,1,1)
        tilt = 15 + 10 * math.cos(angle * math.pi/180) # Tilt as we rotate
        glRotate(tilt, 1, 0, 0) # Tilt a bit to be easier to see
        angle = (angle + 1) % 360
        glRotatef(angle, 0, 0, 1) # Rotate around the box's vertical axis
        
        if keys[K_1]:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, tet_texture)
            Tetrahedron()
        elif keys[K_2]:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, cube_texture)
            Cube()
            glDisable(GL_TEXTURE_2D)
        elif keys[K_3]:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, oct_texture)
            Octahedron()
        elif keys[K_4]:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, dod_texture)
            Dodecahedron()
        elif keys[K_5]:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, ico_texture)
            Icosahedron()
            
            


        # Draw the ground quad
        glColor4f(0.5, 0.5, 0.5, 1)
        glBegin(GL_QUADS)
        glVertex3f(-10, -10, -2)
        glVertex3f(10, -10, -2)
        glVertex3f(10, 10, -2)
        glVertex3f(-10, 10, -2)
        glEnd()

        glPopMatrix()
        
        pygame.display.flip()
        pygame.time.wait(30)


main()


# to do: FIX DOD, adjust numbers as needed

