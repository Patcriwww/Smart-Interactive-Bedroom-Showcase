from OpenGL.GL import *
from OpenGL.GLUT import *

door_open = False
door_angle = 0.0
DOOR_MAX = 90.0
DOOR_SPEED = 2.0

def toggle_wardrobe():
    global door_open
    door_open = not door_open

def update_wardrobe():
    global door_angle
    if door_open and door_angle < DOOR_MAX:
        door_angle += DOOR_SPEED
    elif not door_open and door_angle > 0:
        door_angle -= DOOR_SPEED

def cube(w, h, d):
    """Draw textured cube - all 6 faces"""
    w /= 2; h /= 2; d /= 2
    glBegin(GL_QUADS)

    # FRONT
    glTexCoord2f(0,0); glVertex3f(-w,-h, d)
    glTexCoord2f(1,0); glVertex3f( w,-h, d)
    glTexCoord2f(1,1); glVertex3f( w, h, d)
    glTexCoord2f(0,1); glVertex3f(-w, h, d)

    # BACK
    glTexCoord2f(0,0); glVertex3f( w,-h,-d)
    glTexCoord2f(1,0); glVertex3f(-w,-h,-d)
    glTexCoord2f(1,1); glVertex3f(-w, h,-d)
    glTexCoord2f(0,1); glVertex3f( w, h,-d)

    # LEFT
    glTexCoord2f(0,0); glVertex3f(-w,-h,-d)
    glTexCoord2f(1,0); glVertex3f(-w,-h, d)
    glTexCoord2f(1,1); glVertex3f(-w, h, d)
    glTexCoord2f(0,1); glVertex3f(-w, h,-d)

    # RIGHT
    glTexCoord2f(0,0); glVertex3f( w,-h, d)
    glTexCoord2f(1,0); glVertex3f( w,-h,-d)
    glTexCoord2f(1,1); glVertex3f( w, h,-d)
    glTexCoord2f(0,1); glVertex3f( w, h, d)

    # TOP
    glTexCoord2f(0,0); glVertex3f(-w, h,-d)
    glTexCoord2f(1,0); glVertex3f( w, h,-d)
    glTexCoord2f(1,1); glVertex3f( w, h, d)
    glTexCoord2f(0,1); glVertex3f(-w, h, d)

    # BOTTOM
    glTexCoord2f(0,0); glVertex3f(-w,-h, d)
    glTexCoord2f(1,0); glVertex3f( w,-h, d)
    glTexCoord2f(1,1); glVertex3f( w,-h,-d)
    glTexCoord2f(0,1); glVertex3f(-w,-h,-d)
    
    glEnd()

def shelf_top(w, h, d):
    """Draw only top face - for shelf surfaces"""
    w /= 2; h /= 2; d /= 2
    glBegin(GL_QUADS)
    # TOP ONLY
    glVertex3f(-w, h,-d)
    glVertex3f( w, h,-d)
    glVertex3f( w, h, d)
    glVertex3f(-w, h, d)
    glEnd()

def door_face(w, h, d):
    """Draw ONLY front face - for door panels"""
    w /= 2; h /= 2; d /= 2
    # Sample a wood-grain-only sub-region to avoid the texture's door/handle prints
    u0, v0 = 0.0, 0.0
    us, vs = 0.25, 0.25
    glBegin(GL_QUADS)
    # FRONT ONLY
    glTexCoord2f(u0,     v0);     glVertex3f(-w,-h, d)
    glTexCoord2f(u0+us,  v0);     glVertex3f( w,-h, d)
    glTexCoord2f(u0+us, v0+vs);   glVertex3f( w, h, d)
    glTexCoord2f(u0,    v0+vs);   glVertex3f(-w, h, d)
    glEnd()


def door_handle(hx, hy, hz, hw, hh, hd):
    """Draw a single untextured handle block centered at (hx, hy, hz)."""
    glBegin(GL_QUADS)
    # front face only for a slim handle
    x0, x1 = hx - hw/2, hx + hw/2
    y0, y1 = hy - hh/2, hy + hh/2
    zf = hz + hd/2
    glVertex3f(x0, y0, zf)
    glVertex3f(x1, y0, zf)
    glVertex3f(x1, y1, zf)
    glVertex3f(x0, y1, zf)
    glEnd()



