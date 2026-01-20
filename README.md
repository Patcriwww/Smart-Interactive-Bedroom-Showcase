# Smart Interactive Bedroom Showcase

Project ini merupakan simulasi **ruangan kamar tidur 3D interaktif** yang dibuat menggunakan **Python dan PyOpenGL**. Aplikasi ini menampilkan sebuah kamar dengan beberapa objek furnitur yang dapat dilihat secara bebas menggunakan kamera, serta dilengkapi dengan fitur interaksi sederhana.

Project ini dibuat untuk memenuhi tugas mata kuliah **Komputer Grafik & Pengolahan Citra**, dengan tujuan memahami konsep dasar grafika komputer seperti pemodelan objek 3D, transformasi, pencahayaan, tekstur, dan interaksi pengguna.

---

## Fitur

- **Objek 3D berbasis primitives**  
  Semua objek dalam ruangan dibuat menggunakan primitive OpenGL seperti cube, quad, dan cylinder, kemudian diberi tekstur agar terlihat lebih realistis.

- **Collision detection**  
  Kamera tidak dapat menembus dinding ruangan maupun objek furnitur seperti bed, wardrobe, dan bookshelf.

- **Pergerakan kamera bebas**  
  Pengguna dapat bergerak di dalam ruangan menggunakan keyboard untuk melihat objek dari berbagai sudut.

- **Camera focus ke objek**  
  Tersedia fitur fokus kamera ke objek tertentu seperti bed, table, door, dan lainnya menggunakan tombol angka.

- **Toggle interaksi objek**
  - Membuka / menutup wardrobe  
  - Menyalakan / mematikan lampu  
  - Mengubah mode siang dan malam  
  - Mengaktifkan / menonaktifkan gorden

- **Mode siang dan malam**  
  Pencahayaan ruangan dapat diubah untuk mensimulasikan kondisi siang dan malam.

- **Jam digital real-time**  
  Terdapat jam digital yang menampilkan waktu sistem secara real-time di dalam scene.

- **HUD (Heads-Up Display)**  
  Informasi kontrol dan kamera ditampilkan dalam bentuk HUD semi-transparan.

---

## Kontrol

### Pergerakan Kamera
- `W A S D` : Bergerak maju, mundur, kiri, kanan  
- `Arrow Keys` : Mengubah arah pandang kamera  
- `Q / E` : Naik / turun  

### Interaksi
- `O` : Toggle wardrobe  
- `N` : Mode siang / malam  
- `L` : Lampu Plafon
- `K` : Lampu Tidur  
   

### Focus Kamera
- `1` : Bed  
- `2` : Table  
- `3` : Window  
- `4` : Wardrobe  
- `5` : Door  
- `6` : Poster/Poster2/Poster3/Poster4  
- `7` : Workstation  
- `8` : Bookshelf  
- `9` : Trash Bin  
- `0` : Plant
- `T` : Air Conditioner
- `C` : Lampu Plafon
- `J` : Jam

### Keluar
- `ESC` : Paused
- `Q` : Keluar dari aplikasi    

---

## Tools & Framework

- **Python**  
- **PyOpenGL**  
- **OpenGL (Fixed Function Pipeline)**  
- **GLUT**  
- **Visual Studio Code**

---


**Cara Menjalankan Program**

1. Install Python

2. Install library yang dibutuhkan:

"pip install PyOpenGL PyOpenGL_accelerate"

3. Jalankan program:

"python main.py"


**Catatan**

Project ini tidak menggunakan model 3D eksternal. Seluruh objek dibuat langsung menggunakan primitive OpenGL untuk melatih pemahaman konsep dasar grafika komputer.


**Author**
Fachri Reyhan
Komputer Grafik & Pengolahan Citra – Semester 5


