from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import smart_bedroom.core.lighting as lighting

def draw_ceiling_lamp():
    glDisable(GL_TEXTURE_2D)
    glDisable(GL_LIGHTING)

    glPushMatrix()
    glTranslatef(0.0, 3.18, 0.0)

    # =========================
    # WARNA SESUAI STATUS LAMPU
    # =========================
    if lighting.main_lamp_on:
        glColor3f(1.0, 0.95, 0.8)   # lampu nyala
    else:
        glColor3f(0.35, 0.35, 0.35) # lampu mati (redup)

    radius = 0.22
    segments = 32

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, 0.0, 0.0)

    import math
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        glVertex3f(x, 0.0, z)
    glEnd()

    glPopMatrix()

    glEnable(GL_LIGHTING)
