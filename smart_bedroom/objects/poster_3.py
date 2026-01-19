from OpenGL.GL import *

def draw_poster_3(tex_id):
    if tex_id is None:
        return

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glColor3f(1, 1, 1)

    glPushMatrix()
    glTranslatef(-1.50, 1.4, 3.98)
    glRotatef(180, 0, 1, 0)

    w, h, z = 1.2, 1.4, 0.02

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-w/2, 0,  z)
    glTexCoord2f(1, 0); glVertex3f( w/2, 0,  z)
    glTexCoord2f(1, 1); glVertex3f( w/2, h,  z)
    glTexCoord2f(0, 1); glVertex3f(-w/2, h,  z)
    glEnd()

    glPopMatrix()
    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)