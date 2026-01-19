from OpenGL.GL import *


# =====================================================
# AC CENTRAL (DI ATAS KASUR)
# =====================================================
def draw_ac_central():
    glPushMatrix()

    # =================================================
    # POSISI & UKURAN
    # =================================================
    glTranslatef(-2.2, 3.15, -2.1)
    glScalef(0.45, 0.25, 0.45)

    glEnable(GL_LIGHTING)
    glEnable(GL_NORMALIZE)

    # =================================================
    # 1. FRAME LUAR (BEVEL)
    # =================================================
    glColor3f(0.95, 0.95, 0.95)

    def quad(x1, y1, z1, x2, y2, z2, nx, ny, nz):
        glNormal3f(nx, ny, nz)
        glVertex3f(x1, y1, z1)
        glVertex3f(x2, y1, z1)
        glVertex3f(x2, y2, z2)
        glVertex3f(x1, y2, z2)

    glBegin(GL_QUADS)

    # Top face
    quad(-1, 0.00, -1,  1, 0.00,  1, 0, 1, 0)

    # Bevel sides
    quad(-1, 0.00, -1, -0.9, -0.08,  1, -1, 0, 0)
    quad( 0.9, 0.00, -1,  1, -0.08,  1,  1, 0, 0)
    quad(-1, 0.00, -1,  1, -0.08, -0.9, 0, 0, -1)
    quad(-1, 0.00,  0.9,  1, -0.08,  1, 0, 0,  1)

    glEnd()

    # =================================================
    # 2. PANEL TENGAH (MENURUN)
    # =================================================
    glColor3f(0.90, 0.90, 0.90)
    glBegin(GL_QUADS)
    glNormal3f(0, 1, 0)
    glVertex3f(-0.75, -0.10, -0.75)
    glVertex3f( 0.75, -0.10, -0.75)
    glVertex3f( 0.75, -0.10,  0.75)
    glVertex3f(-0.75, -0.10,  0.75)
    glEnd()

    # =================================================
    # 3. GRILL TENGAH (MENJOROK KE DALAM)
    # =================================================
    glColor3f(0.15, 0.15, 0.15)

    for i in range(-18, 19):
        z = i * 0.035
        glBegin(GL_QUADS)
        glNormal3f(0, 1, 0)
        glVertex3f(-0.45, -0.16, z)
        glVertex3f( 0.45, -0.16, z)
        glVertex3f( 0.45, -0.20, z)
        glVertex3f(-0.45, -0.20, z)
        glEnd()

    # =================================================
    # 4. OUTLET UDARA (MENONJOL)
    # =================================================
    glColor3f(0.2, 0.2, 0.2)

    def outlet(x1, z1, x2, z2):
        glBegin(GL_QUADS)
        glNormal3f(0, 1, 0)
        glVertex3f(x1, -0.05, z1)
        glVertex3f(x2, -0.05, z1)
        glVertex3f(x2, -0.09, z2)
        glVertex3f(x1, -0.09, z2)
        glEnd()

    outlet(-0.65,  0.80,  0.65,  0.95)
    outlet(-0.65, -0.95,  0.65, -0.80)
    outlet( 0.80, -0.65,  0.95,  0.65)
    outlet(-0.95, -0.65, -0.80,  0.65)

    # =================================================
    # 5. PANEL KONTROL
    # =================================================
    glColor3f(0.85, 0.85, 0.85)
    glBegin(GL_QUADS)
    glNormal3f(0, 1, 0)
    glVertex3f(-0.18, -0.06, 0.55)
    glVertex3f( 0.18, -0.06, 0.55)
    glVertex3f( 0.18, -0.06, 0.75)
    glVertex3f(-0.18, -0.06, 0.75)
    glEnd()

    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_QUADS)
    glNormal3f(0, 1, 0)
    glVertex3f(-0.05, -0.07, 0.60)
    glVertex3f( 0.05, -0.07, 0.60)
    glVertex3f( 0.05, -0.07, 0.68)
    glVertex3f(-0.05, -0.07, 0.68)
    glEnd()

    glPopMatrix()

