from OpenGL.GL import *

is_day = True
lamp_on = False


def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_LIGHT0)

    if is_day:
        ambient = [0.55, 0.55, 0.55, 1.0]
        diffuse = [0.75, 0.75, 0.75, 1.0]
        specular = [0.25, 0.25, 0.25, 1.0]
    else:
        ambient = [0.12, 0.12, 0.15, 1.0]
        diffuse = [0.25, 0.25, 0.3, 1.0]
        specular = [0.08, 0.08, 0.1, 1.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular)
    glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 5.0, 4.0, 1.0])

    if lamp_on:
        glEnable(GL_LIGHT1)
        glLightfv(GL_LIGHT1, GL_POSITION, [0.0, 3.2, -2.0, 1.0])
        glLightfv(GL_LIGHT1, GL_AMBIENT, [0.15, 0.15, 0.12, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.6, 0.6, 0.6, 1.0])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [0.0, 0.0, 0.0, 1.0])
        glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, [0.0, -1.0, 0.0])
        glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 75.0)
    else:
        glDisable(GL_LIGHT1)


    # =========================
    # LIGHT 2 = CAHAYA MATAHARI DARI JENDELA (SIANG)
    # =========================
    if is_day:
        glEnable(GL_LIGHT2)

        # arah dari luar window ke dalam ruangan
        glLightfv(GL_LIGHT2, GL_POSITION, [0.0, 1.5, -1.0, 0.0])  # directional
        glLightfv(GL_LIGHT2, GL_AMBIENT,  [0.2, 0.2, 0.15, 1.0])
        glLightfv(GL_LIGHT2, GL_DIFFUSE,  [0.9, 0.85, 0.7, 1.0])
        glLightfv(GL_LIGHT2, GL_SPECULAR, [0.6, 0.6, 0.5, 1.0])
    else:
        glDisable(GL_LIGHT2)


# =========================
# TOGGLE SIANG / MALAM
# =========================
def toggle_day_night():
    global is_day
    is_day = not is_day


# =========================
# TOGGLE LAMPU PLAFON
# =========================
def toggle_lamp():
    global lamp_on
    lamp_on = not lamp_on
