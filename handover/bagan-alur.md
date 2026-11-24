# Bagan Alur Sistem (Bahan untuk 3.2 Kerangka Kerja)

File ini berisi bagan siap pakai untuk laporan. Diagram ditulis dengan sintaks Mermaid,
sehingga bisa langsung dirender menjadi gambar.

**Cara membuat gambar untuk laporan (pilih satu):**

1. Buka <https://mermaid.live>, tempel isi blok kode di bawah, klik **Actions → PNG**.
2. Atau gambar ulang di <https://app.diagrams.net> (draw.io) mengikuti alur yang sama.
3. Atau minta anggota yang biasa membuat diagram mengikuti daftar tahap pada bagian
   "Penjelasan Tahap" — alurnya sudah pasti, tidak perlu menebak.

Simpan hasilnya sebagai `gambar/bagan-alur.png` dan `gambar/struktur-modul.png`.

---

## 1. Bagan Alur Utama (Flowchart)

```mermaid
flowchart TD
    A([Mulai]) --> B["main.py<br/>memanggil main_menu()"]
    B --> C[Tampilkan Menu Utama]
    C --> D{Input pilihan}
    D -->|"1"| E[Submenu Bangun Datar]
    D -->|"2"| F[Submenu Bangun Ruang]
    D -->|"3"| G[Tentang Aplikasi]
    D -->|"0"| Z([Selesai])
    D -->|"selain 0-3"| D1["Pesan: Pilihan tidak valid"] --> C

    E --> E0{Tampilkan daftar bangun datar}
    E0 -->|"1-7"| E1[Input parameter bangun]
    E0 -->|"8"| E2[simpan_excel]
    E0 -->|"9"| E3[Bersihkan riwayat di memori]
    E0 -->|"0"| C
    E2 --> E0
    E3 --> E0

    E1 --> V1{cek_angka_positif}
    V1 -->|"bukan angka / kosong"| VE["Pesan: Input harus berupa angka"] --> E1
    V1 -->|"0 atau negatif"| VN["Pesan: Nilai harus lebih besar dari 0"] --> E1
    V1 -->|"inf / NaN"| VI["Pesan: Masukkan angka yang valid"] --> E1
    V1 -->|valid| E4["Hitung di bangun_datar.py"]
    E4 -->|"segitiga tidak valid"| VT["Perhitungan Gagal:<br/>Ketiga sisi tidak dapat membentuk segitiga"] --> E9
    E4 --> E5[Tampilkan keliling dan luas]
    E5 --> E6[Tambahkan ke riwayat memori]
    E6 --> E9{Pilih aksi}
    E9 -->|"1 Hitung Lagi"| E1
    E9 -->|"2 Pilih Bangun Lain"| E0
    E9 -->|"0 Menu Utama"| C

    F --> F0{Tampilkan daftar bangun ruang}
    F0 -->|"1-8"| F1[Input parameter bangun]
    F0 -->|"9"| F2[simpan_excel]
    F0 -->|"10"| F3[Bersihkan riwayat di memori]
    F0 -->|"0"| C
    F2 --> F0
    F3 --> F0

    F1 --> W1{cek_angka_positif}
    W1 -->|"tidak valid"| WN["Pesan kesalahan"] --> F1
    W1 -->|valid| F4["Hitung di bangun_ruang.py"]
    F4 -->|"alas prisma tidak valid"| WT["Perhitungan Gagal:<br/>Ketiga sisi alas tidak dapat membentuk segitiga"] --> F9
    F4 --> F5[Tampilkan luas permukaan dan volume]
    F5 --> F6[Tambahkan ke riwayat memori]
    F6 --> F9{Pilih aksi}
    F9 -->|"1 Hitung Lagi"| F1
    F9 -->|"2 Pilih Bangun Lain"| F0
    F9 -->|"0 Menu Utama"| C

    E2 --> X["pd.DataFrame → to_excel<br/>data/hasil_perhitungan_bangun_datar.xlsx"]
    F2 --> Y["pd.DataFrame → to_excel<br/>data/hasil_perhitungan_bangun_ruang.xlsx"]
    X --> E0
    Y --> F0

    G --> B1[Tampilkan nama anggota] --> C
```

