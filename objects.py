from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

curtain_open = None

# =====================================================
# BED 
# =====================================================
def draw_bed():
    glPushMatrix()
    glTranslatef(-2.2, 0.0, -2.1)   

    # Base
    glColor3f(0.45, 0.25, 0.15)
    glPushMatrix()
    glTranslatef(0, 0.3, 0)
    glScalef(2.2, 0.6, 1.4)
    glutSolidCube(1)
    glPopMatrix()

    # Mattress
    glColor3f(0.95, 0.95, 0.9)
    glPushMatrix()
    glTranslatef(0, 0.7, 0)
    glScalef(2.1, 0.3, 1.3)
    glutSolidCube(1)
    glPopMatrix()

    # Headboard
    glColor3f(0.9, 0.9, 0.6)
    glPushMatrix()
    glTranslatef(-1.15, 0.95, 0)
    glScalef(0.15, 1.4, 1.4)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()


# =====================================================
# TABLE 
# =====================================================
def draw_table():
    glPushMatrix()

    glTranslatef(-3.2, 0.0, -1.1) 

    # Table top
    glColor3f(0.55, 0.35, 0.25)
    glPushMatrix()
    glTranslatef(0, 0.6, 0)
    glScalef(0.6, 0.1, 0.6)
    glutSolidCube(1)
    glPopMatrix()

    # Legs
    glColor3f(0.4, 0.25, 0.15)
    for x in [-0.22, 0.22]:
        for z in [-0.22, 0.22]:
            glPushMatrix()
            glTranslatef(x, 0.3, z)
            glScalef(0.08, 0.6, 0.08)
            glutSolidCube(1)
            glPopMatrix()

    glPopMatrix()


# =====================================================
# WINDOW (WITH OUTSIDE TEXTURE)
# =====================================================
def draw_window():
    from lighting import is_day
    from texture import city_day_tex, city_night_tex

    glDisable(GL_LIGHTING)

    # ===============================
    # POSISI JENDELA 
    # ===============================
    z = -3.99
    y_bottom = 1.4
    y_top    = 2.7
    x_left   = -1.0
    x_right  =  1.0

    # ===============================
    # FRAME LUAR
    # ===============================
    glColor3f(0.95, 0.95, 0.95)
    glBegin(GL_QUADS)
    glVertex3f(x_left,  y_bottom, z)
    glVertex3f(x_right, y_bottom, z)
    glVertex3f(x_right, y_top,    z)
    glVertex3f(x_left,  y_top,    z)
    glEnd()

    # ===============================
    # FRAME DALAM
    # ===============================
    inset = 0.08
    glColor3f(0.85, 0.85, 0.85)
    glBegin(GL_QUADS)
    glVertex3f(x_left+inset,  y_bottom+inset, z+0.001)
    glVertex3f(x_right-inset, y_bottom+inset, z+0.001)
    glVertex3f(x_right-inset, y_top-inset,    z+0.001)
    glVertex3f(x_left+inset,  y_top-inset,    z+0.001)
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
    glTexCoord2f(0,0); glVertex3f(x_left+glass_inset,  y_bottom+glass_inset, z+0.002)
    glTexCoord2f(1,0); glVertex3f(x_right-glass_inset, y_bottom+glass_inset, z+0.002)
    glTexCoord2f(1,1); glVertex3f(x_right-glass_inset, y_top-glass_inset,    z+0.002)
    glTexCoord2f(0,1); glVertex3f(x_left+glass_inset,  y_top-glass_inset,    z+0.002)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)

    # ===============================
    # PEMBAGI KACA (CROSS)
    # ===============================
    glColor3f(0.75, 0.75, 0.75)
    glLineWidth(3)

    glBegin(GL_LINES)
    glVertex3f(0.0, y_bottom+glass_inset, z+0.003)
    glVertex3f(0.0, y_top-glass_inset,    z+0.003)

    glVertex3f(x_left+glass_inset, (y_bottom+y_top)/2, z+0.003)
    glVertex3f(x_right-glass_inset,(y_bottom+y_top)/2, z+0.003)
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
        glVertex3f(x_left + 0.25,  y0, z0)
        glVertex3f(x_right - 0.25, y0, z0)
        glVertex3f(x_right + 2.4,  y1, z1)
        glVertex3f(x_left  - 2.4,  y1, z1)
        glEnd()

        glDepthMask(GL_TRUE)
        glEnable(GL_DEPTH_TEST)
        glDisable(GL_BLEND)

        glEnable(GL_LIGHTING)


