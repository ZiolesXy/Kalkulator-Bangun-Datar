# JOB DESK — Laporan Final Project

**Project:** Aplikasi Kalkulator Bangun Datar dan Bangun Ruang (CLI, Python + Pandas)
**Posisi:** Pemilik project hanya mengerjakan aplikasi. Penyusunan laporan dikerjakan anggota lain.

Tujuan dokumen ini: membagi tugas secara jelas supaya tidak terjadi revisi bolak-balik
dan tidak ada bagian laporan yang diklaim tanpa dasar.

---

## 0. Prinsip Pembagian

- **Developer** = orang yang menulis kode. Bertanggung jawab atas semua isi laporan yang
  menyangkut cara kerja program: alur sistem, kode, screenshot, data pengujian, dan batasan aplikasi.
- **Penyusun laporan** = bertanggung jawab atas referensi, naskah naratif, kuesioner,
  pengolahan hasil uji, format, dan pengumpulan.
- Bagian teknis (3.2 dan 4.1.2) **tidak boleh** ditulis tanpa versi dari developer, karena
  penyusun tidak mengetahui detail implementasi dan berisiko salah menjelaskan saat sidang.
- Serah terima dilakukan **sekali, sekaligus** (satu folder/zip), bukan dicicil per pertanyaan.

---

## 1. Yang Harus Disiapkan Penyusun Laporan (di luar tanggung jawab developer)

| No | Item | Catatan |
|---|---|---|
| 1 | Template resmi laporan kampus | Margin, font, penomoran bab, halaman romawi/arab, cover |
| 2 | Identitas lengkap | Judul final, 5 nama + NIM, dosen pengampu, prodi, fakultas, tahun, logo kampus |
| 3 | **6 jurnal** (1 untuk 1.1 + 5 untuk 2.2) | PDF disimpan, dimasukkan ke Mendeley |
| 4 | Daftar Pustaka via **Mendeley** | Wajib sesuai outline. Sepakati format APA atau IEEE |
| 5 | Naskah Bab I (1.1–1.3), Bab II (2.1–2.2), Bab V | Murni kerja tulis-menulis + referensi |
| 6 | Pelaksanaan usability testing | Cari 5–10 responden, sebar kuesioner, rekap skor, tulis analisis 4.2 |
| 7 | Instrumen kuesioner | SUS 10 pertanyaan atau Likert; susun lalu cetak / Google Form |
| 8 | Daftar Riwayat Hidup tiap anggota | Termasuk **pembagian tugas**; bagian developer disediakan pada bagian 2E |
| 9 | Lembar Persembahan, Kata Pengantar, Abstraksi | Abstrak ditulis setelah angka hasil uji keluar |
| 10 | Daftar Isi / Simbol / Gambar / Tabel | Generate otomatis dari Word setelah naskah jadi |
| 11 | Finishing | Print, jilid, cek plagiarisme, submit |

---

## 2. Yang Harus Diserahkan Developer (Paket Handover)

Diserahkan sekali, dalam satu folder/zip, disertai pesan pengantar (bagian 4).

### A. Kode dan Cara Menjalankan

- [ ] Source code final (zip atau link repo + commit/tag terakhir). **Freeze** — jangan diubah setelah diserahkan.
- [ ] `README` teknis: cara install (`py -m pip install pandas openpyxl`) dan cara jalan (`py main.py`).
- [ ] Spesifikasi environment: versi Python, Pandas, Openpyxl (dari `py --version` dan `py -m pip show`).
- [ ] Panduan menjalankan aplikasi untuk responden (3 langkah), atau **video demo 1–2 menit**
      sebagai cadangan bila laptop responden tidak memiliki Python.

### B. Materi Teknis untuk Bab II dan III

- [ ] **Tabel 15 bangun** — kolom: Nama | Jenis (datar/ruang) | Parameter input | Output | Rumus.
- [ ] **Struktur folder + peran tiap file:**
      `main.py` (entry point), `menu/menu.py` (navigasi menu),
      `calculator/menu.py` (input pengguna + simpan Excel),
      `calculator/bangun_datar.py` dan `calculator/bangun_ruang.py` (rumus),
      `utils/validation.py` (validasi input), `utils/display.py` (tampilan),
      `data/` (output `.xlsx`).
