from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from smart_bedroom.core.camera import apply_camera, move_camera, rotate_camera, focus_camera, FOCUS_POINTS, mouse_look
from smart_bedroom.core.lighting import setup_lighting, toggle_day_night, toggle_lamp
from smart_bedroom.render import texture as tex
from smart_bedroom.objects import (
    draw_bed,
    draw_table,
    draw_window,
    draw_door,
    draw_poster,
    draw_table_lamp,
    draw_curtain,
    draw_ceiling_lamp,
    draw_plant,
    draw_workstation,
    draw_bookshelf,
    draw_trash_bin,
    draw_wardrobe,
    toggle_wardrobe,
    update_wardrobe,
    draw_clock,
)
from smart_bedroom.ui import draw_text, draw_hud_bg

def init():
    glClearColor(0.15, 0.15, 0.18, 1.0)
    glEnable(GL_DEPTH_TEST)
    tex.init_texture()
    
    glutPassiveMotionFunc(mouse_look)
    glutSetCursor(GLUT_CURSOR_NONE)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    apply_camera()
    setup_lighting()
    tex.draw_room()
    tex.draw_rug()
    draw_wardrobe(tex.wood_tex)
    draw_window()
    draw_door(tex.door_tex) 
    draw_bed()
    draw_table()
    draw_table_lamp()
    draw_ceiling_lamp()
    update_wardrobe()
    draw_poster(tex.poster_tex)
    
    draw_plant()

    draw_workstation()

    draw_clock()

    draw_curtain()

    draw_bookshelf()

    draw_trash_bin()

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

    # ===== HUD BACKGROUND =====
    h = glutGet(GLUT_WINDOW_HEIGHT)

    draw_hud_bg(
        x=8,
        y=h - 8,
        w=635,
        h=140,
        alpha=0.55
    )

    draw_text(15, h - 25, "SMART INTERACTIVE BEDROOM")
    draw_text(15, h - 38, "Kelompok 9 - Komputer Grafik")
    draw_text(15, h - 55, "Movement : W A S D | Look : Arrow Keys | Q / E Up Down")
    draw_text(15, h - 70, "Controls : O Wardrobe | N Day/Night | L Ceiling Lamp | ESC Exit")

    draw_text(15, h - 95, "Camera Focus")
    draw_text(25, h - 115, "1 Bed   2 Table   3 Window   4 Wardrobe   5 Door    6 Poster   7 Workstation")
    draw_text(25, h - 135, "8 Bookshelf   9 Trash Bin   0 Plant   C Ceiling Lamp   R Rug    J Clock")


    # STATE
    glEnable(GL_DEPTH_TEST)

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

    glutSwapBuffers()

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
        toggle_lamp()   
    elif key == b'\x1b':
        try:
            glutLeaveMainLoop()
        except:
            pass
        sys.exit(0)

def special_key(key, x, y):
    rotate_camera(key)

def reshape(w, h):
    if h == 0:
        h = 1

    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, w / h, 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(900, 600)
    glutCreateWindow(b"Bedroom Showcase")

    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_key)
    glutIdleFunc(display)
    glutMainLoop()

def get_window_size():
    return glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)

if __name__ == "__main__":
    main()
