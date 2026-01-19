from OpenGL.GL import *
import math

from ..core.lighting import is_day
from ..render.texture import curtain_tex

# status buka tirai (None = auto)
curtain_open = None


def draw_curtain():
    if curtain_tex is None:
        return

    # ===============================
    # PROTEKSI STATE (WAJIB)
    # ===============================
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glPushMatrix()

    # Curtain adalah plane tipis → jangan pakai depth test
    glDisable(GL_DEPTH_TEST)

    # ===============================
    # LOGIKA BUKA TUTUP
    # ===============================
    cover = (
        0.35 if curtain_open is None and is_day
        else (1.0 if curtain_open is None else curtain_open)
    )

    # ===============================
    # SETUP TEXTURE & WARNA
    # ===============================
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, curtain_tex)
    glDisable(GL_LIGHTING)
    glColor3f(1.0, 1.0, 1.0)

    # ===============================
    # POSISI TIRAI
    # ===============================
    z = -3.95          # SEDIKIT DI DEPAN DINDING (ANTI KALAH DEPTH)
    y_bottom = 1.4
    y_top = 2.7
    x_left = -1.0
    x_right = 1.0

    folds = 14
    wave_amp = 0.07
    step = cover / folds

    # ===============================
    # TIRAI KIRI
    # ===============================
    for i in range(folds):
        x0 = x_left + i * step
        x1 = x_left + (i + 1) * step
        wave = math.sin(i * 0.9) * wave_amp

        u0 = i / folds
        u1 = (i + 1) / folds

        glBegin(GL_QUADS)
        glTexCoord2f(u0, 0); glVertex3f(x0, y_bottom, z + wave)
        glTexCoord2f(u1, 0); glVertex3f(x1, y_bottom, z - wave)
        glTexCoord2f(u1, 1); glVertex3f(x1, y_top,    z - wave)
        glTexCoord2f(u0, 1); glVertex3f(x0, y_top,    z + wave)
        glEnd()

    # ===============================
    # TIRAI KANAN
    # ===============================
    for i in range(folds):
        x0 = x_right - i * step
        x1 = x_right - (i + 1) * step
        wave = math.sin(i * 0.9) * wave_amp

        u0 = i / folds
        u1 = (i + 1) / folds

        glBegin(GL_QUADS)
        glTexCoord2f(u0, 0); glVertex3f(x0, y_bottom, z + wave)
        glTexCoord2f(u1, 0); glVertex3f(x1, y_bottom, z - wave)
        glTexCoord2f(u1, 1); glVertex3f(x1, y_top,    z - wave)
        glTexCoord2f(u0, 1); glVertex3f(x0, y_top,    z + wave)
        glEnd()

    # ===============================
    # RESTORE STATE (WAJIB)
    # ===============================
    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)

    glPopMatrix()
    glPopAttrib()
