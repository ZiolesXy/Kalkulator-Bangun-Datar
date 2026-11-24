# Tabel Bangun, Input, Output, dan Rumus

Bahan untuk **BAB II (2.1)** dan **BAB III (3.1)**.
Semua nilai contoh sudah diverifikasi dengan menjalankan fungsi pada `calculator/bangun_datar.py`
dan `calculator/bangun_ruang.py`.

Keterangan satuan: input dalam **cm**, luas/keliling dalam **cm²**/**cm**, volume dalam **cm³**.
Nilai π diambil dari `math.pi`. Hasil ditampilkan dengan pembulatan 2 angka desimal.

## A. Bangun Datar (7)

| No | Bangun | Parameter input | Output | Rumus |
|---|---|---|---|---|
| 1 | Persegi | sisi (s) | Keliling, Luas | K = 4s ; L = s² |
| 2 | Persegi Panjang | panjang (p), lebar (l) | Keliling, Luas | K = 2(p + l) ; L = p × l |
| 3 | Segitiga | alas (a), sisi 2 (b), sisi 3 (c), tinggi (t) | Keliling, Luas | K = a + b + c ; L = ½ × a × t |
| 4 | Lingkaran | jari-jari (r) | Keliling, Luas | K = 2πr ; L = πr² |
| 5 | Jajar Genjang | alas (a), sisi miring (b), tinggi (t) | Keliling, Luas | K = 2(a + b) ; L = a × t |
| 6 | Trapesium | sisi sejajar 1 (a), sisi sejajar 2 (b), sisi 3 (c), sisi 4 (d), tinggi (t) | Keliling, Luas | K = a + b + c + d ; L = ½ × (a + b) × t |
| 7 | Belah Ketupat | diameter 1 (d₁), diameter 2 (d₂), sisi (s) | Keliling, Luas | K = 4s ; L = ½ × d₁ × d₂ |

## B. Bangun Ruang (8)

| No | Bangun | Parameter input | Output | Rumus |
|---|---|---|---|---|
| 8 | Kubus | sisi (s) | Luas Permukaan, Volume | LP = 6s² ; V = s³ |
| 9 | Balok | panjang (p), lebar (l), tinggi (t) | Luas Permukaan, Volume | LP = 2(pl + pt + lt) ; V = p × l × t |
| 10 | Tabung | jari-jari (r), tinggi (t) | Luas Permukaan, Volume | LP = 2πr(r + t) ; V = πr²t |
| 11 | Kerucut | jari-jari (r), tinggi (t) | Luas Permukaan, Volume | s = √(r² + t²) ; LP = πr(r + s) ; V = ⅓πr²t |
| 12 | Bola | jari-jari (r) | Luas Permukaan, Volume | LP = 4πr² ; V = 4/3 πr³ |
| 13 | Prisma Segitiga | alas segitiga (a), tinggi segitiga (tₛ), sisi 2 (b), sisi 3 (c), tinggi prisma (T) | Luas Permukaan, Volume | L_alas = ½atₛ ; K_alas = a + b + c ; LP = 2L_alas + K_alas × T ; V = L_alas × T |
| 14 | Limas Segitiga | sisi alas (s), tinggi limas (t) | Luas Permukaan, Volume | Limas beraturan; L_alas = ½ × s × (√3/2)s ; LP = L_alas + 3 × L_sisi_tegak ; V = ⅓ L_alas × t |
| 15 | Limas Segiempat | sisi alas (s), tinggi limas (t) | Luas Permukaan, Volume | L_alas = s² ; t_tegak = √((s/2)² + t²) ; LP = s² + 4 × (½ s × t_tegak) ; V = ⅓ s²t |

Catatan penting untuk laporan:

- Limas segitiga dan limas segiempat **diasumsikan limas beraturan** (alas sama sisi / persegi),
  karena pengguna hanya memasukkan sisi alas dan tinggi.
- Segitiga (No. 3) dan prisma segitiga (No. 13) memakai validasi **ketidaksamaan segitiga**:
  bila a + b ≤ c, a + c ≤ b, atau b + c ≤ a, program menolak dengan pesan
  "Ketiga sisi tidak dapat membentuk segitiga".

## C. Contoh Perhitungan Terverifikasi

| No | Bangun | Input | Hasil 1 | Hasil 2 |
|---|---|---|---|---|
| 1 | Persegi | s = 5 | K = 20,00 cm | L = 25,00 cm² |
| 2 | Persegi Panjang | p = 10, l = 4 | K = 28,00 cm | L = 40,00 cm² |
| 3 | Segitiga | a = 6, b = 8, c = 10, t = 4 | K = 24,00 cm | L = 12,00 cm² |
| 4 | Lingkaran | r = 7 | K = 43,98 cm | L = 153,94 cm² |
| 5 | Jajar Genjang | a = 8, b = 5, t = 4 | K = 26,00 cm | L = 32,00 cm² |
| 6 | Trapesium | a = 6, b = 10, c = 5, d = 5, t = 4 | K = 26,00 cm | L = 32,00 cm² |
| 7 | Belah Ketupat | d₁ = 6, d₂ = 8, s = 5 | K = 20,00 cm | L = 24,00 cm² |
| 8 | Kubus | s = 3 | LP = 54,00 cm² | V = 27,00 cm³ |
| 9 | Balok | p = 4, l = 3, t = 2 | LP = 52,00 cm² | V = 24,00 cm³ |
| 10 | Tabung | r = 7, t = 10 | LP = 747,70 cm² | V = 1.539,38 cm³ |
| 11 | Kerucut | r = 3, t = 4 | LP = 75,40 cm² | V = 37,70 cm³ |
| 12 | Bola | r = 7 | LP = 615,75 cm² | V = 1.436,76 cm³ |
| 13 | Prisma Segitiga | a = 3, tₛ = 4, b = 4, c = 5, T = 10 | LP = 132,00 cm² | V = 60,00 cm³ |
| 14 | Limas Segitiga | s = 6, t = 4 | LP = 54,82 cm² | V = 20,78 cm³ |
| 15 | Limas Segiempat | s = 6, t = 4 | LP = 96,00 cm² | V = 48,00 cm³ |
