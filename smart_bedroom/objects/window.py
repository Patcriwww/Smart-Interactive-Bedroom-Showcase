from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_window():
    from ..core.lighting import is_day
    from ..render.texture import city_day_tex, city_night_tex

    glDisable(GL_LIGHTING)

    # ===============================
    # POSISI JENDELA
    # ===============================
    z = -3.99
    y_bottom = 1.4
    y_top = 2.7
    x_left = -1.0
    x_right = 1.0

    # ===============================
    # FRAME LUAR
    # ===============================
    glColor3f(0.95, 0.95, 0.95)
    glBegin(GL_QUADS)
    glVertex3f(x_left, y_bottom, z)
    glVertex3f(x_right, y_bottom, z)
    glVertex3f(x_right, y_top, z)
    glVertex3f(x_left, y_top, z)
    glEnd()

    # ===============================
    # FRAME DALAM
    # ===============================
    inset = 0.08
    glColor3f(0.85, 0.85, 0.85)
    glBegin(GL_QUADS)
    glVertex3f(x_left + inset, y_bottom + inset, z + 0.001)
    glVertex3f(x_right - inset, y_bottom + inset, z + 0.001)
    glVertex3f(x_right - inset, y_top - inset, z + 0.001)
    glVertex3f(x_left + inset, y_top - inset, z + 0.001)
    glEnd()

    # ===============================
    # KACA (PAKAI TEXTURE LUAR)
    # ===============================
    glass_inset = 0.16

    glEnable(GL_TEXTURE_2D)
    tex = city_day_tex if is_day else city_night_tex
    glBindTexture(GL_TEXTURE_2D, tex)
    glColor3f(1, 1, 1)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(x_left + glass_inset, y_bottom + glass_inset, z + 0.002)
    glTexCoord2f(1, 0)
    glVertex3f(x_right - glass_inset, y_bottom + glass_inset, z + 0.002)
    glTexCoord2f(1, 1)
    glVertex3f(x_right - glass_inset, y_top - glass_inset, z + 0.002)
    glTexCoord2f(0, 1)
    glVertex3f(x_left + glass_inset, y_top - glass_inset, z + 0.002)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)

    # ===============================
    # PEMBAGI KACA (CROSS)
    # ===============================
    glColor3f(0.75, 0.75, 0.75)
    glLineWidth(3)

    glBegin(GL_LINES)
    glVertex3f(0.0, y_bottom + glass_inset, z + 0.003)
    glVertex3f(0.0, y_top - glass_inset, z + 0.003)

    glVertex3f(x_left + glass_inset, (y_bottom + y_top) / 2, z + 0.003)
    glVertex3f(x_right - glass_inset, (y_bottom + y_top) / 2, z + 0.003)
    glEnd()

    glEnable(GL_LIGHTING)

    # ===============================
    # SUNLIGHT BEAM (DAY ONLY)
    # ===============================
    if is_day:
        glDisable(GL_LIGHTING)

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glDisable(GL_DEPTH_TEST)
        glDepthMask(GL_FALSE)

        glColor4f(1.0, 0.95, 0.7, 0.18)

        z0 = z + 0.02
        z1 = z0 + 4.5

        y0 = (y_bottom + y_top) / 2 + 0.3
        y1 = y0 - 2.2

        glBegin(GL_QUADS)
        glVertex3f(x_left + 0.25, y0, z0)
        glVertex3f(x_right - 0.25, y0, z0)
        glVertex3f(x_right + 2.4, y1, z1)
        glVertex3f(x_left - 2.4, y1, z1)
        glEnd()

        glDepthMask(GL_TRUE)
        glEnable(GL_DEPTH_TEST)
        glDisable(GL_BLEND)

        glEnable(GL_LIGHTING)
