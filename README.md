
# 🩺 Aplikasi Cek Risiko dan Rekomendasi Sistem Diabetes

Aplikasi ini membantu pengguna mengevaluasi risiko diabetes dan memberikan rekomendasi awal berbasis gejala dan aturan yang telah ditentukan. Dibuat untuk keperluan edukasi dan skripsi.

## 📁 Struktur Folder

```
RS DIABETES/
├── Aplication/
│   ├── Material/                # Gambar antarmuka
│   └── Rule/                    # Dataset dan aturan
├── Aplikasi_Cek_Resiko_DiabetesRS.py   # Script utama (Python)
└── Aplikasi_Cek_Resiko_DiabetesRS.exe  # File executable (Windows)
```

## 🚀 Fitur

- ✅ Evaluasi risiko diabetes berdasarkan gejala pengguna
- 💡 Rekomendasi tindakan awal menggunakan rule-based system
- 🖼️ Antarmuka visual dengan tombol & ikon interaktif
- 🖥️ Bisa dijalankan langsung di Windows (.exe) atau via Python

## 🧪 Cara Menjalankan

### 📌 Versi Python
1. Pastikan Python 3.x terinstal
2. Jalankan:
   ```bash
   python Aplikasi_Cek_Resiko_DiabetesRS.py
   ```

### 📌 Versi Windows
- Jalankan langsung:
  ```
  Aplikasi_Cek_Resiko_DiabetesRS.exe
  ```

## 📦 Kebutuhan (Jika menjalankan versi .py)

Install `pandas` jika belum tersedia:
```bash
pip install pandas
```

Pastikan `tkinter` sudah tersedia (biasanya sudah include di Python).

## 📊 Dataset & Aturan

- `data_gejala_obat.csv` — Data gejala dan informasi obat
- `rulesUmum.csv` — Aturan penilaian risiko & rekomendasi

## 📄 Lisensi

Proyek ini dikembangkan untuk keperluan proyek akhir dan edukasi.
Silakan digunakan dengan mencantumkan kredit yang sesuai.

## 🤝 Kontribusi

Terbuka untuk saran dan pengembangan lebih lanjut, termasuk:
- Integrasi machine learning
- Pengembangan mobile apps
- Penyempurnaan tampilan GUI

---
