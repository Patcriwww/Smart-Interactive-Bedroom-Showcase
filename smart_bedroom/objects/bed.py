from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_bed():
    glPushMatrix()
    glTranslatef(-2.2, 0.0, -2.1)

    glColor3f(0.45, 0.25, 0.15)
    glPushMatrix()
    glTranslatef(0, 0.3, 0)
    glScalef(2.2, 0.6, 1.4)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(0.95, 0.95, 0.9)
    glPushMatrix()
    glTranslatef(0, 0.7, 0)
    glScalef(2.1, 0.3, 1.3)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(0.9, 0.9, 0.6)
    glPushMatrix()
    glTranslatef(-1.15, 0.95, 0)
    glScalef(0.15, 1.4, 1.4)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()
