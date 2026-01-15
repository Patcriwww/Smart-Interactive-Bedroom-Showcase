from OpenGL.GL import *
import math


def draw_trash_bin():
    glPushMatrix()
    glTranslatef(3.75, 0.0, 1.55)

    radius = 0.18
    height = 0.45
    segments = 24

    glColor3f(0.15, 0.15, 0.15)
    glBegin(GL_QUAD_STRIP)
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        x = math.cos(angle) * radius
        z = math.sin(angle) * radius
        glVertex3f(x, 0.0, z)
        glVertex3f(x, height, z)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, 0.0, 0.0)
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        glVertex3f(math.cos(angle) * radius, 0.0, math.sin(angle) * radius)
    glEnd()

    glColor3f(0.10, 0.10, 0.10)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, height + 0.02, 0.0)
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        glVertex3f(math.cos(angle) * (radius + 0.02), height + 0.02, math.sin(angle) * (radius + 0.02))
    glEnd()

    glPopMatrix()
