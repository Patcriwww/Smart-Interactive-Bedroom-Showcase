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
from smart_bedroom.ui import draw_text, draw_hud_bg, draw_text_centered


# =========================
# STATE
# =========================
paused = False
poster_mode = 0
pause_menu_selected = 0  # 0 = Resume, 1 = Exit
mouse_x = 0
mouse_y = 0


# =========================
# INIT
# =========================
def mouse_look_wrapper(x, y):
    """Track mouse position for pause menu clicks"""
    global mouse_x, mouse_y
    mouse_x = x
    mouse_y = y
    
    # Only do mouse look when not paused
    if not paused:
        mouse_look(x, y, is_paused=False)


def mouse_click(button, state, x, y):
    """Handle mouse clicks in pause menu"""
    global paused, pause_menu_selected
    
    if not paused or button != GLUT_LEFT_BUTTON or state != GLUT_DOWN:
        return
    
    # Pause menu dimensions (same as in display)
    w = glutGet(GLUT_WINDOW_WIDTH)
    h = glutGet(GLUT_WINDOW_HEIGHT)
    panel_w = 300
    panel_h = 140
    px = w // 2 - panel_w // 2
    py = h // 2 + 60
    
    # Convert OpenGL coordinates to screen coordinates (y is flipped)
    screen_y = h - y
    
    # Resume option at py - 65
    resume_y = py - 65
    if abs(screen_y - resume_y) < 10 and px < x < px + panel_w:
        pause_menu_selected = 0
        paused = False
        glutSetCursor(GLUT_CURSOR_NONE)  # Hide cursor
        return
    
    # Exit option at py - 90
    exit_y = py - 90
    if abs(screen_y - exit_y) < 10 and px < x < px + panel_w:
        pause_menu_selected = 1
        try:
            glutLeaveMainLoop()
        except:
            pass
        import sys
        sys.exit(0)


def init():
    glClearColor(0.15, 0.15, 0.18, 1.0)
    glEnable(GL_DEPTH_TEST)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    tex.init_texture()

    glutPassiveMotionFunc(mouse_look_wrapper)
    glutMouseFunc(mouse_click)
    glutSetCursor(GLUT_CURSOR_NONE)


# =========================
# DISPLAY
# =========================
def display():
    global pause_menu_selected
    
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

    draw_hud_bg(8, h - 8, 650, 200, alpha=0.60)

    draw_text(15, h - 20, "SMART INTERACTIVE BEDROOM")
    draw_text(15, h - 40, "Kelompok 9 - Komputer Grafik IF23H")
    draw_text(15, h - 60, "Anggota : Alamsyah H, Ariq Gymnastiar P, Fachri Reyhan, Ralf Fadila")
    draw_text(15, h - 80, "Move : W A S D | Look : Mouse | Q / E Up Down")
    draw_text(15, h - 100, "Controls : O Wardrobe | N Day/Night | L Main Lamp | K Bed Lamp | P PC Power")

    draw_text(15, h - 120, "Camera Focus")
    draw_text(25, h - 140, "1 Bed   2 Table   3 Window   4 Wardrobe   5 Door")
    draw_text(25, h - 160, "6 Poster Cycle   7 Workstation   8 Bookshelf   9 Trash Bin")
    draw_text(25, h - 180, "0 Plant   T AC   J Clock   ESC Pause")

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
        draw_text_centered(cx, py - 35, "PAUSED")
        
        # Resume option
        resume_text = ">> Resume <<" if pause_menu_selected == 0 else "   Resume   "
        glColor3f(1.0, 1.0, 1.0)
        draw_text_centered(cx, py - 65, resume_text)
        
        # Exit option
        exit_text = ">> Exit <<" if pause_menu_selected == 1 else "   Exit   "
        draw_text_centered(cx, py - 90, exit_text)

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


def mouse_look_wrapper(x, y):
    """Wrapper to pass paused state to mouse_look"""
    mouse_look(x, y, is_paused=paused)

paused = False
poster_mode = 0

def keyboard(key, x, y):
    global paused, poster_mode, is_fullscreen, pause_menu_selected

    # =====================
    # TOGGLE PAUSE (ESC)
    # =====================
    if key == b'\x1b':  # ESC
        if paused:
            paused = False
            glutSetCursor(GLUT_CURSOR_NONE)  # Hide cursor when resuming
        else:
            paused = True
            pause_menu_selected = 0  # Reset to Resume option
            glutSetCursor(GLUT_CURSOR_CROSSHAIR)  # Show cursor for menu
        return

    # =====================
    # SAAT PAUSE
    # =====================
    if paused:
        # ENTER = SELECT OPTION
        if key == b'\r':  # Enter
            if pause_menu_selected == 0:  # Resume
                paused = False
                glutSetCursor(GLUT_CURSOR_NONE)  # Hide cursor
            else:  # Exit
                try:
                    glutLeaveMainLoop()
                except:
                    pass
                import sys
                sys.exit(0)
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
    global is_fullscreen, paused, pause_menu_selected

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
    # PAUSE MENU NAVIGATION
    # =====================
    if paused:
        if key == GLUT_KEY_UP or key == GLUT_KEY_DOWN:
            pause_menu_selected = 1 - pause_menu_selected  # Toggle between 0 and 1
        elif key == GLUT_KEY_RIGHT or key == GLUT_KEY_LEFT:
            pause_menu_selected = 1 - pause_menu_selected  # Also toggle with left/right
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