from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
from collision import COLLIDERS, sphere_aabb, CAMERA_RADIUS


# =====================
# ROOM BOUNDARY (HARUS SAMA DENGAN texture.py)
# =====================
ROOM_SIZE = 4.0
ROOM_HEIGHT = 3.0
WALL_MARGIN = 0.45   

# =====================
# CAMERA STATE
# =====================
pos = [0.0, 1.6, 1.5]   # posisi kamera dalam ruangan
yaw = 180.0
pitch = 0.0

vel = [0.0, 0.0, 0.0]

MOVE_SPEED = 0.15
ROT_SPEED  = 2.0
DAMPING    = 0.85

# =====================
# CAMERA FOCUS
# =====================
FOCUS_POINTS = {

    # BED
    b'1': {
        "name": "Bed",
        "cam": [-0.6, 1.6, -0.6],
        "target": [-2.2, 0.8, -2.1],
    },

    # TABLE + LAMP
    b'2': {
        "name": "Table",
        "cam": [-2.0, 1.6, -0.2],
        "target": [-3.2, 0.7, -1.1],
    },

    # WINDOW + CURTAIN
    b'3': {
        "name": "Window",
        "cam": [0.0, 1.8, -1.8],
        "target": [0.0, 2.0, -3.95],
    },

    # WARDROBE 
    b'4': {
        "name": "Wardrobe",
        "cam": [1.2, 1.7, -1.7],
        "target": [3.5, 1.4, -3.2],
    },

    # DOOR
    b'5': {
    "name": "Door",
    "cam": [1.50, 1.6, 0.6],
    "target": [3.95, 1.2, 2.0],
    },
    
    # POSTER
    b'6': {
        "name": "Poster",
        "cam": [0.0, 1.7, 2.4],
        "target": [0.0, 2.0, 3.95],
    },

    # WORKSTATION
    b'7': {
        "name": "Workstation",
        "cam": [-1.9, 1.6, 1.6],
        "target": [-3.3, 0.9, 1.2],
    },

    # BOOKSHELF 
    b'8': {
        "name": "Bookshelf",
        "cam": [1.4, 2.0, 0.7],
        "target": [3.75, 2.0, 0.55],
    },

    # TRASH BIN 
    b'9': {
        "name": "Trash Bin",
        "cam": [2.0, 1.3, 0.8],
        "target": [3.75, 0.3, 1.55],
    },

    # PLANT
    b'0': {
        "name": "Plant",
        "cam": [-2.8, 1.5, 3.0],
        "target": [-3.6, 0.6, 3.6],
    },

    # CEILING LAMP 
    b'c': {
        "name": "Ceiling Lamp",
        "cam": [0.0, 1.8, 0.0],
        "target": [0.0, 2.9, 0.0],
    },
    
    # RUG 
    b'r': {   
        "name": "Rug",
        "cam": [0.0, 1.4, 2.2],     
        "target": [0.0, 0.01, 0.0]   
    },

    # DIGITAL CLOCK
    b'j': {
        "name": "Digital Clock",
        "cam": [-2.8, 2.2, 0.5],      
        "target": [-3.95, 2.5, 0.5], 
},
}


# =====================
# HELPER
# =====================
def deg2rad(d):
    return d * math.pi / 180.0

def clamp(v, vmin, vmax):
    return max(vmin, min(vmax, v))

def get_dir():
    ry = deg2rad(yaw)
    rp = deg2rad(pitch)
    return [
        math.cos(ry) * math.cos(rp),
        math.sin(rp),
        math.sin(ry) * math.cos(rp)
    ]


# =====================
# FOCUS CAMERA
# =====================
def focus_camera(cam_pos, target):
    global pos, yaw, pitch, vel

    # movement
    vel = [0.0, 0.0, 0.0]

    # set posisi kamera
    pos[0], pos[1], pos[2] = cam_pos

    dx = target[0] - pos[0]
    dy = target[1] - pos[1]
    dz = target[2] - pos[2]

    yaw = math.degrees(math.atan2(dz, dx))
    dist = math.sqrt(dx*dx + dz*dz)
    pitch = math.degrees(math.atan2(dy, dist))

    yaw -= 6.0
    pitch -= 3.0