- [ ] **Bagan alur (untuk 3.2)** — alur nyata: `main.py` → menu utama → submenu bangun
      datar/ruang → input + validasi → perhitungan → tampil hasil → simpan Excel.
      Dibuat oleh developer (draw.io), penyusun menyalin bagan + menulis penjelasan.
- [ ] **Poin teori tools (2.1):** Python, CLI, modularisasi, `try-except`/`ValueError`,
      modul `math` (`pi`, `sqrt`, `isfinite`), Pandas `DataFrame`, Openpyxl — masing-masing 1–2 kalimat.

### C. Materi Teknis untuk Bab IV

- [ ] **Code generation (4.1.2)** — 4–5 potongan kode inti **beserta penjelasannya:**
      `cek_angka` (penanganan input salah + `replace(",", ".")`), `cek_angka_positif`,
      `hitung_segitiga` (ketidaksamaan segitiga), `hitung_kerucut` (`garis_pelukis` dengan `sqrt`),
      `simpan_excel` (`pd.DataFrame` → `to_excel`).
      Cek `data/Potongan Code.docx` — bila belum ada penjelasan, lengkapi.
- [ ] **Screenshot semua layar:** Menu Utama, Menu Bangun Datar, input, hasil perhitungan,
      Menu Bangun Ruang, Tentang Aplikasi, penolakan input salah.
      Simpan rapi, misal `gambar/menu-utama.png`.
- [ ] **File bukti Excel** — `hasil_perhitungan_bangun_datar.xlsx` dan
      `hasil_perhitungan_bangun_ruang.xlsx` yang sudah terisi, plus screenshot dibuka di Excel.
      **Catatan:** folder `data/` masuk `.gitignore`, jadi file ini harus diserahkan manual
      (bukan lewat repo).
- [ ] **Tabel hasil test case** (sudah terisi oleh developer): No | Skenario | Input |
      Output diharapkan | Hasil. Wajib mencakup:
      1. input huruf, 2. input `0`, 3. input negatif, 4. segitiga mustahil (1, 2, 10),
      5. simpan Excel berhasil, 6. simpan saat riwayat kosong, 7. bersihkan riwayat,
      8. pilih menu salah.

### D. Batasan dan Kejujuran Teknis (untuk 1.5 dan 5.2)

- [ ] Daftar batasan aplikasi agar laporan tidak mengklaim berlebihan:
      1. Berbasis teks/CLI, bukan GUI atau web.
      2. Satuan tetap cm; tidak ada konversi satuan.
      3. Menu "Bersihkan Excel" hanya mengosongkan riwayat di memori sesi berjalan —
         **file `.xlsx` tidak terhapus**.
      4. Riwayat hilang jika kembali ke menu utama sebelum menekan simpan.
      5. Simpan Excel saat riwayat kosong tidak memberi pesan apa pun.
      6. Limas segitiga dan limas segiempat diasumsikan **limas beraturan**
         (input hanya sisi alas + tinggi).
      7. Data disimpan lokal, tanpa database dan tanpa login.
- [ ] Bila memungkinkan, perbaiki dulu poin 3–6 sebelum uji usability. Bila tidak,
      cukup ditulis sebagai batasan — tetapi **beri tahu penyusun laporan** agar tidak
      menulis klaim yang salah (contoh salah: "menghapus file Excel").

### E. Untuk Daftar Riwayat Hidup

Deskripsi kontribusi developer (siap tempel):

> Bertanggung jawab atas perancangan dan pengembangan aplikasi, meliputi perancangan
> struktur modul, implementasi 7 rumus bangun datar dan 8 rumus bangun ruang, validasi
> input, integrasi Pandas untuk ekspor Excel, serta pengujian fungsional aplikasi.

Developer juga menjadi narahubung teknis saat sidang. Siapkan jawaban untuk:
kenapa memilih CLI, kenapa memakai Pandas, dan bagaimana rumus limas dihitung.

---

## 3. Pembagian Bab

