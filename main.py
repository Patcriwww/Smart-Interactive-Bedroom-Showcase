from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# =========================
# CORE
# =========================
from smart_bedroom.core.camera import (
    apply_camera,
    move_camera,
    rotate_camera,
    focus_camera,
    FOCUS_POINTS,
    mouse_look
)

from smart_bedroom.core.lighting import (
    setup_lighting,
    toggle_day_night,
    toggle_main_lamp,
    toggle_bed_lamp,
    window_light_patch,
    window_grid_shadow
)

# =========================
# RENDER
# =========================
from smart_bedroom.render import texture as tex

# =========================
# OBJECTS
# =========================
from smart_bedroom.objects import (
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
    draw_wardrobe,
    toggle_wardrobe,
    update_wardrobe,
    draw_clock,
)

from smart_bedroom.objects.workstation import toggle_pc

# =========================
# UI
# =========================
from smart_bedroom.ui import draw_text, draw_hud_bg


# =========================
# STATE
# =========================
paused = False
poster_mode = 0


# =========================
# INIT
# =========================
def init():
    glClearColor(0.15, 0.15, 0.18, 1.0)
    glEnable(GL_DEPTH_TEST)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    tex.init_texture()

    glutPassiveMotionFunc(mouse_look)
    glutSetCursor(GLUT_CURSOR_NONE)


# =========================
# DISPLAY
# =========================
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    apply_camera()
    setup_lighting()

    # === ROOM ===
    tex.draw_room()
    tex.draw_rug()

    # === OBJECTS ===
    draw_wardrobe(tex.wood_tex)
    update_wardrobe()

    draw_window()
    draw_curtain()
    draw_door(tex.door_tex)

    draw_bed()
    draw_ac_central()  # ← AC CUSTOM KAMU

    draw_table()
    draw_table_lamp()
    draw_ceiling_lamp()

    draw_poster(tex.poster_1_tex)
    draw_poster_2(tex.poster_2_tex)
    draw_poster_3(tex.poster_3_tex)
    draw_poster_4(tex.poster_4_tex)


    draw_workstation()
    draw_bookshelf()
    draw_trash_bin()
    draw_plant()
    draw_clock()

    # === LIGHTING ===

    window_light_patch()
    window_grid_shadow()
    # =====================
    # HUD (2D)
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

    draw_hud_bg(8, h - 8, 650, 170, alpha=0.55)

    draw_text(15, h - 25, "SMART INTERACTIVE BEDROOM")
    draw_text(15, h - 40, "Kelompok 9 - Komputer Grafik")
    draw_text(15, h - 60, "Move : W A S D | Look : Mouse | Q / E Up Down")
    draw_text(15, h - 75, "Controls : O Wardrobe | N Day/Night | L Main Lamp | K Bed Lamp | P PC Power")

    draw_text(15, h - 100, "Camera Focus")
    draw_text(25, h - 120, "1 Bed   2 Table   3 Window   4 Wardrobe   5 Door")
    draw_text(25, h - 140, "6 Poster Cycle   7 Workstation   8 Bookshelf   9 Trash Bin")
    draw_text(25, h - 160, "0 Plant   T AC   J Clock   ESC Pause")

    # =====================
    # PAUSE
    # =====================
    is_fullscreen = False
    WINDOWED_SIZE = (900, 600)

    if paused:
        panel_w = 300
        panel_h = 140
        px = w // 2 - panel_w // 2
        py = h // 2 + 60

        draw_hud_bg(px, py, panel_w, panel_h, alpha=0.7)

        cx = px + panel_w // 2
        draw_text(cx - 25, py - 35, "PAUSED")
        draw_text(cx - 75, py - 65, "ESC Resume")
        draw_text(cx - 90, py - 90, "Enter to Exit")

    glEnable(GL_DEPTH_TEST)

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

    glutSwapBuffers()


# =========================
# INPUT
# =========================
is_fullscreen = False
WINDOWED_SIZE = (900, 600)

paused = False
poster_mode = 0

def keyboard(key, x, y):
    global paused, poster_mode, is_fullscreen

    # =====================
    # TOGGLE PAUSE (ESC)
    # =====================
    if key == b'\x1b':  # ESC
        paused = not paused
        return

    # =====================
    # SAAT PAUSE
    # =====================
    if paused:
        # ENTER = EXIT PROGRAM
        if key == b'\r':  # Enter
            try:
                glutLeaveMainLoop()
            except:
                pass
            sys.exit(0)

        # selain ENTER → semua input mati
        return

    # =====================
    # FULLSCREEN TOGGLE (F11)
    # =====================
    if key == b'\x7a':  # F11 (FreeGLUT Windows)
        if not is_fullscreen:
            glutFullScreen()
            is_fullscreen = True
        else:
            w, h = WINDOWED_SIZE
            glutReshapeWindow(w, h)
            glutPositionWindow(100, 100)
            is_fullscreen = False
        return

    # =====================
    # CAMERA MOVEMENT
    # =====================
    move_camera(key)

    # =====================
    # POSTER MODE (KEY 6)
    # =====================
    if key == b'6':
        poster_mode = (poster_mode + 1) % 4

        if poster_mode == 0:
            focus_camera([0.0, 2.1, 2.4], [0.0, 2.1, 3.98])       # Poster 1
        elif poster_mode == 1:
            focus_camera([-2.6, 2.0, 3.0], [-3.95, 2.0, 3.0])    # Poster 2
        elif poster_mode == 2:
            focus_camera([-1.5, 2.1, 2.4], [-1.5, 2.1, 3.98])    # Poster 3
        else:
            focus_camera([1.5, 2.1, 2.4], [1.5, 2.1, 3.98])      # Poster 4
        return

    # =====================
    # FOCUS OBJECTS
    # =====================
    if key in FOCUS_POINTS:
        data = FOCUS_POINTS[key]
        focus_camera(data["cam"], data["target"])
        return

    # =====================
    # INTERACTIONS
    # =====================
    if key == b'o':
        toggle_wardrobe()
    elif key == b'n':
        toggle_day_night()
    elif key == b'l':
        toggle_main_lamp()
    elif key == b'k':
        toggle_bed_lamp()
    elif key == b'p':
        toggle_pc()




def special_key(key, x, y):
    global is_fullscreen

    # =====================
    # FULLSCREEN TOGGLE (F11)
    # =====================
    if key == GLUT_KEY_F11:
        if not is_fullscreen:
            glutFullScreen()
            is_fullscreen = True
        else:
            w, h = WINDOWED_SIZE
            glutReshapeWindow(w, h)
            glutPositionWindow(100, 100)
            is_fullscreen = False
        return

    # =====================
    # BLOK INPUT SAAT PAUSE
    # =====================
    if paused:
        return

    rotate_camera(key)



# =========================
# WINDOW
# =========================
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


# =========================
# MAIN
# =========================
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