# =====================
# COLLISION CHECK
# =====================
def apply_collision():

    pos[1] = clamp(pos[1], 0.6, ROOM_HEIGHT - 0.4)
    pos[0] = clamp(
        pos[0],
        -ROOM_SIZE + WALL_MARGIN + CAMERA_RADIUS,
         ROOM_SIZE - WALL_MARGIN - CAMERA_RADIUS
    )

    pos[2] = clamp(
        pos[2],
        -ROOM_SIZE + WALL_MARGIN + CAMERA_RADIUS,
         ROOM_SIZE - WALL_MARGIN - CAMERA_RADIUS
    )

    # =========================
    # LANTAI & PLAFON
    # =========================
    pos[1] = clamp(
        pos[1],
        0.6,
        ROOM_HEIGHT - 0.4
    )


# =====================
# APPLY CAMERA
# =====================
def apply_camera():
    global pos, vel

    # =========================
    # PREDICT NEXT POS
    # =========================
    next_x = pos[0] + vel[0]
    next_y = pos[1] + vel[1]
    next_z = pos[2] + vel[2]

    # =========================
    # WALL COLLISION FIRST
    # =========================
    min_x = -ROOM_SIZE + WALL_MARGIN + CAMERA_RADIUS
    max_x =  ROOM_SIZE - WALL_MARGIN - CAMERA_RADIUS
    min_z = -ROOM_SIZE + WALL_MARGIN + CAMERA_RADIUS
    max_z =  ROOM_SIZE - WALL_MARGIN - CAMERA_RADIUS

    if not (min_x <= next_x <= max_x):
        vel[0] = 0
        next_x = pos[0]

    if not (min_z <= next_z <= max_z):
        vel[2] = 0
        next_z = pos[2]

    # =========================
    # SLIDING COLLISION (X AXIS)
    # =========================
    blocked_x = False
    for box in COLLIDERS:
        if sphere_aabb(next_x, pos[1], pos[2], CAMERA_RADIUS, box):
            blocked_x = True
            break

    if not blocked_x:
        pos[0] = next_x
    else:
        vel[0] = 0

    # =========================
    # SLIDING COLLISION (Z AXIS)
    # =========================
    blocked_z = False
    for box in COLLIDERS:
        if sphere_aabb(pos[0], pos[1], next_z, CAMERA_RADIUS, box):
            blocked_z = True
            break

    if not blocked_z:
        pos[2] = next_z
    else:
        vel[2] = 0


    # =========================
    # Y AXIS (FLOOR / CEILING)
    # =========================
    pos[1] += vel[1]

    # =========================
    # DAMPING
    # =========================
    for i in range(3):
        vel[i] *= DAMPING

    apply_collision()

    d = get_dir()

    gluLookAt(
        pos[0], pos[1], pos[2],
        pos[0] + d[0],
        pos[1] + d[1],
        pos[2] + d[2],
        0, 1, 0
    )


# =====================
# MOVEMENT (WASD)
# =====================
def move_camera(key):
    global vel
    d = get_dir()
    right = [-d[2], 0, d[0]]

    if key == b'w':
        for i in range(3): vel[i] += d[i] * MOVE_SPEED
    elif key == b's':
        for i in range(3): vel[i] -= d[i] * MOVE_SPEED
    elif key == b'a':
        vel[0] -= right[0] * MOVE_SPEED
        vel[2] -= right[2] * MOVE_SPEED
    elif key == b'd':
        vel[0] += right[0] * MOVE_SPEED
        vel[2] += right[2] * MOVE_SPEED
    elif key == b'q':
        vel[1] += MOVE_SPEED
    elif key == b'e':
        vel[1] -= MOVE_SPEED

# =====================
# ROTATION (ARROW KEYS)
# =====================
def rotate_camera(key):
    global yaw, pitch

    if key == GLUT_KEY_LEFT:
        yaw -= ROT_SPEED
    elif key == GLUT_KEY_RIGHT:
        yaw += ROT_SPEED
    elif key == GLUT_KEY_UP:
        pitch += ROT_SPEED
    elif key == GLUT_KEY_DOWN:
        pitch -= ROT_SPEED

    pitch = clamp(pitch, -89.0, 89.0)
