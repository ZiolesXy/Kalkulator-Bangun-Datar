# Tabel Pengujian (Test Case) — Bahan untuk BAB IV

Dipakai untuk bagian **4.1.2 (Code Generation)** dan **4.2 (Usability Testing)**.

## Status: SUDAH DIUJI

- **Tanggal pengujian:** 24 November 2026
- **Lingkungan:** Windows (win32), Python 3.14.0, pandas 3.1.0, openpyxl 3.1.5
- **Cara uji:** aplikasi dijalankan melalui alur menu sesungguhnya (`py main.py` →
  `menu.menu.main_menu`) dengan input terskrip otomatis menggunakan
  `handover/uji_otomatis.py`. Pengujian dilakukan pada salinan project agar file
  `data/*.xlsx` milik pengguna tidak tertimpa.
- **Hasil total:** 33 dari 33 skenario sesuai harapan (100%).

Nilai pada kolom hasil ditulis **persis seperti yang tampil di aplikasi**, yaitu
menggunakan titik desimal (contoh `20.00`), karena keluaran diformat dengan `:.2f`
pada Python. Di naskah laporan boleh diubah ke koma sesuai kaidah bahasa Indonesia,
asalkan konsisten.

---

## A. Pengujian Perhitungan (15 bangun)

| No | Bangun | Input | Output Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| A1 | Persegi | sisi = 5 | K = 20 ; L = 25 | `Keliling: 20.00 cm` ; `Luas: 25.00 cm2` | Lulus |
| A2 | Persegi Panjang | p = 10, l = 4 | K = 28 ; L = 40 | `28.00` ; `40.00` | Lulus |
| A3 | Segitiga | a = 6, b = 8, c = 10, t = 4 | K = 24 ; L = 12 | `24.00` ; `12.00` | Lulus |
| A4 | Lingkaran | r = 7 | K = 43,98 ; L = 153,94 | `43.98` ; `153.94` | Lulus |
| A5 | Jajar Genjang | a = 8, b = 5, t = 4 | K = 26 ; L = 32 | `26.00` ; `32.00` | Lulus |
| A6 | Trapesium | a = 6, b = 10, c = 5, d = 5, t = 4 | K = 26 ; L = 32 | `26.00` ; `32.00` | Lulus |
| A7 | Belah Ketupat | d₁ = 6, d₂ = 8, s = 5 | K = 20 ; L = 24 | `20.00` ; `24.00` | Lulus |
| A8 | Kubus | s = 3 | LP = 54 ; V = 27 | `54.00` ; `27.00` | Lulus |
| A9 | Balok | p = 4, l = 3, t = 2 | LP = 52 ; V = 24 | `52.00` ; `24.00` | Lulus |
| A10 | Tabung | r = 7, t = 10 | LP = 747,70 ; V = 1.539,38 | `747.70` ; `1539.38` | Lulus |
| A11 | Kerucut | r = 3, t = 4 | LP = 75,40 ; V = 37,70 | `75.40` ; `37.70` | Lulus |
| A12 | Bola | r = 7 | LP = 615,75 ; V = 1.436,76 | `615.75` ; `1436.76` | Lulus |
| A13 | Prisma Segitiga | a = 3, tₛ = 4, b = 4, c = 5, T = 10 | LP = 132 ; V = 60 | `132.00` ; `60.00` | Lulus |
| A14 | Limas Segitiga | s = 6, t = 4 | LP = 54,82 ; V = 20,78 | `54.82` ; `20.78` | Lulus |
| A15 | Limas Segiempat | s = 6, t = 4 | LP = 96 ; V = 48 | `96.00` ; `48.00` | Lulus |

---

## B. Pengujian Validasi Input

Cara uji: jalankan `py main.py`, masuk menu yang sesuai, lalu masukkan nilai pada tabel.

