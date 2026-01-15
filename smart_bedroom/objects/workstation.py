from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_workstation():
    glPushMatrix()
    glTranslatef(-3.3, 0.0, 1.2)
    glRotatef(90, 0, 1, 0)

    glColor3f(0.42, 0.28, 0.15)
    glPushMatrix()
    glTranslatef(0.0, 0.75, 0.0)
    glScalef(1.2, 0.08, 0.6)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(0.30, 0.20, 0.12)
    for x in [-0.5, 0.5]:
        for z in [-0.25, 0.25]:
            glPushMatrix()
            glTranslatef(x, 0.38, z)
            glScalef(0.08, 0.75, 0.08)
            glutSolidCube(1)
            glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, 1.10, -0.18)

    glColor3f(0.2, 0.2, 0.2)
    glPushMatrix()
    glTranslatef(0.0, -0.14, 0.0)
    glScalef(0.08, 0.24, 0.03)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, -0.28, 0.05)
    glScalef(0.25, 0.03, 0.18)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(0.05, 0.05, 0.05)
    glPushMatrix()
    glScalef(0.55, 0.35, 0.04)
    glutSolidCube(1)
    glPopMatrix()

    glDisable(GL_LIGHTING)
    glColor3f(0.1, 0.3, 0.45)
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.03)
    glScalef(0.48, 0.28, 0.01)
    glutSolidCube(1)
    glPopMatrix()
    glEnable(GL_LIGHTING)

    glPopMatrix()

    glColor3f(0.10, 0.10, 0.10)
    glPushMatrix()
    glTranslatef(0.0, 0.82, 0.05)
    glScalef(0.45, 0.03, 0.18)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(0.08, 0.08, 0.08)
    glPushMatrix()
    glTranslatef(0.30, 0.83, 0.05)
    glScalef(0.08, 0.03, 0.12)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(0.12, 0.12, 0.12)
    glPushMatrix()
    glTranslatef(0.75, 0.25, 0.0)
    glScalef(0.28, 0.9, 0.45)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.55)

    glColor3f(0.18, 0.18, 0.18)
    glPushMatrix()
    glTranslatef(0.0, 0.45, 0.0)
    glScalef(0.5, 0.08, 0.5)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, 0.75, 0.22)
    glScalef(0.5, 0.6, 0.08)
    glutSolidCube(1)
    glPopMatrix()

    for x in [-0.18, 0.18]:
        for z in [-0.18, 0.18]:
            glPushMatrix()
            glTranslatef(x, 0.22, z)
            glScalef(0.06, 0.45, 0.06)
            glutSolidCube(1)
            glPopMatrix()

    glPopMatrix()
    glPopMatrix()
