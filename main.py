from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import texture

from camera import apply_camera, move_camera, rotate_camera, focus_camera, FOCUS_POINTS
from lighting import (
    setup_lighting,
    toggle_day_night,
    toggle_main_lamp,
    toggle_bed_lamp
)
from texture import init_texture, draw_room, draw_rug

from objects import (
    draw_bed,
    draw_table,
    draw_window,
    draw_door,
    draw_poster,
    draw_poster_2,
    draw_poster_3,
    draw_poster_4,
    draw_table_lamp,
    draw_curtain,
    draw_ceiling_lamp,
    draw_plant,
    draw_workstation,
    draw_bookshelf,
    draw_trash_bin,
    draw_ac_central,
    draw_window_light_patch,
    draw_window_grid_shadow  

)

from wardrobe import draw_wardrobe, toggle_wardrobe, update_wardrobe
from clock3d import draw_clock
from utils import draw_text, draw_hud_bg


# =====================
# INIT
# =====================
def init():
    glClearColor(0.15, 0.15, 0.18, 1.0)
    glEnable(GL_DEPTH_TEST)

    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    init_texture()

# =====================
# DISPLAY
# =====================
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    apply_camera()

    # === LIGHTING ===
    setup_lighting()

    # === ROOM ===
    draw_room()
    draw_rug()
    draw_window_light_patch() 
    draw_window_grid_shadow() 

    # === FURNITURE & OBJECTS ===
    draw_wardrobe(texture.wood_tex)
    update_wardrobe()

    draw_window()
    draw_door(texture.door_tex)

    draw_bed()
    draw_ac_central()        # AC di atas kasur

    draw_table()
    draw_table_lamp()
    draw_ceiling_lamp()

    draw_poster(texture.poster_tex)
    draw_poster_2(texture.poster2_tex)
    draw_poster_3(texture.poster3_tex)
    draw_poster_4(texture.poster4_tex)

    draw_curtain()
    draw_workstation()
    draw_bookshelf()
    draw_trash_bin()
    draw_plant()
    draw_clock()


    # =====================
    # HUD (2D OVERLAY)
    # =====================
    w, h = get_window_size()

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glDisable(GL_DEPTH_TEST)
    glDisable(GL_LIGHTING)

    draw_hud_bg(
        x=8,
        y=h - 8,
        w=650,
        h=165,
        alpha=0.55
    )

    draw_text(15, h - 25, "SMART INTERACTIVE BEDROOM")
    draw_text(15, h - 40, "Kelompok 9 - Komputer Grafik")
    draw_text(15, h - 60, "Move : W A S D | Look : Arrow Keys | Q / E Up Down")
    draw_text(15, h - 75, "Controls : O Wardrobe | N Day/Night | L Ceiling Lamp | K Night Lamp | ESC Exit")

    draw_text(15, h - 100, "Camera Focus")
    draw_text(25, h - 120, "1 Bed   2 Table   3 Window   4 Wardrobe   5 Door")
    draw_text(25, h - 140, "6 Poster   7 Workstation   8 Bookshelf   9 Trash Bin")
    draw_text(25, h - 160, "0 Plant   C Ceiling Lamp   R Rug   J Clock  T AC")

    

    glEnable(GL_DEPTH_TEST)

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

    glutSwapBuffers()


# =====================
# INPUT
# =====================
def keyboard(key, x, y):
    move_camera(key)

    if key in FOCUS_POINTS:
        data = FOCUS_POINTS[key]
        focus_camera(data["cam"], data["target"])
    if key == b'o':
        toggle_wardrobe()
    if key == b'n':
        toggle_day_night()
    if key == b'l':
        toggle_main_lamp()
    if key == b'k':
        toggle_bed_lamp()
    elif key == b'\x1b':
        try:
            glutLeaveMainLoop()
        except:
            pass
        sys.exit(0)


def special_key(key, x, y):
    rotate_camera(key)


# =====================
# WINDOW
# =====================
def reshape(w, h):
    if h == 0:
        h = 1

    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, w / h, 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)


def get_window_size():
    return glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)


# =====================
# MAIN
# =====================
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(900, 600)
    glutCreateWindow(b"Smart Interactive Bedroom Showcase")

    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_key)
    glutIdleFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    main()
