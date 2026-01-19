import os

from OpenGL.GL import *
from PIL import Image

# =========================
# GLOBAL TEXTURE HANDLES
# =========================
floor_tex = None
wall_tex  = None
rug_tex   = None
wood_tex  = None
door_tex  = None
poster_tex = None
curtain_tex = None
ac_tex = None   # <<< TAMBAHAN


# =========================
# LOAD TEXTURE HELPER
# =========================
def load_texture(path):
    img = Image.open(path).convert("RGB")
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    data = img.tobytes()

    tex = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex)

    glTexImage2D(
        GL_TEXTURE_2D, 0, GL_RGB,
        img.width, img.height, 0,
        GL_RGB, GL_UNSIGNED_BYTE, data
    )

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    glBindTexture(GL_TEXTURE_2D, 0)
    return tex


# =========================
# INIT ALL TEXTURES
# =========================
def init_texture():
    global floor_tex, wall_tex, rug_tex, wood_tex
    global door_tex, poster_tex, curtain_tex, ac_tex
    global poster2_tex, poster3_tex, poster4_tex, curtain_tex


    floor_tex   = load_texture("textures/floor.jpg")
    wall_tex    = load_texture("textures/wall.jpg")
    rug_tex     = load_texture("textures/rug.jpg")
    wood_tex    = load_texture("textures/wood.jpg")
    door_tex    = load_texture("textures/door.jpg")
    poster_tex  = load_texture("textures/poster.jpg")
    poster2_tex = load_texture("textures/poster2.jpg")
    poster3_tex = load_texture("textures/poster3.jpg")
    poster4_tex = load_texture("textures/poster_4.jpg")

    curtain_tex = load_texture("textures/curtain.jpg")

    ac_tex      = load_texture("textures/ac.jpg")   # ← INI



# =========================
# DRAW ROOM (FLOOR + WALL)
# =========================
def draw_room():
    size = 4
    height = 3

    glEnable(GL_TEXTURE_2D)

    # FLOOR
    glBindTexture(GL_TEXTURE_2D, floor_tex)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-size, 0, -size)
    glTexCoord2f(4, 0); glVertex3f( size, 0, -size)
    glTexCoord2f(4, 4); glVertex3f( size, 0,  size)
    glTexCoord2f(0, 4); glVertex3f(-size, 0,  size)
    glEnd()

    # WALLS
    glBindTexture(GL_TEXTURE_2D, wall_tex)
    walls = [
        [(-size,0,-size),( size,0,-size),( size,height,-size),(-size,height,-size)],
        [(-size,0,size),( size,0,size),( size,height,size),(-size,height,size)],
        [(-size,0,-size),(-size,0,size),(-size,height,size),(-size,height,-size)],
        [( size,0,-size),( size,0,size),( size,height,size),( size,height,-size)]
    ]

    for w in walls:
        glBegin(GL_QUADS)
        glTexCoord2f(0,0); glVertex3f(*w[0])
        glTexCoord2f(4,0); glVertex3f(*w[1])
        glTexCoord2f(4,3); glVertex3f(*w[2])
        glTexCoord2f(0,3); glVertex3f(*w[3])
        glEnd()

    glDisable(GL_TEXTURE_2D)


# =========================
# DRAW RUG
# =========================
def draw_rug():
    if rug_tex is None:
        return

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, rug_tex)

    y = 0.01
    rug_w = 1.6
    rug_d = 1.2

    glBegin(GL_QUADS)
    glTexCoord2f(0,0); glVertex3f(-rug_w, y, -rug_d)
    glTexCoord2f(1,0); glVertex3f( rug_w, y, -rug_d)
    glTexCoord2f(1,1); glVertex3f( rug_w, y,  rug_d)
    glTexCoord2f(0,1); glVertex3f(-rug_w, y,  rug_d)
    glEnd()

    glDisable(GL_TEXTURE_2D)
