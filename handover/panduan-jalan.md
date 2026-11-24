# Panduan Menjalankan Aplikasi

Untuk responden usability testing dan siapa pun yang perlu mencoba aplikasi.
Aplikasi berbasis **Command Line Interface**, jadi dijalankan lewat terminal, bukan diklik.

---

## 1. Prasyarat

- Windows / Linux / macOS
- Python 3.10 atau lebih baru
- Koneksi internet **hanya** untuk instalasi library (sekali saja)

---

## 2. Tiga Langkah Menjalankan

Buka terminal (PowerShell di Windows) **di folder project**, lalu:

**Langkah 1 — install library (sekali saja)**
```
py -m pip install pandas openpyxl
```

**Langkah 2 — jalankan aplikasi**
```
py main.py
```

**Langkah 3 — ikuti menu**
Ketik angka pilihan lalu tekan ENTER. Contoh menampilkan akan seperti ini:
```
==========================================================
                  Kalkulator Bangun Datar
==========================================================
[1] Kalkulator Bangun Datar
[2] Kalkulator Bangun Ruang
[3] Tentang Aplikasi
[0] Keluar
Masukan Pilihan Anda:
```

Keluar dari aplikasi: pilih `0` pada menu utama.

---

## 3. Alur Singkat untuk Responden Uji

1. Pilih `[1]` → pilih bangun, misal `[1] Persegi`.
2. Masukkan nilai saat diminta, contoh `5` → tekan ENTER.
3. Hasil keliling dan luas ditampilkan.
4. Pilih `[1] Hitung Lagi`, `[2] Pilih Bangun Lain`, atau `[0] Menu Utama`.
5. Ulangi untuk `[2] Kalkulator Bangun Ruang`.
6. Untuk menyimpan hasil: pada submenu bangun pilih nomor **Simpan Ke Excel**
   (menu datar: `[8]`, menu ruang: `[9]`).
7. File hasil tersimpan di folder `data/` dengan nama
   `hasil_perhitungan_bangun_datar.xlsx` atau `hasil_perhitungan_bangun_ruang.xlsx`.

Skenario tugas yang bisa diberikan ke responden (pilih 4–5):

| No | Tugas | Jawaban benar |
|---|---|---|
| 1 | Hitung keliling dan luas persegi dengan sisi 5 | K = 20, L = 25 |
| 2 | Hitung luas permukaan dan volume tabung r = 7, t = 10 | LP = 747,70 ; V = 1539,38 |
| 3 | Coba masukkan huruf `abc` sebagai panjang sisi | Muncul pesan "Input harus berupa angka." |
| 4 | Hitung segitiga dengan sisi 1, 2, dan 10 | Muncul pesan segitiga tidak dapat dibentuk |
| 5 | Simpan hasil perhitungan ke Excel, lalu buka filenya | File muncul di folder `data/` |
| 6 | Kembali ke menu utama lalu keluar aplikasi | Aplikasi berhenti normal |

Catat untuk tiap responden: berhasil / tidak, dan berapa lama (opsional).

---

## 4. Masalah Umum dan Solusinya

| Gejala | Penyebab | Solusi |
|---|---|---|
| `py` tidak dikenali | Python belum terpasang / belum masuk PATH | Install Python dari python.org, centang "Add Python to PATH", lalu buka terminal baru |
| `ModuleNotFoundError: No module named 'pandas'` | Library belum diinstall | Jalankan `py -m pip install pandas openpyxl` |
| `ModuleNotFoundError: No module named 'menu'` | Terminal tidak berada di folder project | `cd` ke folder project (yang berisi `main.py`), baru jalankan `py main.py` |
| `PermissionError` saat simpan Excel | File `.xlsx` sedang dibuka di Excel | Tutup filenya, lalu simpan ulang |
| Huruf aneh / simbol rusak di terminal | Encoding terminal | Pakai Windows Terminal atau PowerShell terbaru; atau jalankan `chcp 65001` |
| `pip` gagal karena izin | Butuh hak tulis | Coba `py -m pip install --user pandas openpyxl` |
| Aplikasi langsung tertutup setelah selesai | Jendela dobel-klik | Jalankan dari terminal, jangan dengan klik dua kali `main.py` |

---

## 5. Catatan Penguji

- Riwayat perhitungan **hanya tersimpan di sesi berjalan**. Kalau responden kembali ke
  menu utama sebelum menekan Simpan, datanya hilang. Beri tahu responden bila tugasnya
  menyimpan ke Excel.
- Menu "Bersihkan Excel" hanya mengosongkan riwayat di memori; file `.xlsx` yang sudah ada
  **tidak** terhapus. Jangan menulis sebaliknya di laporan.
- Jika menyimpan saat riwayat kosong, tidak ada pesan yang muncul — ini perilaku saat ini.
- Folder `data/` sudah ada di project. Jika belum ada, buat folder `data` di dalam folder
  project sebelum menyimpan.