| Bagian | Pemilik |
|---|---|
| 1.1–1.3 Latar Belakang, Perumusan Masalah, Maksud & Tujuan | Penyusun |
| 1.4 Metode Penelitian | Penyusun (diskusi dulu dengan developer) |
| 1.5 Ruang Lingkup | Developer beri daftar batasan → penyusun merapikan kalimat |
| 2.1 Tinjauan Pustaka | Penyusun (bahan teori dari developer) |
| 2.2 Penelitian Terkait | Penyusun |
| 3.1 Analisa Kebutuhan Program | Developer (fungsional/non-fungsional) → penyusun memoles |
| 3.2 Kerangka Kerja | **Developer** (bagan + alur sistem) |
| 4.1.1 Rancangan Antarmuka | Developer (screenshot) → penyusun menulis deskripsi |
| 4.1.2 Code Generation | **Developer** |
| 4.2 Usability Testing | Penyusun (developer bantu siapkan aplikasi + panduan run) |
| 5.1 Kesimpulan | Penyusun |
| 5.2 Saran | Penyusun (ambil dari daftar batasan developer) |
| Daftar Pustaka, Riwayat Hidup, format, finishing | Penyusun |

---

## 4. Pesan Pengantar untuk Grup (siap copy)

> Ini paket final dari saya buat laporan:
> (1) source code + README cara jalan,
> (2) tabel 15 bangun + rumus,
> (3) bagan alur sistem,
> (4) potongan kode untuk 4.1.2 beserta penjelasannya,
> (5) screenshot semua menu + bukti Excel,
> (6) tabel hasil pengujian,
> (7) daftar batasan aplikasi,
> (8) deskripsi tugas saya untuk Riwayat Hidup.
>
> Bagian 3.2, 4.1.2, dan batasan pada 1.5 tolong pakai versi saya apa adanya karena
> itu sesuai kode. Yang saya tidak kerjakan: referensi/jurnal, Bab I–II naratif,
> kuesioner & rekap usability, format, dan Daftar Pustaka.
>
> Kalau ada yang perlu diklarifikasi soal program, tanya saya **sebelum naskah dikunci**.

---

## 5. Checklist Serah Terima

- [ ] Source code final + README + versi environment
- [ ] Tabel 15 bangun + rumus
- [ ] Struktur folder dan peran tiap file
- [ ] Bagan alur sistem (gambar + penjelasan singkat)
- [ ] Potongan kode 4.1.2 + penjelasan tiap potongan
- [ ] Screenshot semua layar + screenshot input salah
- [ ] File Excel bukti + screenshot
- [ ] Tabel hasil test case terisi
- [ ] Daftar batasan aplikasi
- [ ] Deskripsi kontribusi untuk Daftar Riwayat Hidup
- [ ] Pesan pengantar (bagian 4) sudah dikirim ke grup

---

## 6. File Pendukung di Folder `handover/`

| File | Isi | Dipakai untuk |
|---|---|---|
| `jobdesk.md` | Dokumen ini — pembagian tugas dan checklist serah terima | Koordinasi kelompok |
| `tabel-rumus.md` | 15 bangun + parameter input + rumus + contoh hasil terverifikasi | Bab II (2.1) dan Bab III (3.1) |
| `test-case.md` | 33 skenario uji (perhitungan, validasi input, Excel) + ringkasan + temuan | Bab IV (4.1.2 dan 4.2) |
| `panduan-jalan.md` | Cara install & menjalankan aplikasi, troubleshooting, skenario tugas | Pelaksanaan usability testing |
| `bagan-alur.md` | Flowchart alur program + struktur modul + penjelasan tiap tahap | Bab III (3.2) |
| `potongan-kode.md` | 5 potongan kode inti + penjelasan + kalimat siap pakai | Bab IV (4.1.2) |
| `uji_otomatis.py` | Skrip pengujian otomatis 33 skenario, mencetak LULUS/GAGAL | Reproduksi bukti pengujian |

Status pengisian:

- `tabel-rumus.md` — **selesai**, nilai contoh sudah diverifikasi dengan menjalankan fungsi.
- `test-case.md` — **selesai dan sudah diuji** (24 Nov 2026, Python 3.14.0, pandas 3.1.0,
  openpyxl 3.1.5): 33/33 lulus. Bagian C3, C5, C6 lolos sesuai kode tetapi dicatat sebagai
  keterbatasan yang perlu diperbaiki.
- `panduan-jalan.md` — selesai, tinggal dibagikan ke responden.
- `uji_otomatis.py` — selesai, jalankan `py handover/uji_otomatis.py` untuk reproduksi.
