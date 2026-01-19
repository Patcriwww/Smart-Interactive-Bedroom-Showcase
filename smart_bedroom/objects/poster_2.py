from OpenGL.GL import *


def draw_poster_2(poster_tex_2):
    """Draw a second poster on the wall"""
    if poster_tex_2 is None:
        return

    glDisable(GL_LIGHTING)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, poster_tex_2)
    glColor3f(1, 1, 1)

    w = 0.9
    h = 1.3

    glPushMatrix()
    glTranslatef(-3.95, 2.0, 3.0)
    glRotatef(90, 0, 1, 0)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(0, -h / 2, 0)
    glTexCoord2f(1, 0)
    glVertex3f(w, -h / 2, 0)
    glTexCoord2f(1, 1)
    glVertex3f(w, h / 2, 0)
    glTexCoord2f(0, 1)
    glVertex3f(0, h / 2, 0)
    glEnd()

    glPopMatrix()

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING)
