from OpenGL.GL import *

# =========================
# STATE GLOBAL
# =========================
is_day = True

# status lampu (TIDAK tergantung siang / malam)
main_lamp_on = False
bed_lamp_on  = False


# =========================
# SETUP LIGHTING (DIPANGGIL TIAP FRAME)
# =========================
def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    # ==================================================
    # LIGHT 0 — AMBIENT GLOBAL (LINGKUNGAN)
    # ==================================================
    glEnable(GL_LIGHT0)

    if is_day:
        ambient = [0.25, 0.25, 0.25, 1.0]   # siang
    else:
        ambient = [0.02, 0.02, 0.03, 1.0]   # malam (sangat gelap)

    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  [0.0, 0.0, 0.0, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [0.0, 0.0, 0.0, 1.0])

    # ==================================================
    # LIGHT 2 — CAHAYA LUAR (MATAHARI / BULAN)
    # AKTIF: JIKA LAMPU UTAMA MATI
    # ==================================================
    if not main_lamp_on:
        glEnable(GL_LIGHT2)

        glLightfv(GL_LIGHT2, GL_POSITION, [0.0, 2.2, -4.2, 1.0])
        glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, [0.0, -0.6, 1.0])
        glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 50.0)

        if is_day:
            # ☀️ CAHAYA MATAHARI
            glLightfv(GL_LIGHT2, GL_DIFFUSE,  [0.9, 0.9, 0.8, 1.0])
            glLightfv(GL_LIGHT2, GL_AMBIENT,  [0.25, 0.25, 0.22, 1.0])
            glLightfv(GL_LIGHT2, GL_SPECULAR, [0.1, 0.1, 0.1, 1.0])
        else:
            # 🌙 CAHAYA BULAN (SANGAT REDUP)
            glLightfv(GL_LIGHT2, GL_DIFFUSE,  [0.12, 0.14, 0.18, 1.0])
            glLightfv(GL_LIGHT2, GL_AMBIENT,  [0.02, 0.02, 0.03, 1.0])
            glLightfv(GL_LIGHT2, GL_SPECULAR, [0.01, 0.01, 0.015, 1.0])

    else:
        glDisable(GL_LIGHT2)

    # ==================================================
    # LIGHT 1 — LAMPU UTAMA PLAFON
    # AKTIF: JIKA main_lamp_on
    # ==================================================
    if main_lamp_on:
        glEnable(GL_LIGHT1)

        glLightfv(GL_LIGHT1, GL_POSITION, [0.0, 3.2, 0.0, 1.0])
        glLightfv(GL_LIGHT1, GL_DIFFUSE,  [1.0, 0.95, 0.85, 1.0])
        glLightfv(GL_LIGHT1, GL_AMBIENT,  [0.3, 0.28, 0.25, 1.0])
        glLightfv(GL_LIGHT1, GL_SPECULAR, [0.2, 0.2, 0.2, 1.0])

        glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, [0.0, -1.0, 0.0])
        glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 80.0)
    else:
        glDisable(GL_LIGHT1)

    # ==================================================
    # LIGHT 3 — LAMPU TIDUR (KUNING HANGAT)
    # AKTIF: JIKA bed_lamp_on
    # ==================================================
    if bed_lamp_on:
        glEnable(GL_LIGHT3)

        glLightfv(GL_LIGHT3, GL_POSITION, [-3.2, 0.9, -1.1, 1.0])
        glLightfv(GL_LIGHT3, GL_DIFFUSE,  [1.0, 0.75, 0.45, 1.0])
        glLightfv(GL_LIGHT3, GL_AMBIENT,  [0.3, 0.22, 0.15, 1.0])
        glLightfv(GL_LIGHT3, GL_SPECULAR, [0.1, 0.1, 0.1, 1.0])

        glLightfv(GL_LIGHT3, GL_SPOT_DIRECTION, [0.0, -1.0, 0.0])
        glLightf(GL_LIGHT3, GL_SPOT_CUTOFF, 55.0)
    else:
        glDisable(GL_LIGHT3)


# =========================
# TOGGLE FUNCTIONS
# =========================
def toggle_day_night():
    global is_day
    is_day = not is_day


def toggle_main_lamp():
    global main_lamp_on
    main_lamp_on = not main_lamp_on


def toggle_bed_lamp():
    global bed_lamp_on
    bed_lamp_on = not bed_lamp_on