## 2. Bagan Struktur Modul (Dependency)

```mermaid
flowchart LR
    M["main.py"] --> MU["menu/menu.py<br/>main_menu, submenu, about"]
    MU --> CM["calculator/menu.py<br/>input pengguna, simpan_excel"]
    MU --> UD["utils/display.py<br/>print_judul, print_garis, pause"]
    CM --> BD["calculator/bangun_datar.py<br/>7 fungsi rumus"]
    CM --> BR["calculator/bangun_ruang.py<br/>8 fungsi rumus"]
    CM --> UV["utils/validation.py<br/>cek_angka, cek_angka_positif, pilihan_menu"]
    UV --> UD
    CM --> PD[("pandas + openpyxl")]
    PD --> XL[("data/*.xlsx")]
```

## 3. Penjelasan Tahap (untuk naskah 3.2)

Tulis satu paragraf pendek per tahap, mengikuti urutan ini:

| Tahap | Penjelasan yang bisa dipakai |
|---|---|
| 1. Inisialisasi | `main.py` menjadi titik masuk aplikasi. Fungsi `main()` memanggil `main_menu()` dari modul `menu/menu.py`, sehingga seluruh alur program terpusat pada satu pintu masuk. |
| 2. Menu utama | Menampilkan empat pilihan: kalkulator bangun datar, kalkulator bangun ruang, tentang aplikasi, dan keluar. Input divalidasi oleh `pilihan_menu()` agar hanya nilai yang terdaftar yang diterima. |
| 3. Submenu bangun datar | Menampilkan tujuh bangun datar ditambah opsi simpan ke Excel, bersihkan riwayat, dan kembali. Riwayat disimpan pada list `riwayat_perhitungan` di dalam fungsi ini. |
| 4. Input parameter | Setiap bangun meminta parameter sesuai kebutuhannya (contoh: persegi hanya sisi; trapesium meminta empat sisi dan tinggi). Semua input melewati `cek_angka_positif()` untuk menolak nilai bukan angka, nol, negatif, dan tak hingga. |
| 5. Perhitungan | Perhitungan dipisahkan dari tampilan: fungsi murni di `bangun_datar.py` dan `bangun_ruang.py` menerima parameter dan mengembalikan hasil. Pemisahan ini memudahkan pengujian dan penambahan bangun baru. |
| 6. Validasi geometri | Khusus segitiga dan prisma segitiga, program memeriksa ketidaksamaan segitiga sebelum menghitung. Bila gagal, fungsi melempar `ValueError` yang ditangkap di `calculator/menu.py` dan ditampilkan sebagai pesan kesalahan. |
| 7. Penampilan hasil | Hasil ditampilkan dengan format dua angka desimal beserta satuan cm, cm², atau cm³, lalu baris data ditambahkan ke riwayat agar bisa disimpan. |
| 8. Navigasi aksi | Setelah hasil tampil, pengguna memilih hitung lagi, pilih bangun lain, atau kembali ke menu utama. Struktur perulangan bersarang inilah yang menjaga aplikasi tetap berjalan tanpa restart. |
| 9. Penyimpanan | `simpan_excel()` mengubah list riwayat menjadi `DataFrame` pandas lalu menuliskannya dengan `to_excel()` (engine openpyxl) ke folder `data/`. |

## 4. Catatan Kejujuran untuk 3.2

Saat menjelaskan tahap 4 dan 9, jangan menulis klaim berikut karena tidak sesuai kode:

- "Riwayat tersimpan permanen di database" → **salah**, riwayat hanya ada di memori sesi berjalan.
- "Bersihkan Excel menghapus file" → **salah**, hanya mengosongkan list di memori.
- "Simpan memberi notifikasi bila data kosong" → **salah**, tidak ada pesan apa pun.

Ketiganya sudah tercatat sebagai temuan di `handover/test-case.md` bagian C dan E.
