import os
from OpenGL.GL import *
from PIL import Image

# =========================
# BASE DIRECTORY
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
TEXTURE_DIR = os.path.join(BASE_DIR, "textures")

# =========================
# GLOBAL TEXTURE HANDLES
# =========================
floor_tex = None
wall_tex  = None
rug_tex   = None
wood_tex  = None
door_tex  = None
curtain_tex = None
ac_tex = None

# Posters
poster_1_tex = None
poster_2_tex = None
poster_3_tex = None
poster_4_tex = None

# City
city_day_tex = None
city_night_tex = None

# PC screens
pc_boot_tex = None
pc_home_tex = None
pc_shutdown_tex = None



# =========================
# LOAD TEXTURE HELPER
# =========================
def load_texture(filename):
    path = os.path.join(TEXTURE_DIR, filename)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Texture not found: {path}")

    img = Image.open(path)
    
    # Handle both RGB and RGBA
    if img.mode == 'RGBA':
        img_format = GL_RGBA
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        data = img.tobytes()
    else:
        img_format = GL_RGB
        img = img.convert("RGB")
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        data = img.tobytes()

    tex = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex)

    glTexImage2D(
        GL_TEXTURE_2D, 0, img_format,
        img.width, img.height, 0,
        img_format, GL_UNSIGNED_BYTE, data
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
    global door_tex, curtain_tex, ac_tex
    global poster_1_tex, poster_2_tex, poster_3_tex, poster_4_tex
    global city_day_tex, city_night_tex
    global pc_boot_tex, pc_home_tex, pc_shutdown_tex

    floor_tex   = load_texture("floor.jpg")
    wall_tex    = load_texture("wall.jpg")
    rug_tex     = load_texture("rug.jpg")
    wood_tex    = load_texture("wood.jpg")
    door_tex    = load_texture("door.jpg")
    curtain_tex = load_texture("curtain.jpg")
    ac_tex      = load_texture("ac.jpg")

    poster_1_tex = load_texture("poster_1.jpg")
    poster_2_tex = load_texture("poster_2.jpg")
    poster_3_tex = load_texture("poster_3.jpg")
    poster_4_tex = load_texture("poster_4.jpg")

    city_day_tex   = load_texture("city_day.jpg")
    city_night_tex = load_texture("city_night.jpg")

    pc_boot_tex     = load_texture("pc_boot.png")
    pc_home_tex     = load_texture("pc_home.png")
    pc_shutdown_tex = load_texture("pc_shutdown.png")




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
