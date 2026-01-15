from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_bookshelf():
    glPushMatrix()
    glTranslatef(3.75, 2.1, 0.55)
    glRotatef(90, 0, 1, 0)

    shelf_width = 1.6
    shelf_depth = 0.25
    shelf_thick = 0.05

    glColor3f(0.28, 0.18, 0.10)
    for y in [0.0, -0.45, -0.9]:
        glPushMatrix()
        glTranslatef(0.0, y, 0.0)
        glScalef(shelf_width, shelf_thick, shelf_depth)
        glutSolidCube(1)
        glPopMatrix()

    glColor3f(0.35, 0.23, 0.14)
    for x in [-shelf_width / 2 + 0.03, shelf_width / 2 - 0.03]:
        glPushMatrix()
        glTranslatef(x, -0.45, 0.0)
        glScalef(0.05, 1.0, shelf_depth)
        glutSolidCube(1)
        glPopMatrix()

    book_colors = [
        (0.35, 0.22, 0.18),
        (0.22, 0.30, 0.40),
        (0.25, 0.35, 0.28),
        (0.40, 0.32, 0.18),
        (0.30, 0.22, 0.35),
        (0.38, 0.28, 0.22),
    ]

    def draw_books_row(y_level):
        x_start = -0.65
        for i in range(10):
            glColor3f(*book_colors[i % len(book_colors)])
            glPushMatrix()
            glTranslatef(x_start + i * 0.14, y_level + 0.18, 0.0)
            glScalef(0.1, 0.32, 0.18)
            glutSolidCube(1)
            glPopMatrix()

    draw_books_row(0.0)
    draw_books_row(-0.45)
    draw_books_row(-0.9)

    glPopMatrix()
