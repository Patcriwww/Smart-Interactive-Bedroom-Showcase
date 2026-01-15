from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw_text(x, y, text):
    window_width = glutGet(GLUT_WINDOW_WIDTH)
    window_height = glutGet(GLUT_WINDOW_HEIGHT)

    glPushAttrib(GL_ENABLE_BIT | GL_COLOR_BUFFER_BIT | GL_TRANSFORM_BIT)

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, window_width, 0, window_height)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glDisable(GL_LIGHTING)
    glDisable(GL_DEPTH_TEST)
    glColor3f(1.0, 1.0, 1.0)

    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(char))

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

    glPopAttrib()


def draw_hud_bg(x, y, w, h, alpha=0.6):
    window_width = glutGet(GLUT_WINDOW_WIDTH)
    window_height = glutGet(GLUT_WINDOW_HEIGHT)

    glPushAttrib(GL_ENABLE_BIT | GL_COLOR_BUFFER_BIT | GL_TRANSFORM_BIT)

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, window_width, 0, window_height)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glDisable(GL_LIGHTING)
    glDisable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glColor4f(0.05, 0.05, 0.05, alpha)

    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + w, y)
    glVertex2f(x + w, y - h)
    glVertex2f(x, y - h)
    glEnd()

    glDisable(GL_BLEND)

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

    glPopAttrib()
