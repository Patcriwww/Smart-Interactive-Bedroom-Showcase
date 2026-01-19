from OpenGL.GL import *
from OpenGL.GLUT import *
from ..core import lighting


def draw_table_lamp():
    glPushMatrix()
    glTranslatef(-3.2, 0.75, -1.1)

    # ======================
    # BASE
    # ======================
    glColor3f(0.25, 0.25, 0.25)
    glPushMatrix()
    glScalef(0.25, 0.05, 0.25)
    glutSolidCube(1)
    glPopMatrix()

    # ======================
    # TIANG
    # ======================
    glColor3f(0.35, 0.35, 0.35)
    glPushMatrix()
    glTranslatef(0, 0.25, 0)
    glScalef(0.05, 0.5, 0.05)
    glutSolidCube(1)
    glPopMatrix()

    # ======================
    # KAP LAMPU (EMISSIVE)
    # ======================
    glPushMatrix()
    glTranslatef(0, 0.6, 0)
    glScalef(0.4, 0.3, 0.4)

    if lighting.bed_lamp_on:
        # 🔥 NYALA → KUNING TERANG
        glDisable(GL_LIGHTING)               # ← KUNCI UTAMA
        glColor3f(1.0, 0.85, 0.45)           # kuning hangat
    else:
        # MATI → ABU GELAP
        glColor3f(0.35, 0.35, 0.35)

    glutSolidSphere(0.5, 24, 24)

    if lighting.bed_lamp_on:
        glEnable(GL_LIGHTING)

    glPopMatrix()
    glPopMatrix()
