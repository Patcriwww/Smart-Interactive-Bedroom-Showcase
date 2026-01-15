from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_table():
    glPushMatrix()
    glTranslatef(-3.2, 0.0, -1.1)

    glColor3f(0.55, 0.35, 0.25)
    glPushMatrix()
    glTranslatef(0, 0.6, 0)
    glScalef(0.6, 0.1, 0.6)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(0.4, 0.25, 0.15)
    for x in [-0.22, 0.22]:
        for z in [-0.22, 0.22]:
            glPushMatrix()
            glTranslatef(x, 0.3, z)
            glScalef(0.08, 0.6, 0.08)
            glutSolidCube(1)
            glPopMatrix()

    glPopMatrix()