# =====================================================
# DOOR 
# =====================================================
def draw_door(tex_id):
    if tex_id is None:
        return

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glColor3f(1, 1, 1)

    glPushMatrix()

    glTranslatef(3.95, 0.0, 2.0)   
    glRotatef(-90, 0, 1, 0)         

    door_width  = 1.3
    door_height = 2.5
    thickness   = 0.03

    glBegin(GL_QUADS)

    # TEXTURE DOOR.JPG
    glTexCoord2f(0, 0); glVertex3f(0, 0, thickness)
    glTexCoord2f(1, 0); glVertex3f(door_width, 0, thickness)
    glTexCoord2f(1, 1); glVertex3f(door_width, door_height, thickness)
    glTexCoord2f(0, 1); glVertex3f(0, door_height, thickness)

    glEnd()

    glPopMatrix()

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)


# =====================================================
# POSTER
# =====================================================
def draw_poster(tex_id):
    if tex_id is None:
        return

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glColor3f(1, 1, 1)

    glPushMatrix()

    glTranslatef(0.0, 1.4, 3.98)
    glRotatef(180, 0, 1, 0)

    w = 1.2
    h = 1.4
    z = 0.02

    glBegin(GL_QUADS)

    glTexCoord2f(0.0, 0.0); glVertex3f(-w/2, 0,  z)
    glTexCoord2f(1.0, 0.0); glVertex3f( w/2, 0,  z)
    glTexCoord2f(1.0, 1.0); glVertex3f( w/2, h,  z)
    glTexCoord2f(0.0, 1.0); glVertex3f(-w/2, h,  z)

    glEnd()

    glPopMatrix()
    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)


# =====================================================
# TABLE LAMP
# =====================================================
def draw_table_lamp():
    from lighting import is_day

    glPushMatrix()

    # posisi lampu di atas meja
    glTranslatef(-3.2, 0.75, -1.1)

    # ======================
    # BASE
    # ======================
    glColor3f(0.2, 0.2, 0.2)
    glPushMatrix()
    glScalef(0.25, 0.05, 0.25)
    glutSolidCube(1)
    glPopMatrix()

    # ======================
    # POLE
    # ======================
    glColor3f(0.3, 0.3, 0.3)
    glPushMatrix()
    glTranslatef(0, 0.25, 0)
    glScalef(0.05, 0.5, 0.05)
    glutSolidCube(1)
    glPopMatrix()

    # ======================
    # LAMP SHADE
    # ======================
    if is_day:
        glColor3f(0.7, 0.7, 0.7)   # mati
    else:
        glColor3f(1.0, 0.9, 0.6)   # nyala kuning

        glDisable(GL_LIGHTING)

    glPushMatrix()
    glTranslatef(0, 0.6, 0)
    glScalef(0.4, 0.3, 0.4)
    glutSolidSphere(0.5, 24, 24)
    glPopMatrix()

    if not is_day:
        glEnable(GL_LIGHTING)

    glPopMatrix()


# =====================================================
# CURTAIN
# =====================================================
def draw_curtain():

    from lighting import is_day
    from texture import curtain_tex
    import math

    if curtain_tex is None:
        return

    # ===============================
    # LOGIKA FINAL 
    # ===============================
    if curtain_open is None:
        cover = 0.35 if is_day else 1.0
    else:
        cover = curtain_open             

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, curtain_tex)
    glDisable(GL_LIGHTING)
    glColor3f(1, 1, 1)

    # POSISI WINDOW
    z = -3.97
    y_bottom = 1.4
    y_top = 2.7
    x_left = -1.0
    x_right = 1.0

    folds = 14
    wave_amp = 0.07

    step = cover / folds   

    # ===============================
    # GORDEN KIRI
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
    # GORDEN KANAN
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

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING)


