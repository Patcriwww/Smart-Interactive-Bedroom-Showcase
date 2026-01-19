from OpenGL.GL import *


def draw_central_ac(ac_tex):
    """Draw a central AC unit on the ceiling"""
    if ac_tex is None:
        return

    glDisable(GL_LIGHTING)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, ac_tex)
    glColor3f(1, 1, 1)

    y = 2.98
    size = 0.6

    offset_x = -1.9
    offset_z = 1.8

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-size + offset_x, y, -size + offset_z)
    glTexCoord2f(1, 0)
    glVertex3f(size + offset_x, y, -size + offset_z)
    glTexCoord2f(1, 1)
    glVertex3f(size + offset_x, y, size + offset_z)
    glTexCoord2f(0, 1)
    glVertex3f(-size + offset_x, y, size + offset_z)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING)
