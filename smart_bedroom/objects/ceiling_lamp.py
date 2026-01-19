from OpenGL.GL import *
import math

from ..core import lighting


def draw_ceiling_lamp():
    glDisable(GL_TEXTURE_2D)
    glDisable(GL_LIGHTING)

    glPushMatrix()
    glTranslatef(0.0, 3.18, 0.0)

    if lighting.lamp_on:
        glColor3f(1.0, 0.95, 0.8)
    else:
        glColor3f(0.4, 0.4, 0.4)

    radius = 0.22
    segments = 32

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, 0.0, 0.0)
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        glVertex3f(x, 0.0, z)
    glEnd()

    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        glVertex3f(x, 0.001, z)
    glEnd()

    glPopMatrix()
    glEnable(GL_LIGHTING)
