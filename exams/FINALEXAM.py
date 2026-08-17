#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COSC 4370 FINAL EXAM
"""

import math
import pygame
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


speed = 8.0 # particle speed
min_speed = 2.0
max_speed = 20.0

cone_angle = math.radians(10) # cone
min_angle = math.radians(2)
max_angle = math.radians(25)

spawn_rate = 100 # pps
min_spawn = 1
max_spawn = 1000
spawn_timer = 0

zoom = 20.0 # zoom obv
min_zoom = 5.0
max_zoom = 40.0


class Particle:
    def __init__(self):
        # pos
        self.x = 0
        self.y = 1
        self.z = 0
        # vel
        theta = random.uniform(0, 2*math.pi)
        phi = random.uniform(0, cone_angle)
        
        self.vx = speed * math.sin(phi) * math.cos(theta)
        self.vy = speed * math.cos(phi)
        self.vz = speed * math.sin(phi) * math.sin(theta)

        self.life = 3.0
        self.maxLife = 3.0


def Sphere(radius, lat_bands=10, long_bands=10):
    display_list = glGenLists(1)
    glNewList(display_list, GL_COMPILE)
    
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
            x1 = zr0 * math.cos(lon0)
            y1 = zr0 * math.sin(lon0)
            v1 = (x1, y1, z0)

            x2 = zr1 * math.cos(lon0)
            y2 = zr1 * math.sin(lon0)
            v2 = (x2, y2, z1)

            x3 = zr1 * math.cos(lon1)
            y3 = zr1 * math.sin(lon1)
            v3 = (x3, y3, z1)

            x4 = zr0 * math.cos(lon1)
            y4 = zr0 * math.sin(lon1)
            v4 = (x4, y4, z0)

            # tri 1 (with normals for lighting)
            glNormal3f(x1/radius, y1/radius, z0/radius)
            glVertex3fv(v1)
            glNormal3f(x2/radius, y2/radius, z1/radius)
            glVertex3fv(v2)
            glNormal3f(x3/radius, y3/radius, z1/radius)
            glVertex3fv(v3)

            # tri 2 (with normals for lighting)
            glNormal3f(x1/radius, y1/radius, z0/radius)
            glVertex3fv(v1)
            glNormal3f(x3/radius, y3/radius, z1/radius)
            glVertex3fv(v3)
            glNormal3f(x4/radius, y4/radius, z0/radius)
            glVertex3fv(v4)

    glEnd()
    glEndList()
    return display_list


def draw_cylinder():
    quadric = gluNewQuadric()
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    glColor3f(0.5,0.5,0.5)
    gluCylinder(quadric, 0.5, 0.5, 1.0, 16, 1)
    glPopMatrix()
    gluDeleteQuadric(quadric)
    
    
def main():
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    
    global speed, cone_angle, spawn_timer, spawn_rate, zoom
    
    viewAngle = 0
    particles = []
    clock = pygame.time.Clock()

    sphere_list = Sphere(0.1)
    
    while True:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        #glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-zoom, zoom, -zoom, zoom, -100, 100)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glRotatef(-viewAngle, 1, 0, 0)
        
        light_position = (0, 10, 0, 1)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)

        keys = pygame.key.get_pressed()
        
        gravity = -9.8

        for p in particles:
            p.vy += gravity * dt
        
            p.x += p.vx * dt
            p.y += p.vy * dt
            p.z += p.vz * dt
        
            p.life -= dt
            
                    
        for p in particles:
            glPushMatrix()
        
            glTranslatef(p.x, p.y, p.z)
        
            life_ratio = max(0, p.life / p.maxLife)
            
            color = (1 - life_ratio, 0, life_ratio) # red to blue
        
            glColor3fv(color)
            glCallList(sphere_list)
        
            glPopMatrix()
    
        particles = [p for p in particles if p.life > 0]
        
        draw_cylinder()
        spawn_timer += dt
        
        while spawn_timer >= 1 / spawn_rate:
            particles.append(Particle())
            spawn_timer -= 1 / spawn_rate
        

        if keys[K_UP]:
            viewAngle -= 1
        
        if keys[K_DOWN]:
            viewAngle += 1
        
        
        # adjst speed
        if keys[K_LEFT]:
            speed -= 10.0 * dt
        
        if keys[K_RIGHT]:
            speed += 10.0 * dt
        
        
        # adjust cone angle
        if keys[K_COMMA]:  # <
            cone_angle -= math.radians(10.0 * dt)
        
        if keys[K_PERIOD]:  # >
            cone_angle += math.radians(10.0 * dt)
            
        if keys[K_EQUALS]: # +
            spawn_rate += 100 * dt
        
        if keys[K_MINUS]: # -
            spawn_rate -= 100 * dt
            
        if keys[K_w]:
            zoom -= 10.0 * dt
        
        if keys[K_s]:
            zoom += 10.0 * dt
        
        zoom = max(min_zoom, min(max_zoom, zoom))
        
        spawn_rate = max(min_spawn, min(max_spawn, spawn_rate))
        
        speed = max(min_speed, min(max_speed, speed))
        
        cone_angle = max(min_angle, min(max_angle, cone_angle))
            
        viewAngle = max(0, min(60, viewAngle))
        
        pygame.display.flip()

if __name__ == "__main__":
    main()