# =====================================================
# CEILING LAMP (BOHLAM PLAFON)
# =====================================================
def draw_ceiling_lamp():
    from lighting import setup_lighting
    import math

    glDisable(GL_TEXTURE_2D)
    glDisable(GL_LIGHTING)

    glPushMatrix()

     # =========================
    # POSISI TENGAH RUANGAN
    # =========================
    glTranslatef(0.0, 3.18, 0.0)

    # =========================
    # WARNA LAMPU
    # =========================
    if setup_lighting:
        glColor3f(1.0, 0.95, 0.8)   # nyala
    else:
        glColor3f(0.4, 0.4, 0.4)    # mati

    radius = 0.22
    segments = 32

    # =========================
    # LAMPU (LINGKARAN HADAP BAWAH)
    # =========================
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, 0.0, 0.0)  

    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        glVertex3f(x, 0.0, z)

    glEnd()

    # =========================
    # RING TIPIS (FRAME)
    # =========================
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        glVertex3f(x, 0.001, z)
    glEnd()

    glPopMatrix()

    glEnable(GL_LIGHTING)

#==================================
# POHON
#==================================
from OpenGL.GL import *
import math

def draw_plant():
    glDisable(GL_LIGHTING)

    # ===============================
    # TRANSFORM UTAMA
    # ===============================
    glPushMatrix()
    glTranslatef(-3.6, 0.0, 3.6)

    # ===============================
    # POT
    # ===============================
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

    # ===============================
    # TANAH
    # ===============================
    glColor3f(0.35, 0.25, 0.15)
    glBegin(GL_POLYGON)
    for i in range(segments):
        a = 2 * math.pi * i / segments
        glVertex3f(math.cos(a) * 0.22, pot_h, math.sin(a) * 0.22)
    glEnd()

    # ===============================
    # BATANG 
    # ===============================
    glColor3f(0.3, 0.5, 0.3)
    trunk_h = 0.28
    trunk_offset = -0.06
    trunk_r = 0.040   

    glBegin(GL_QUADS)
    glVertex3f(-trunk_r, pot_h + trunk_offset, 0.0)
    glVertex3f( trunk_r, pot_h + trunk_offset, 0.0)
    glVertex3f( trunk_r, pot_h + trunk_h + trunk_offset, 0.0)
    glVertex3f(-trunk_r, pot_h + trunk_h + trunk_offset, 0.0)
    glEnd()

    # ===============================
    # DAUN MELENGKUNG 
    # ===============================
    glColor3f(0.18, 0.65, 0.30)

    leaf_base_y = pot_h + trunk_h + trunk_offset - 0.05
    leaf_count = 10
    leaf_length = 0.34      
    leaf_width  = 0.065
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
            glVertex3f( leaf_width, 0.0, 0.0)
            glVertex3f( leaf_width * 0.6, seg_len, 0.0)
            glVertex3f(-leaf_width * 0.6, seg_len, 0.0)
            glEnd()

        glPopMatrix()

    glPopMatrix()     
    glPopMatrix()      
    glEnable(GL_LIGHTING)


