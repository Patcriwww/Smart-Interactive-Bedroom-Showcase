from OpenGL.GL import *
from OpenGL.GLUT import *
import time

from ..render import texture

# PC States
PC_OFF = 0
PC_BOOTING = 1
PC_ON = 2
PC_SHUTTING_DOWN = 3

# Global PC state
pc_state = PC_OFF
pc_state_start_time = 0.0

BOOT_TIME = 3.0  # seconds
SHUTDOWN_TIME = 2.0  # seconds


def toggle_pc():
    """Toggle PC power - only works when not in transition state"""
    global pc_state, pc_state_start_time
    
    if pc_state == PC_OFF:
        pc_state = PC_BOOTING
        pc_state_start_time = time.time()
    elif pc_state == PC_ON:
        pc_state = PC_SHUTTING_DOWN
        pc_state_start_time = time.time()
    # Ignore if in BOOTING or SHUTTING_DOWN state


def update_pc_state():
    """Update PC state based on elapsed time"""
    global pc_state
    
    current_time = time.time()
    elapsed = current_time - pc_state_start_time
    
    if pc_state == PC_BOOTING and elapsed >= BOOT_TIME:
        pc_state = PC_ON
    elif pc_state == PC_SHUTTING_DOWN and elapsed >= SHUTDOWN_TIME:
        pc_state = PC_OFF


def draw_workstation():
    update_pc_state()
    
    glPushMatrix()
    glTranslatef(-3.3, 0.0, 1.2)
    glRotatef(90, 0, 1, 0)

    glColor3f(0.42, 0.28, 0.15)
    glPushMatrix()
    glTranslatef(0.0, 0.75, 0.0)
    glScalef(1.2, 0.08, 0.6)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(0.30, 0.20, 0.12)
    for x in [-0.5, 0.5]:
        for z in [-0.25, 0.25]:
            glPushMatrix()
            glTranslatef(x, 0.38, z)
            glScalef(0.08, 0.75, 0.08)
            glutSolidCube(1)
            glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, 1.10, -0.18)

    glColor3f(0.2, 0.2, 0.2)
    glPushMatrix()
    glTranslatef(0.0, -0.14, 0.0)
    glScalef(0.08, 0.24, 0.03)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, -0.28, 0.05)
    glScalef(0.25, 0.03, 0.18)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(0.05, 0.05, 0.05)
    glPushMatrix()
    glScalef(0.55, 0.35, 0.04)
    glutSolidCube(1)
    glPopMatrix()

    # Monitor screen - display based on PC state
    glDisable(GL_LIGHTING)
    
    if pc_state == PC_OFF:
        # Black screen when off
        glColor3f(0.0, 0.0, 0.0)
        glPushMatrix()
        glTranslatef(0.0, 0.0, 0.03)
        glScalef(0.48, 0.28, 0.01)
        glutSolidCube(1)
        glPopMatrix()
    else:
        # Show appropriate texture
        glEnable(GL_TEXTURE_2D)
        
        if pc_state == PC_BOOTING and texture.pc_boot_tex is not None:
            glBindTexture(GL_TEXTURE_2D, texture.pc_boot_tex)
        elif pc_state == PC_ON and texture.pc_home_tex is not None:
            glBindTexture(GL_TEXTURE_2D, texture.pc_home_tex)
        elif pc_state == PC_SHUTTING_DOWN and texture.pc_shutdown_tex is not None:
            glBindTexture(GL_TEXTURE_2D, texture.pc_shutdown_tex)
        
        glColor3f(1.0, 1.0, 1.0)
        glPushMatrix()
        glTranslatef(0.0, 0.0, 0.03)
        
        w = 0.48
        h = 0.28
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(-w/2, -h/2, 0)
        glTexCoord2f(1, 0); glVertex3f(w/2, -h/2, 0)
        glTexCoord2f(1, 1); glVertex3f(w/2, h/2, 0)
        glTexCoord2f(0, 1); glVertex3f(-w/2, h/2, 0)
        glEnd()
        
        glPopMatrix()
        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)
    
    glEnable(GL_LIGHTING)

    glPopMatrix()

    glColor3f(0.10, 0.10, 0.10)
    glPushMatrix()
    glTranslatef(0.0, 0.82, 0.05)
    glScalef(0.45, 0.03, 0.18)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(0.08, 0.08, 0.08)
    glPushMatrix()
    glTranslatef(0.30, 0.83, 0.05)
    glScalef(0.08, 0.03, 0.12)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(0.12, 0.12, 0.12)
    glPushMatrix()
    glTranslatef(0.75, 0.25, 0.0)
    glScalef(0.28, 0.9, 0.45)
    glutSolidCube(1)
    glPopMatrix()

    # Power LED indicator on PC case
    glDisable(GL_LIGHTING)
    glPushMatrix()
    glTranslatef(0.75, 0.6, 0.23)
    
    # LED color based on state
    if pc_state == PC_OFF:
        glColor3f(0.8, 0.0, 0.0)  # Red
    elif pc_state == PC_BOOTING or pc_state == PC_SHUTTING_DOWN:
        glColor3f(0.9, 0.9, 0.0)  # Yellow
    else:  # PC_ON
        glColor3f(0.0, 0.8, 0.0)  # Green
    
    glutSolidSphere(0.02, 10, 10)
    glPopMatrix()
    glEnable(GL_LIGHTING)

    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.55)

    glColor3f(0.18, 0.18, 0.18)
    glPushMatrix()
    glTranslatef(0.0, 0.45, 0.0)
    glScalef(0.5, 0.08, 0.5)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, 0.75, 0.22)
    glScalef(0.5, 0.6, 0.08)
    glutSolidCube(1)
    glPopMatrix()

    for x in [-0.18, 0.18]:
        for z in [-0.18, 0.18]:
            glPushMatrix()
            glTranslatef(x, 0.22, z)
            glScalef(0.06, 0.45, 0.06)
            glutSolidCube(1)
            glPopMatrix()

    glPopMatrix()
    glPopMatrix()