| No | Skenario | Input | Output Diharapkan (teks persis) | Hasil | Status |
|---|---|---|---|---|---|
| B1 | Input bukan angka | `abc` | `Input harus berupa angka.` lalu input diminta ulang | Muncul pesan tersebut, lalu diminta ulang, lalu nilai `5` diterima | Lulus |
| B2 | Input nol | `0` | `Nilai harus lebih besar dari 0.` lalu input diminta ulang | Muncul pesan tersebut, lalu nilai `5` diterima | Lulus |
| B3 | Input negatif | `-5` | `Nilai harus lebih besar dari 0.` lalu input diminta ulang | Muncul pesan tersebut, lalu nilai `5` diterima | Lulus |
| B4 | Input kosong (ENTER) | *(kosong)* | `Input harus berupa angka.` lalu input diminta ulang | Muncul pesan tersebut, lalu nilai `5` diterima | Lulus |
| B5 | Desimal pakai koma | `7,5` | Diterima, dibaca sebagai 7.5 | Diterima; K = `30.00`, L = `56.25` | Lulus |
| B6 | Input tak hingga | `inf` | `Input harus berupa angka.` | Muncul **`Masukkan angka yang valid.`** | Lulus, pesan berbeda |
| B7 | Pilihan menu tidak ada | `99` | `Pilihan tidak valid. Silakan coba lagi.` | Muncul pesan tersebut, lalu menu tampil ulang | Lulus |
| B8 | Segitiga mustahil | 1, 2, 10 | `Perhitungan Gagal: Ketiga sisi tidak dapat membentuk segitiga` | Pesan persis sama, lalu menu aksi tampil | Lulus |
| B9 | Prisma, alas mustahil | a=1, b=2, c=10 | `Perhitungan Gagal: Ketiga sisi alas tidak dapat membentuk segitiga` | Pesan persis sama | Lulus |
| B10 | Pilihan menu bukan angka | `x` pada menu | `Pilihan tidak valid. Silakan coba lagi.` | Muncul pesan tersebut | Lulus |

Catatan B6: dugaan pada draf awal **terbukti benar**. Input `inf` dibaca sebagai
`float('inf')` lalu ditolak oleh `math.isfinite()` di `utils/validation.py`, sehingga pesannya
"Masukkan angka yang valid." — **berbeda** dari pesan untuk input bukan angka (B1).
Perilaku ini tetap valid (input ditolak), tetapi tidak konsisten. Tulis sebagai temuan
di 4.2 dan saran penyeragaman pesan di 5.2.

---

## C. Pengujian Fitur Penyimpanan Excel

| No | Skenario | Langkah | Output Diharapkan | Hasil | Status |
|---|---|---|---|---|---|
| C1 | Simpan dengan riwayat terisi (datar) | Hitung persegi s=5 dan persegi panjang 10×4, pilih `[8]` Simpan | `Berhasil menyimpan data ke file: data/hasil_perhitungan_bangun_datar.xlsx` | Pesan persis muncul, file terbentuk | Lulus |
| C1b | Simpan dengan riwayat terisi (ruang) | Hitung kubus s=3, pilih `[9]` Simpan | `Berhasil menyimpan data ke file: data/hasil_perhitungan_bangun_ruang.xlsx` | Pesan persis muncul, file terbentuk | Lulus |
| C2 | Cek isi file datar | Buka file `.xlsx` | Kolom sesuai input + hasil, baris = jumlah perhitungan | 2 baris; kolom `Bangun Datar, Sisi, Keliling (cm), Luas (cm2), Panjang, Lebar` | Lulus |
| C2b | Cek isi file ruang | Buka file `.xlsx` | Idem | 1 baris; kolom `Bangun Ruang, Sisi, Luas Permukaan (cm2), Volume (cm3)` | Lulus |
| C3 | Simpan saat riwayat kosong | Langsung pilih Simpan tanpa menghitung | **Tidak ada pesan apa pun**, tidak ada file dibuat | Tidak ada pesan; file tidak dibuat (folder `data/` kosong) | Lulus sesuai kode, **perlu perbaikan** |
| C4 | Bersihkan riwayat | Hitung, lalu pilih `[9]` Bersihkan | `Riwayat perhitungan berhasil dibersihkan.` | Pesan persis muncul | Lulus |
| C5 | Bersihkan lalu simpan | Bersihkan, lalu pilih Simpan | Tidak ada data tersimpan (perilaku C3) | Tidak ada pesan; file tidak berubah | Lulus sesuai kode, **perlu perbaikan** |
| C6 | File lama setelah Bersihkan | Bersihkan, cek folder `data/` | **File `.xlsx` lama masih ada** | File tetap ada; ukuran dan waktu ubah tidak berubah | Lulus sesuai kode, **perlu perbaikan** |