# =====================================================
# WORKSTATION (MEJA + KURSI + PC)
# =====================================================
def draw_workstation():
    glPushMatrix()

    # ===============================
    # POSISI SET 
    # ===============================
    glTranslatef(-3.3, 0.0, 1.2)
    glRotatef(90, 0, 1, 0)

    # =================================================
    # MEJA
    # =================================================
    # Top
    glColor3f(0.42, 0.28, 0.15)
    glPushMatrix()
    glTranslatef(0.0, 0.75, 0.0)
    glScalef(1.2, 0.08, 0.6)
    glutSolidCube(1)
    glPopMatrix()

    # Kaki meja
    glColor3f(0.30, 0.20, 0.12)
    for x in [-0.5, 0.5]:
        for z in [-0.25, 0.25]:
            glPushMatrix()
            glTranslatef(x, 0.38, z)
            glScalef(0.08, 0.75, 0.08)
            glutSolidCube(1)
            glPopMatrix()

    # =================================================
    # PC DESKTOP (MONITOR + CPU + KEYBOARD + MOUSE)
    # =================================================

    # ===============================
    # MONITOR
    # ===============================
    glPushMatrix()
    glTranslatef(0.0, 1.10, -0.18)

    # Stand
    glColor3f(0.2, 0.2, 0.2)
    glPushMatrix()
    glTranslatef(0.0, -0.14, 0.0)
    glScalef(0.08, 0.24, 0.03)
    glutSolidCube(1)
    glPopMatrix()

    # Base stand
    glPushMatrix()
    glTranslatef(0.0, -0.28, 0.05)
    glScalef(0.25, 0.03, 0.18)
    glutSolidCube(1)
    glPopMatrix()

    # Monitor frame
    glColor3f(0.05, 0.05, 0.05)
    glPushMatrix()
    glScalef(0.55, 0.35, 0.04)
    glutSolidCube(1)
    glPopMatrix()

    # Screen (nyala)
    glDisable(GL_LIGHTING)
    glColor3f(0.1, 0.3, 0.45)   
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.03)
    glScalef(0.48, 0.28, 0.01)
    glutSolidCube(1)
    glPopMatrix()
    glEnable(GL_LIGHTING)

    glPopMatrix()  


    # ===============================
    # KEYBOARD
    # ===============================
    glColor3f(0.10, 0.10, 0.10)
    glPushMatrix()
    glTranslatef(0.0, 0.82, 0.05)
    glScalef(0.45, 0.03, 0.18)
    glutSolidCube(1)
    glPopMatrix()


    # ===============================
    # MOUSE
    # ===============================
    glColor3f(0.08, 0.08, 0.08)
    glPushMatrix()
    glTranslatef(0.30, 0.83, 0.05)
    glScalef(0.08, 0.03, 0.12)
    glutSolidCube(1)
    glPopMatrix()


    # ===============================
    # CPU CASE (TOWER)
    # ===============================
    glColor3f(0.12, 0.12, 0.12)
    glPushMatrix()
    glTranslatef(0.75, 0.25, 0.0)
    glScalef(0.28, 0.9, 0.45)
    glutSolidCube(1)
    glPopMatrix()
    
    # =================================================
    # KURSI
    # =================================================
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.55)

    # Dudukan
    glColor3f(0.18, 0.18, 0.18)
    glPushMatrix()
    glTranslatef(0.0, 0.45, 0.0)
    glScalef(0.5, 0.08, 0.5)
    glutSolidCube(1)
    glPopMatrix()

    # Sandaran
    glPushMatrix()
    glTranslatef(0.0, 0.75, 0.22)
    glScalef(0.5, 0.6, 0.08)
    glutSolidCube(1)
    glPopMatrix()

    # Kaki kursi
    for x in [-0.18, 0.18]:
        for z in [-0.18, 0.18]:
            glPushMatrix()
            glTranslatef(x, 0.22, z)
            glScalef(0.06, 0.45, 0.06)
            glutSolidCube(1)
            glPopMatrix()

    glPopMatrix()  

    glPopMatrix()


