🩺 Aplikasi Cek Risiko dan Rekomendasi Sistem Diabetes

Aplikasi ini bertujuan untuk membantu pengguna mengevaluasi risiko diabetes dan memberikan rekomendasi awal berbasis gejala dan aturan umum yang dimasukkan ke dalam sistem.

============================================================
📁 Struktur Proyek

RS DIABETES/
├── Aplication/
│   ├── Material/            # Gambar ikon dan antarmuka pengguna
│   │   ├── image_1.png
│   │   ├── image_2.png
│   │   └── ...
│   └── Rule/
│       ├── data_gejala_obat.csv     # Data gejala dan obat-obatan
│       └── rulesUmum.csv            # Aturan sistem rekomendasi
├── Aplikasi_Cek_Resiko_DiabetesRS.py   # File utama (Python)
└── Aplikasi_Cek_Resiko_DiabetesRS.exe  # Versi executable (Windows)

============================================================
🚀 Fitur Utama

- ✅ Evaluasi risiko diabetes berdasarkan gejala yang dipilih pengguna.
- 💡 Sistem rekomendasi berbasis aturan (rule-based) untuk penanganan awal.
- 📊 Interface visual dengan dukungan gambar dan tombol interaktif.
- 🖥️ Bisa dijalankan langsung tanpa Python (via `.exe`).

============================================================
🧪 Cara Menjalankan Aplikasi

🔹 Jika Menggunakan Python:
1. Pastikan Python 3.x telah terinstal.
2. Jalankan perintah:
   python Aplikasi_Cek_Resiko_DiabetesRS.py

🔹 Jika Menggunakan Windows:
1. Jalankan langsung file:
   Aplikasi_Cek_Resiko_DiabetesRS.exe

============================================================
📦 Kebutuhan (Opsional, jika pakai .py)

Jika kamu menjalankan dari file .py, pastikan kamu punya:
- Python 3.x
- Pustaka GUI seperti `tkinter`, `pandas`, dan `csv`

Install dengan:
pip install pandas

============================================================
👨‍⚕️ Dataset & Rules

- data_gejala_obat.csv – Menyimpan daftar gejala dan obat terkait.
- rulesUmum.csv – Aturan umum untuk sistem inferensi atau rekomendasi berbasis gejala.

============================================================
