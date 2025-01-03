# Filter Partikel (Sparkling Effects)

## Anggota Kelompok
NAMA                     | NIM                  |ID Github
:----------------------: | :-----------------: | :---------------:
Dias Morello Sembiring   | 120140167           | Mynamedm
Rama Aldiaksa Supi       | 121140056           | ramaaldiaksa
Miftah Hasan Hadi Mohtar | 121140045           | Miftah114

## Deskripsi
Penambahan efek partikel di sekitar wajah pengguna. Efek ini akan mengikuti gerakan wajah secara real-time.

### Menggunakan library:
- **MediaPipe Face Mesh** untuk mendeteksi wajah.
- **OpenCV** untuk menghasilkan efek partikel di sekitar wajah.

---

## Fitur Utama
- Deteksi wajah secara real-time menggunakan MediaPipe Face Mesh.
- Efek partikel yang mengikuti gerakan wajah.
- Real-time visualisasi dengan menggunakan webcam.
- Tampilan hasil efek partikel di sekitar wajah pengguna.

---

## Logbook Progress

| **Minggu** | **Tanggal**   | **Progress**                                                                                                                                                               |
|------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1          | 5/12/2024    | - Inisialisasi proyek, eksplorasi MediaPipe, implementasi deteksi wajah dan landmark wajah. <br> - Pengembangan logika efek partikel untuk mengikuti wajah. |
| 2          | 10/12/2024    | - Menambahkan tampilan dengan OpenCV untuk menampilkan efek partikel di sekitar wajah. <br> - Finalisasi program dan dokumentasi awal proyek. |
| 3          | 14/12/2024    | - Mengimplementasikan efek partikel yang mengikuti gerakan wajah. <br> - Memperbaiki tampilan agar lebih user-friendly dan menarik. |
| 4          | 22/12/2024    | - Menambahkan dokumentasi dengan LaTeX untuk laporan proyek. [Link Laporan](https://www.overleaf.com/project/676944b98ced759900e75834) |
| 5          | 23/12/2024    | - Debugging dan optimasi performa, memastikan tidak ada bug dan glitch. Efek partikel berjalan dengan mulus mengikuti gerakan wajah. |

---

## Instruksi Instalasi dan Penggunaan

1. **Clone repositori ini ke komputer Anda:**
   ```bash
   git clone https://github.com/username/Tubes-Mulmed.git
   cd Tubes-Mulmed

2. Instal Dependencies yang diperlukan dari file requirements.txt :
   ```bash
   pip install -r requirements.txt

4. Jalankan proyek menggunakan:
   ```bash
   python Main_Fix.py

---

## Penutup

Proyek ini bertujuan untuk menambahkan efek visual menarik yang mengikuti wajah pengguna secara real-time. Dengan menggunakan teknologi MediaPipe untuk deteksi wajah dan OpenCV untuk efek visual, aplikasi ini memberikan pengalaman interaktif yang menyenangkan. Ke depan, fitur ini bisa diperluas dengan jenis efek partikel lainnya atau dengan menambahkan lebih banyak interaktivitas.

