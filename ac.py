from OpenGL.GL import *

def draw_ac_central():
    glPushMatrix()

    # Posisi: di atas kasur (sesuaikan koordinat kasurmu)
    glTranslatef(0.0, 2.4, -1.2)
    glScalef(1.8, 0.3, 0.4)

    glColor3f(0.9, 0.9, 0.9)

    glBegin(GL_QUADS)
    # depan
    glVertex3f(-0.5, -0.2,  0.2)
    glVertex3f( 0.5, -0.2,  0.2)
    glVertex3f( 0.5,  0.2,  0.2)
    glVertex3f(-0.5,  0.2,  0.2)

    # belakang
    glVertex3f(-0.5, -0.2, -0.2)
    glVertex3f( 0.5, -0.2, -0.2)
    glVertex3f( 0.5,  0.2, -0.2)
    glVertex3f(-0.5,  0.2, -0.2)
    glEnd()

    glPopMatrix()
