from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_window():
    from ..core.lighting import is_day

    glDisable(GL_LIGHTING)

    z = -3.99
    y_bottom = 1.4
    y_top = 2.7
    x_left = -1.0
    x_right = 1.0

    glColor3f(0.95, 0.95, 0.95)
    glBegin(GL_QUADS)
    glVertex3f(x_left, y_bottom, z)
    glVertex3f(x_right, y_bottom, z)
    glVertex3f(x_right, y_top, z)
    glVertex3f(x_left, y_top, z)
    glEnd()

    inset = 0.08
    glColor3f(0.85, 0.85, 0.85)
    glBegin(GL_QUADS)
    glVertex3f(x_left + inset, y_bottom + inset, z + 0.001)
    glVertex3f(x_right - inset, y_bottom + inset, z + 0.001)
    glVertex3f(x_right - inset, y_top - inset, z + 0.001)
    glVertex3f(x_left + inset, y_top - inset, z + 0.001)
    glEnd()

    if is_day:
        glColor3f(0.6, 0.8, 1.0)
    else:
        glColor3f(0.05, 0.07, 0.12)

    glass_inset = 0.16
    glBegin(GL_QUADS)
    glVertex3f(x_left + glass_inset, y_bottom + glass_inset, z + 0.002)
    glVertex3f(x_right - glass_inset, y_bottom + glass_inset, z + 0.002)
    glVertex3f(x_right - glass_inset, y_top - glass_inset, z + 0.002)
    glVertex3f(x_left + glass_inset, y_top - glass_inset, z + 0.002)
    glEnd()

    glColor3f(0.75, 0.75, 0.75)
    glLineWidth(3)

    glBegin(GL_LINES)
    glVertex3f(0.0, y_bottom + glass_inset, z + 0.003)
    glVertex3f(0.0, y_top - glass_inset, z + 0.003)
    glVertex3f(x_left + glass_inset, (y_bottom + y_top) / 2, z + 0.003)
    glVertex3f(x_right - glass_inset, (y_bottom + y_top) / 2, z + 0.003)
    glEnd()

    glEnable(GL_LIGHTING)