# =====================================================
# WALL MOUNTED BOOKSHELF (TEMPEL DINDING)
# =====================================================
def draw_bookshelf():
    glPushMatrix()

    # ===============================
    # POSISI (TEMPEL DINDING)
    # ===============================
    glTranslatef(3.75, 2.1, 0.55)  
    glRotatef(90, 0, 1, 0)

    shelf_width = 1.6
    shelf_depth = 0.25
    shelf_thick = 0.05

    # ===============================
    # PAPAN RAK 
    # ===============================
    glColor3f(0.28, 0.18, 0.10)   

    for y in [0.0, -0.45, -0.9]:
        glPushMatrix()
        glTranslatef(0.0, y, 0.0)
        glScalef(shelf_width, shelf_thick, shelf_depth)
        glutSolidCube(1)
        glPopMatrix()

    # ===============================
    # SISI KIRI & KANAN
    # ===============================
    glColor3f(0.35, 0.23, 0.14)

    for x in [-shelf_width/2 + 0.03, shelf_width/2 - 0.03]:
        glPushMatrix()
        glTranslatef(x, -0.45, 0.0)
        glScalef(0.05, 1.0, shelf_depth)
        glutSolidCube(1)
        glPopMatrix()

    # ===============================
    # BUKU-BUKU
    # ===============================
    book_colors = [
        (0.35, 0.22, 0.18),  # maroon gelap
        (0.22, 0.30, 0.40),  # biru navy pudar
        (0.25, 0.35, 0.28),  # hijau zaitun
        (0.40, 0.32, 0.18),  # coklat mustard
        (0.30, 0.22, 0.35),  # ungu gelap
        (0.38, 0.28, 0.22),  # coklat tua
    ]

    def draw_books_row(y_level):
        x_start = -0.65
        for i in range(10):
            glColor3f(*book_colors[i % len(book_colors)])
            glPushMatrix()
            glTranslatef(x_start + i * 0.14, y_level + 0.18, 0.0)
            glScalef(0.1, 0.32, 0.18)
            glutSolidCube(1)
            glPopMatrix()

    draw_books_row(0.0)
    draw_books_row(-0.45)
    draw_books_row(-0.9)  

    glPopMatrix()


# ===============================
# TONG SAMPAH
# ===============================
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_trash_bin():
    glPushMatrix()

    # ===============================
    # POSISI 
    # ===============================
    glTranslatef(3.75, 0.0, 1.55)  

    radius = 0.18
    height = 0.45
    segments = 24

    # ===============================
    # BODY TONG
    # ===============================
    glColor3f(0.15, 0.15, 0.15)   

    glBegin(GL_QUAD_STRIP)
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        x = math.cos(angle) * radius
        z = math.sin(angle) * radius
        glVertex3f(x, 0.0, z)
        glVertex3f(x, height, z)
    glEnd()

    # ===============================
    # DASAR TONG
    # ===============================
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, 0.0, 0.0)
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        glVertex3f(
            math.cos(angle) * radius,
            0.0,
            math.sin(angle) * radius
        )
    glEnd()

    # ===============================
    # TUTUP
    # ===============================
    glColor3f(0.10, 0.10, 0.10)

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, height + 0.02, 0.0)
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        glVertex3f(
            math.cos(angle) * (radius + 0.02),
            height + 0.02,
            math.sin(angle) * (radius + 0.02)
        )
    glEnd()

    glPopMatrix()


# =====================================================
# CENTRAL AC (CEILING) 
# =====================================================
def draw_central_ac():
    from texture import ac_tex

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
    glTexCoord2f(0, 0); glVertex3f(-size + offset_x, y, -size + offset_z)
    glTexCoord2f(1, 0); glVertex3f( size + offset_x, y, -size + offset_z)
    glTexCoord2f(1, 1); glVertex3f( size + offset_x, y,  size + offset_z)
    glTexCoord2f(0, 1); glVertex3f(-size + offset_x, y,  size + offset_z)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING)


# =====================================================
# POSTER 2 
# =====================================================
def draw_poster_2():
    from texture import poster_tex_2

    if poster_tex_2 is None:
        return

    glDisable(GL_LIGHTING)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, poster_tex_2)
    glColor3f(1, 1, 1)

    w = 0.9
    h = 1.3

    x = -3.95
    y = 0.5
    z = 0.5 + 1.0  

    glPushMatrix()
    glTranslatef(-3.95, 2.0, 3.0)
    glRotatef(90, 0, 1, 0)   

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(0,     -h/2, 0)
    glTexCoord2f(1, 0); glVertex3f(w,     -h/2, 0)
    glTexCoord2f(1, 1); glVertex3f(w,      h/2, 0)
    glTexCoord2f(0, 1); glVertex3f(0,      h/2, 0)
    glEnd()

    glPopMatrix()

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING)
