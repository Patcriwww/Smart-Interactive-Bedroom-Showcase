from OpenGL.GL import *
from OpenGL.GLUT import *
from datetime import datetime


def draw_clock():
    time_str = datetime.now().strftime("%H:%M:%S")

    glPushAttrib(GL_ENABLE_BIT | GL_CURRENT_BIT)
    glDisable(GL_LIGHTING)

    glPushMatrix()
    glTranslatef(-3.95, 2.5, 0.5)
    glRotatef(90, 0, 1, 0)

    glColor3f(0.08, 0.08, 0.08)
    glBegin(GL_QUADS)
    glVertex3f(-0.7, -0.3, 0)
    glVertex3f(0.7, -0.3, 0)
    glVertex3f(0.7, 0.3, 0)
    glVertex3f(-0.7, 0.3, 0)
    glEnd()

    glColor3f(0.9, 0.95, 1.0)
    glTranslatef(-0.65, -0.08, 0.01)
    glScalef(0.0025, 0.0025, 0.0025)

    for ch in time_str:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(ch))

    glPopMatrix()
    glPopAttrib()
