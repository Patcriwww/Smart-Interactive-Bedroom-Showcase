from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_table_lamp():
    from ..core.lighting import is_day

    glPushMatrix()
    glTranslatef(-3.2, 0.75, -1.1)

    glColor3f(0.2, 0.2, 0.2)
    glPushMatrix()
    glScalef(0.25, 0.05, 0.25)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(0.3, 0.3, 0.3)
    glPushMatrix()
    glTranslatef(0, 0.25, 0)
    glScalef(0.05, 0.5, 0.05)
    glutSolidCube(1)
    glPopMatrix()

    if is_day:
        glColor3f(0.7, 0.7, 0.7)
    else:
        glColor3f(1.0, 0.9, 0.6)
        glDisable(GL_LIGHTING)

    glPushMatrix()
    glTranslatef(0, 0.6, 0)
    glScalef(0.4, 0.3, 0.4)
    glutSolidSphere(0.5, 24, 24)
    glPopMatrix()

    if not is_day:
        glEnable(GL_LIGHTING)

    glPopMatrix()
