from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_door(tex_id):
    if tex_id is None:
        return

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glColor3f(1, 1, 1)

    glPushMatrix()
    glTranslatef(3.95, 0.0, 2.0)
    glRotatef(-90, 0, 1, 0)

    door_width = 1.3
    door_height = 2.5
    thickness = 0.03

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(0, 0, thickness)
    glTexCoord2f(1, 0); glVertex3f(door_width, 0, thickness)
    glTexCoord2f(1, 1); glVertex3f(door_width, door_height, thickness)
    glTexCoord2f(0, 1); glVertex3f(0, door_height, thickness)
    glEnd()

    glPopMatrix()

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
