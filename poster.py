def draw_poster_2():
    glPushMatrix()

    # === POSISI: PERSIS DI SAMPING POSTER 1 ===
    glTranslatef(1.25, 1.4, 3.98)   # X digeser kanan
    glRotatef(180, 0, 1, 0)

    w = 1.2
    h = 1.4
    z = 0.02

    glColor3f(0.8, 0.6, 0.4)  # warna sementara (tanpa texture)

    glBegin(GL_QUADS)
    glNormal3f(0, 0, 1)
    glVertex3f(-w/2, 0,  z)
    glVertex3f( w/2, 0,  z)
    glVertex3f( w/2, h,  z)
    glVertex3f(-w/2, h,  z)
    glEnd()

    glPopMatrix()
