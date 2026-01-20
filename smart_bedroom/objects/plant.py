from OpenGL.GL import *
import math


def draw_plant():
    glPushMatrix()
    glTranslatef(-3.6, 0.0, 3.6)

    glColor3f(0.9, 0.9, 0.9)
    segments = 20
    pot_r = 0.25
    pot_h = 0.30

    glBegin(GL_QUAD_STRIP)
    for i in range(segments + 1):
        a = 2 * math.pi * i / segments
        glVertex3f(math.cos(a) * pot_r, 0.0, math.sin(a) * pot_r)
        glVertex3f(math.cos(a) * pot_r, pot_h, math.sin(a) * pot_r)
    glEnd()

    glColor3f(0.35, 0.25, 0.15)
    glBegin(GL_POLYGON)
    for i in range(segments):
        a = 2 * math.pi * i / segments
        glVertex3f(math.cos(a) * 0.22, pot_h, math.sin(a) * 0.22)
    glEnd()

    glColor3f(0.3, 0.5, 0.3)
    trunk_h = 0.28
    trunk_offset = -0.06
    trunk_r = 0.040

    glBegin(GL_QUADS)
    glVertex3f(-trunk_r, pot_h + trunk_offset, 0.0)
    glVertex3f(trunk_r, pot_h + trunk_offset, 0.0)
    glVertex3f(trunk_r, pot_h + trunk_h + trunk_offset, 0.0)
    glVertex3f(-trunk_r, pot_h + trunk_h + trunk_offset, 0.0)
    glEnd()

    glColor3f(0.18, 0.65, 0.30)
    leaf_base_y = pot_h + trunk_h + trunk_offset - 0.05
    leaf_count = 10
    leaf_length = 0.34
    leaf_width = 0.065
    leaf_segments = 7
    curve_angle = -8

    glPushMatrix()
    glTranslatef(0.0, leaf_base_y, 0.0)

    for i in range(leaf_count):
        glPushMatrix()
        glRotatef((360 / leaf_count) * i, 0, 1, 0)
        glRotatef(-22, 1, 0, 0)

        seg_len = leaf_length / leaf_segments

        for _ in range(leaf_segments):
            glRotatef(curve_angle, 1, 0, 0)
            glTranslatef(0.0, seg_len, 0.0)

            glBegin(GL_QUADS)
            glVertex3f(-leaf_width, 0.0, 0.0)
            glVertex3f(leaf_width, 0.0, 0.0)
            glVertex3f(leaf_width * 0.6, seg_len, 0.0)
            glVertex3f(-leaf_width * 0.6, seg_len, 0.0)
            glEnd()

        glPopMatrix()

    glPopMatrix()
    glPopMatrix()