def cube_no_front(w, h, d):
    """Draw textured cube WITHOUT front face - prevents duplicate doors.

    Uses a small UV window to sample only wood grain (avoids handles in the wood texture).
    """
    w /= 2; h /= 2; d /= 2
    # Sample only a sub-rectangle of the texture to avoid the door/handle area
    u0, v0 = 0.0, 0.0
    us, vs = 0.25, 0.25  # small grain-only region
    glBegin(GL_QUADS)

    # BACK
    glTexCoord2f(u0,      v0);      glVertex3f( w,-h,-d)
    glTexCoord2f(u0+us,   v0);      glVertex3f(-w,-h,-d)
    glTexCoord2f(u0+us, v0+vs);     glVertex3f(-w, h,-d)
    glTexCoord2f(u0,    v0+vs);     glVertex3f( w, h,-d)

    # LEFT
    glTexCoord2f(u0,      v0);      glVertex3f(-w,-h,-d)
    glTexCoord2f(u0+us,   v0);      glVertex3f(-w,-h, d)
    glTexCoord2f(u0+us, v0+vs);     glVertex3f(-w, h, d)
    glTexCoord2f(u0,    v0+vs);     glVertex3f(-w, h,-d)

    # RIGHT
    glTexCoord2f(u0,      v0);      glVertex3f( w,-h, d)
    glTexCoord2f(u0+us,   v0);      glVertex3f( w,-h,-d)
    glTexCoord2f(u0+us, v0+vs);     glVertex3f( w, h,-d)
    glTexCoord2f(u0,    v0+vs);     glVertex3f( w, h, d)

    # TOP
    glTexCoord2f(u0,      v0);      glVertex3f(-w, h,-d)
    glTexCoord2f(u0+us,   v0);      glVertex3f( w, h,-d)
    glTexCoord2f(u0+us, v0+vs);     glVertex3f( w, h, d)
    glTexCoord2f(u0,    v0+vs);     glVertex3f(-w, h, d)

    # BOTTOM
    glTexCoord2f(u0,      v0);      glVertex3f(-w,-h, d)
    glTexCoord2f(u0+us,   v0);      glVertex3f( w,-h, d)
    glTexCoord2f(u0+us, v0+vs);     glVertex3f( w,-h,-d)
    glTexCoord2f(u0,    v0+vs);     glVertex3f(-w,-h,-d)

    glEnd()


def draw_wardrobe(wood_tex):
    global door_angle

    glPushMatrix()
    glTranslatef(3.3, 1.4, -2.2)  # pulled further off the back wall to keep it fully inside the 4x4 room; raised slightly to avoid floor clipping
    glRotatef(-90, 0, 1, 0)

    # BODY - textured with NO front face (to avoid duplicate doors)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, wood_tex)
    glColor3f(1, 1, 1)
    
    glPushMatrix()
    glScalef(3.0, 2.6, 0.8)  # reduced depth to avoid wall clipping
    cube_no_front(1, 1, 1)
    glPopMatrix()

    # DOORS - front face only
    # LEFT DOOR (full-width coverage)
    glPushMatrix()
    glTranslatef(-1.5, 0, 0.41)  # hinge at left edge, adjusted for shallower depth
    glRotatef(-door_angle, 0, 1, 0)
    glTranslatef(0.75, 0, 0)
    glScalef(1.5, 2.4, 0.05)
    door_face(1, 1, 1)
    glDisable(GL_TEXTURE_2D)
    glColor3f(0.2, 0.2, 0.2)
    # single handle centered on door
    door_handle(0.35, 0.0, 0.52, 0.05, 0.35, 0.02)
    glEnable(GL_TEXTURE_2D)
    glPopMatrix()

    # RIGHT DOOR (full-width coverage)
    glPushMatrix()
    glTranslatef(1.5, 0, 0.41)   # hinge at right edge, adjusted for shallower depth
    glRotatef(door_angle, 0, 1, 0)
    glTranslatef(-0.75, 0, 0)
    glScalef(1.5, 2.4, 0.05)
    door_face(1, 1, 1)
    glDisable(GL_TEXTURE_2D)
    glColor3f(0.2, 0.2, 0.2)
    # single handle centered on door
    door_handle(-0.35, 0.0, 0.52, 0.05, 0.35, 0.02)
    glEnable(GL_TEXTURE_2D)
    glPopMatrix()

    glDisable(GL_TEXTURE_2D)

    glPopMatrix()

def draw_wardrobe_interior():
    """Draw wardrobe shelves and interior"""
    glPushMatrix()
    glDisable(GL_TEXTURE_2D)

    # Interior back wall (bright white/cream)
    glColor3f(0.98, 0.96, 0.94)
    glPushMatrix()
    glTranslatef(0, 0, -0.45)
    glScalef(1.5, 2.5, 0.02)
    cube(1, 1, 1)
    glPopMatrix()

    # Interior side walls (light)
    glColor3f(0.95, 0.93, 0.91)
    glPushMatrix()
    glTranslatef(-0.74, 0, 0)
    glScalef(0.02, 2.5, 0.9)
    cube(1, 1, 1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.74, 0, 0)
    glScalef(0.02, 2.5, 0.9)
    cube(1, 1, 1)
    glPopMatrix()

    # Interior shelves - TOP FACE ONLY (no sides/front/back)
    glColor3f(0.85, 0.78, 0.70)
    for y in [0.7, 0.0, -0.7]:
        glPushMatrix()
        glTranslatef(0, y, 0)
        glScalef(1.48, 0.03, 0.88)
        shelf_top(1, 1, 1)
        glPopMatrix()

    # Clothes rod
    glColor3f(0.6, 0.6, 0.6)
    glPushMatrix()
    glTranslatef(0, 0.9, 0)
    glRotatef(90, 0, 1, 0)
    gluCylinder(gluNewQuadric(), 0.015, 0.015, 0.72, 12, 1)
    glPopMatrix()

    glPopMatrix()
