# Filter Partikel (Sparkling Effects)

## Anggota Kelompok
NAMA                     | NIM                  |ID Github
:----------------------: | :-----------------: | :---------------:
Dias Morello Sembiring   | 120140167           | Mynamedm
Rama Aldiaksa Supi       | 121140056           | ramaaldiaksa
Miftah Hasan Hadi Mohtar | 121140045           | Miftah114

## Deskripsi
Penambahan efek partikel (seperti bintang atau gelembung) di sekitar wajah pengguna. Efek ini akan mengikuti gerakan wajah secara real-time.

### Menggunakan library:
- **MediaPipe Face Mesh** untuk mendeteksi wajah.
- **OpenCV** untuk menghasilkan efek partikel di sekitar wajah.

---

## Fitur Utama
- Deteksi wajah secara real-time menggunakan MediaPipe Face Mesh.
- Efek partikel (seperti bintang atau gelembung) yang mengikuti gerakan wajah.
- Real-time visualisasi dengan menggunakan webcam.
- Tampilan hasil efek partikel yang dinamis di sekitar wajah pengguna.

---

## Logbook Progress

| **Minggu** | **Tanggal**   | **Progress**                                                                                                                                                               |
|------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1          | 5/12/2024    | - Inisialisasi proyek, eksplorasi MediaPipe, studi dokumentasi API Face Mesh, implementasi deteksi wajah dan landmark wajah. <br> - Pengembangan logika efek partikel untuk mengikuti wajah. |
| 2          | 10/12/2024    | - Menambahkan UI dengan OpenCV untuk menampilkan efek partikel di sekitar wajah. <br> - Finalisasi program dan dokumentasi awal proyek. |
| 3          | 11/12/2024    | - Mengimplementasikan efek partikel dinamis dengan mengikuti gerakan wajah. <br> - Memperbaiki tampilan agar lebih user-friendly dan menarik. |
| 4          | 22/12/2024    | - Menambahkan dokumentasi dengan LaTeX untuk laporan proyek. [Link Laporan](#) |
| 5          | 22/12/2024    | - Debugging dan optimasi performa, memastikan tidak ada bug dan glitch. Efek partikel berjalan dengan mulus mengikuti gerakan wajah. |

---

## Instruksi Instalasi dan Penggunaan

1. **Persyaratan:**
   - Python 3.x
   - Install dependensi dengan pip:
     ```bash
     pip install mediapipe opencv-python numpy
     ```

2. **Penggunaan:**
   - Jalankan skrip Python:
     ```bash
     python sparkling_effects.py
     ```
   - Arahkan wajah Anda ke kamera untuk melihat efek partikel (seperti bintang atau gelembung) yang mengikuti gerakan wajah Anda.

---

## Penutup

Proyek ini bertujuan untuk menambahkan efek visual menarik yang mengikuti wajah pengguna secara real-time. Dengan menggunakan teknologi MediaPipe untuk deteksi wajah dan OpenCV untuk efek visual, aplikasi ini memberikan pengalaman interaktif yang menyenangkan. Ke depan, fitur ini bisa diperluas dengan jenis efek partikel lainnya atau dengan menambahkan lebih banyak interaktivitas.