C3, C5, dan C6 bukan kegagalan program, melainkan **keterbatasan perilaku** yang harus
dilaporkan apa adanya di 4.2 (temuan) dan 5.2 (saran). Jangan menulis di laporan bahwa
menu "Bersihkan Excel" menghapus file Excel — hasil uji membuktikan sebaliknya.

---

## D. Ringkasan untuk Laporan

| Kategori | Jumlah Kasus | Berhasil | Gagal | Persentase |
|---|---|---|---|---|
| Perhitungan (A) | 15 | 15 | 0 | 100% |
| Validasi input (B) | 10 | 10 | 0 | 100% |
| Penyimpanan Excel (C) | 8 | 8 | 0 | 100% |
| **Total** | **33** | **33** | **0** | **100%** |

Kalimat siap pakai untuk 4.2:

> Pengujian dilakukan pada 33 skenario yang mencakup 15 perhitungan bangun, 10 skenario
> validasi input, dan 8 skenario penyimpanan Excel. Seluruh skenario (100%) berjalan sesuai
> harapan: hasil perhitungan kesembilan belas rumus tepat, input tidak valid ditolak dengan
> pesan yang jelas, dan data berhasil disimpan dalam format `.xlsx`. Meskipun demikian,
> pengujian menemukan tiga keterbatasan: (1) pesan untuk input tak hingga berbeda dari pesan
> input bukan angka, (2) penyimpanan saat riwayat kosong tidak memberi umpan balik apa pun,
> dan (3) menu "Bersihkan Excel" hanya mengosongkan riwayat di memori tanpa menghapus file
> `.xlsx` yang sudah tersimpan.

---

## E. Temuan Tambahan (di luar 33 skenario)

Temuan ini terlihat saat pengujian berlangsung, berguna untuk 5.2:

1. **Riwayat hilang saat pindah menu.** Variabel `riwayat_perhitungan` dibuat baru setiap
   kali masuk submenu, sehingga hasil yang belum disimpan hilang bila pengguna kembali ke
   menu utama. Belum diuji formal; bisa dijadikan skenario tambahan.
2. **Label menu kurang tepat.** Menu `[9] Bersihkan Excel` pada bangun datar dan
   `[10] Bersihkan Excel` pada bangun ruang hanya membersihkan riwayat di memori.
   Label yang lebih tepat: "Bersihkan Riwayat".
3. **Struktur kolom Excel tidak seragam.** Setiap bangun punya kolom input berbeda, sehingga
   satu baris bisa berisi `NaN` pada kolom bangun lain (contoh: baris Persegi Panjang
   kosong pada kolom `Sisi`). Data tetap terbaca, tetapi kurang rapi untuk analisis lanjutan.
4. **Tidak ada konfirmasi sebelum menimpa file.** Menyimpan dua kali akan menimpa file
   sebelumnya tanpa peringatan.

---

## F. Cara Mereproduksi

```
py handover/uji_otomatis.py
```

Skrip akan menjalankan seluruh skenario A, B, dan C secara otomatis, menampilkan
LULUS/GAGAL per baris, lalu mencetak ringkasan. Kode keluar `0` bila semua lulus,
`1` bila ada yang gagal (berguna bila nanti dipakai pada CI).

Untuk pengujian manual oleh responden, gunakan `handover/panduan-jalan.md`.
