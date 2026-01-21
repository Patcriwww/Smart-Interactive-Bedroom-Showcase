# Smart Interactive Bedroom Showcase

Simulasi **kamar tidur 3D interaktif** menggunakan **Python dan
PyOpenGL**. Project ini menampilkan sebuah ruangan dengan berbagai objek
furnitur yang dapat diobservasi secara bebas menggunakan kamera, lengkap
dengan fitur interaksi dan pencahayaan dinamis.

Project ini dibuat untuk memenuhi tugas mata kuliah **Komputer Grafik &
Pengolahan Citra** dengan tujuan memahami konsep dasar grafika komputer
seperti: - Pemodelan objek 3D - Transformasi - Pencahayaan - Tekstur -
Interaksi pengguna

------------------------------------------------------------------------

## Fitur Utama

### 1. Objek 3D Berbasis Primitive

Semua objek dibuat menggunakan primitive OpenGL (cube, quad, cylinder)
dan diberi tekstur agar terlihat lebih realistis.

### 2. Collision Detection

Kamera tidak dapat menembus dinding dan objek furnitur seperti: - Bed\
- Wardrobe\
- Bookshelf\
- Meja

### 3. Pergerakan Kamera Bebas

Navigasi ruangan secara bebas menggunakan keyboard.

### 4. Kamera Fokus Objek

Fitur fokus otomatis ke objek tertentu menggunakan tombol angka.

### 5. Interaksi Objek

-   Toggle wardrobe (buka/tutup)\
-   Lampu plafon dan lampu tidur\
-   Mode siang dan malam\
-   Gorden\
-   Power PC

### 6. Mode Siang & Malam

Simulasi pencahayaan siang dan malam.

### 7. Jam Digital Real-Time

Menampilkan waktu sistem secara langsung di dalam scene.

### 8. HUD (Heads-Up Display)

Menampilkan informasi kontrol dan status kamera secara semi-transparan.

------------------------------------------------------------------------

## Kontrol

### Navigasi Kamera

  Tombol       Fungsi
  ------------ ---------------------------
  W A S D      Maju, Mundur, Kiri, Kanan
  Arrow Keys   Mengubah arah pandang
  Q / E        Naik / Turun

### Interaksi

  Tombol   Fungsi
  -------- --------------------
  O        Toggle Wardrobe
  N        Mode Siang / Malam
  L        Lampu Plafon
  K        Lampu Tidur
  P        Power PC

### Fokus Kamera

  Tombol   Objek
  -------- -----------------
  1        Bed
  2        Table
  3        Window
  4        Wardrobe
  5        Door
  6        Poster
  7        Workstation
  8        Bookshelf
  9        Trash Bin
  0        Plant
  T        Air Conditioner
  C        Lampu Plafon
  J        Jam

### Keluar Aplikasi

  Tombol       Fungsi
  ------------ --------
  ESC          Pause
  Klik Mouse   Keluar

------------------------------------------------------------------------

## Tools & Framework

-   Python\
-   PyOpenGL\
-   OpenGL (Fixed Function Pipeline)\
-   GLUT\
-   Visual Studio Code

------------------------------------------------------------------------

## Cara Menjalankan

1.  Install Python\

2.  Install dependency:

    ``` bash
    pip install PyOpenGL PyOpenGL_accelerate
    ```

3.  Jalankan program:

    ``` bash
    python main.py
    ```

------------------------------------------------------------------------

## Catatan

Project ini tidak menggunakan model 3D eksternal. Seluruh objek dibuat
menggunakan primitive OpenGL untuk melatih pemahaman konsep dasar
grafika komputer.

------------------------------------------------------------------------

## Author

**Fachri Reyhan**\
Komputer Grafik & Pengolahan Citra -- Semester 5
