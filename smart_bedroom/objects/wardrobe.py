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
    w /= 2; h /= 2; d /= 2
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-w, -h, d)
    glTexCoord2f(1, 0); glVertex3f(w, -h, d)
    glTexCoord2f(1, 1); glVertex3f(w, h, d)
    glTexCoord2f(0, 1); glVertex3f(-w, h, d)
    glTexCoord2f(0, 0); glVertex3f(w, -h, -d)
    glTexCoord2f(1, 0); glVertex3f(-w, -h, -d)
    glTexCoord2f(1, 1); glVertex3f(-w, h, -d)
    glTexCoord2f(0, 1); glVertex3f(w, h, -d)
    glTexCoord2f(0, 0); glVertex3f(-w, -h, -d)
    glTexCoord2f(1, 0); glVertex3f(-w, -h, d)
    glTexCoord2f(1, 1); glVertex3f(-w, h, d)
    glTexCoord2f(0, 1); glVertex3f(-w, h, -d)
    glTexCoord2f(0, 0); glVertex3f(w, -h, d)
    glTexCoord2f(1, 0); glVertex3f(w, -h, -d)
    glTexCoord2f(1, 1); glVertex3f(w, h, -d)
    glTexCoord2f(0, 1); glVertex3f(w, h, d)
    glEnd()

def draw_wardrobe(wood_tex):
    global door_angle
    glPushMatrix()
    glTranslatef(3.5, 1.3, -3.2)
    glRotatef(-90, 0, 1, 0)

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, wood_tex)

    glPushMatrix()
    glScalef(3.2, 2.6, 1.0)
    cube(1, 1, 1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.6, 0, 0.51)
    glRotatef(-door_angle, 0, 1, 0)
    glTranslatef(0.3, 0, 0)
    glScalef(0.6, 2.4, 0.05)
    cube(1, 1, 1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.6, 0, 0.51)
    glRotatef(door_angle, 0, 1, 0)
    glTranslatef(-0.3, 0, 0)
    glScalef(0.6, 2.4, 0.05)
    cube(1, 1, 1)
    glPopMatrix()

    glDisable(GL_TEXTURE_2D)
    glPopMatrix()

def draw_wardrobe_interior():
    glPushMatrix()
    glColor3f(0.85, 0.85, 0.85)

    glPushMatrix()
    glTranslatef(0, 0, -0.45)
    glScalef(1.15, 2.4, 0.05)
    cube(1, 1, 1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.55, 0, 0)
    glScalef(0.05, 2.4, 0.9)
    cube(1, 1, 1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.55, 0, 0)
    glScalef(0.05, 2.4, 0.9)
    cube(1, 1, 1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.8, 0)
    glScalef(1.1, 0.05, 0.85)
    cube(1, 1, 1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glScalef(1.1, 0.05, 0.85)
    cube(1, 1, 1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, -1.1, 0)
    glScalef(1.1, 0.05, 0.85)
    cube(1, 1, 1)
    glPopMatrix()

    glPopMatrix()
