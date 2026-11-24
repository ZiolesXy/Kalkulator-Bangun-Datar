"""
Harness pengujian otomatis untuk Aplikasi Kalkulator Bangun Datar/Ruang.

Menjalankan alur menu yang sesungguhnya (menu.menu.main_menu) dengan cara
mengganti builtins.input memakai antrean input terskrip. Tujuannya agar
setiap skenario pada handover/test-case.md benar-benar dieksekusi, bukan
diasumsikan.

Jalankan dari folder project:
    py handover/uji_otomatis.py
"""

import builtins
import contextlib
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.chdir(ROOT)

from menu.menu import main_menu  # noqa: E402


class InputHabis(Exception):
    """Dipakai untuk menghentikan skrip saat antrean input sudah kosong."""


def jalankan_skrip(daftar_input):
    """Menjalankan main_menu() dengan input terskrip, mengembalikan output teks."""
    antrean = list(daftar_input)
    buf = io.StringIO()

    def input_palsu(prompt=""):
        buf.write(prompt)
        if not antrean:
            raise InputHabis()
        nilai = str(antrean.pop(0))
        buf.write(nilai + "\n")
        return nilai

    asli = builtins.input
    builtins.input = input_palsu
    try:
        with contextlib.redirect_stdout(buf):
            try:
                main_menu()
            except InputHabis:
                pass
    finally:
        builtins.input = asli
    return buf.getvalue()


def punya(teks, *potongan):
    return all(p in teks for p in potongan)


def f(nilai):
    return f"{nilai:.2f}"


HASIL = []


def catat(kode, nama, lolos, bukti):
    HASIL.append((kode, nama, "LULUS" if lolos else "GAGAL", bukti))
    print(f"[{'LULUS' if lolos else 'GAGAL'}] {kode} {nama}")
    if not lolos:
        print("        bukti: " + bukti.replace("\n", " ")[:160])


# ---------------------------------------------------------------- Bagian A
A = [
    ("A1", "Persegi sisi=5", ["1", "1", "5"], (20.00, 25.00)),
    ("A2", "Persegi Panjang 10x4", ["1", "2", "10", "4"], (28.00, 40.00)),
    ("A3", "Segitiga 6,8,10 t=4", ["1", "3", "6", "8", "10", "4"], (24.00, 12.00)),
    ("A4", "Lingkaran r=7", ["1", "4", "7"], (43.98, 153.94)),
    ("A5", "Jajar Genjang 8,5,4", ["1", "5", "8", "5", "4"], (26.00, 32.00)),
    ("A6", "Trapesium 6,10,5,5,4", ["1", "6", "6", "10", "5", "5", "4"], (26.00, 32.00)),
    ("A7", "Belah Ketupat 6,8,5", ["1", "7", "6", "8", "5"], (20.00, 24.00)),
    ("A8", "Kubus s=3", ["2", "1", "3"], (54.00, 27.00)),
    ("A9", "Balok 4x3x2", ["2", "2", "4", "3", "2"], (52.00, 24.00)),
    ("A10", "Tabung r=7 t=10", ["2", "3", "7", "10"], (747.70, 1539.38)),
    ("A11", "Kerucut r=3 t=4", ["2", "4", "3", "4"], (75.40, 37.70)),
    ("A12", "Bola r=7", ["2", "5", "7"], (615.75, 1436.76)),
    ("A13", "Prisma Segitiga 3,4,4,5,10", ["2", "6", "3", "4", "4", "5", "10"], (132.00, 60.00)),
    ("A14", "Limas Segitiga s=6 t=4", ["2", "7", "6", "4"], (54.82, 20.78)),
    ("A15", "Limas Segiempat s=6 t=4", ["2", "8", "6", "4"], (96.00, 48.00)),
]

print("=== BAGIAN A: PERHITUNGAN ===")
for kode, nama, skrip, (harap1, harap2) in A:
    keluaran = jalankan_skrip(skrip)
    lolos = punya(keluaran, f(harap1), f(harap2))
    catat(kode, nama, lolos, f"harap {f(harap1)} & {f(harap2)}")

# ---------------------------------------------------------------- Bagian B
print("\n=== BAGIAN B: VALIDASI INPUT ===")
B = [
    ("B1", "Input bukan angka", ["1", "1", "abc", "5"],
     ("Input harus berupa angka.",), None),
    ("B2", "Input nol", ["1", "1", "0", "5"],
     ("Nilai harus lebih besar dari 0.",), None),
    ("B3", "Input negatif", ["1", "1", "-5", "5"],
     ("Nilai harus lebih besar dari 0.",), None),
    ("B4", "Input kosong", ["1", "1", "", "5"],
     ("Input harus berupa angka.",), None),
    ("B5", "Desimal pakai koma 7,5", ["1", "1", "7,5"],
     (), (30.00, 56.25)),
    ("B6", "Input tak hingga inf", ["1", "1", "inf", "5"],
     ("Masukkan angka yang valid.",), None),
    ("B7", "Pilihan menu 99", ["99", "", "0"],
     ("Pilihan tidak valid. Silakan coba lagi.",), None),
    ("B8", "Segitiga mustahil 1,2,10", ["1", "3", "1", "2", "10", "3"],
     ("Perhitungan Gagal: Ketiga sisi tidak dapat membentuk segitiga",), None),
    ("B9", "Prisma alas mustahil 1,2,10", ["2", "6", "1", "4", "2", "10", "5"],
     ("Perhitungan Gagal: Ketiga sisi alas tidak dapat membentuk segitiga",), None),
    ("B10", "Pilihan menu bukan angka x", ["x", "", "0"],
     ("Pilihan tidak valid. Silakan coba lagi.",), None),
]

for kode, nama, skrip, potongan, angka in B:
    keluaran = jalankan_skrip(skrip)
    if angka is not None:
        lolos = punya(keluaran, f(angka[0]), f(angka[1]))
    else:
        lolos = punya(keluaran, *potongan)
    pesan = "message: " + potongan[0] if potongan else f"nilai {f(angka[0])} & {f(angka[1])}"
    catat(kode, nama, lolos, pesan)

# ---------------------------------------------------------------- Bagian C
print("\n=== BAGIAN C: PENYIMPANAN EXCEL ===")
import pandas as pd  # noqa: E402

DATA = os.path.join(ROOT, "data")
XLSX_DATAR = os.path.join(DATA, "hasil_perhitungan_bangun_datar.xlsx")
XLSX_RUANG = os.path.join(DATA, "hasil_perhitungan_bangun_ruang.xlsx")

for berkas in (XLSX_DATAR, XLSX_RUANG):
    if os.path.exists(berkas):
        os.remove(berkas)

# C3 - simpan saat riwayat kosong (dijalankan lebih dulu agar bisa dipastikan file tidak dibuat)
keluaran = jalankan_skrip(["1", "8", "0"])
keluaran += jalankan_skrip(["2", "9", "0"])
lolos = (
    "Berhasil menyimpan" not in keluaran
    and not os.path.exists(XLSX_DATAR)
    and not os.path.exists(XLSX_RUANG)
)
catat("C3", "Simpan saat riwayat kosong", lolos,
      f"file datar ada={os.path.exists(XLSX_DATAR)}, ruang ada={os.path.exists(XLSX_RUANG)}")

# C1 - simpan dengan riwayat terisi (2 bangun datar, lalu 1 bangun ruang)
keluaran = jalankan_skrip(["1", "1", "5", "2", "2", "10", "4", "2", "8", "0"])
lolos = "Berhasil menyimpan data ke file: data/hasil_perhitungan_bangun_datar.xlsx" in keluaran
catat("C1", "Simpan 2 bangun datar", lolos, "pesan simpan datar")

keluaran = jalankan_skrip(["2", "1", "3", "2", "9", "0"])
lolos = "Berhasil menyimpan data ke file: data/hasil_perhitungan_bangun_ruang.xlsx" in keluaran
catat("C1b", "Simpan 1 bangun ruang", lolos, "pesan simpan ruang")

# C2 - cek isi file
try:
    df = pd.read_excel(XLSX_DATAR)
    kolom = list(df.columns)
    lolos = (
        len(df) == 2
        and "Bangun Datar" in kolom
        and "Keliling (cm)" in kolom
        and "Luas (cm2)" in kolom
    )
    bukti = f"baris={len(df)}, kolom={kolom}"
except Exception as exc:  # noqa: BLE001
    lolos, bukti = False, f"gagal membaca: {exc}"
catat("C2", "Isi file datar (2 baris)", lolos, bukti)

try:
    df_ruang = pd.read_excel(XLSX_RUANG)
    lolos = len(df_ruang) == 1 and "Volume (cm3)" in list(df_ruang.columns)
    bukti = f"baris={len(df_ruang)}, kolom={list(df_ruang.columns)}"
except Exception as exc:  # noqa: BLE001
    lolos, bukti = False, f"gagal membaca: {exc}"
catat("C2b", "Isi file ruang (1 baris)", lolos, bukti)

# C4 + C5 - hitung, bersihkan riwayat, lalu simpan
sebelum = os.path.getsize(XLSX_DATAR), os.path.getmtime(XLSX_DATAR)
keluaran = jalankan_skrip(["1", "1", "5", "2", "9", "8", "0"])
lolos = (
    "Riwayat perhitungan berhasil dibersihkan." in keluaran
    and "Berhasil menyimpan" not in keluaran
)
catat("C4", "Bersihkan riwayat", "Riwayat perhitungan berhasil dibersihkan." in keluaran, "pesan bersihkan")
catat("C5", "Bersihkan lalu simpan", lolos, "tidak ada pesan simpan setelah dibersihkan")

# C6 - file lama masih ada dan tidak berubah
sesudah = os.path.getsize(XLSX_DATAR), os.path.getmtime(XLSX_DATAR)
lolos = os.path.exists(XLSX_DATAR) and sebelum == sesudah
catat("C6", "File lama tetap ada setelah Bersihkan", lolos,
      f"ukuran/mtime sama={sebelum == sesudah}")

# ---------------------------------------------------------------- Ringkasan
total = len(HASIL)
lulus = sum(1 for h in HASIL if h[2] == "LULUS")
print("\n=== RINGKASAN ===")
for kelompok, awalan in (("Perhitungan (A)", "A"), ("Validasi input (B)", "B"),
                         ("Penyimpanan Excel (C)", "C")):
    bagian = [h for h in HASIL if h[0].startswith(awalan)]
    ok = sum(1 for h in bagian if h[2] == "LULUS")
    print(f"{kelompok:24} {ok}/{len(bagian)}")
print(f"{'TOTAL':24} {lulus}/{total} ({lulus / total * 100:.1f}%)")

gagal = [h for h in HASIL if h[2] == "GAGAL"]
if gagal:
    print("\nYang gagal:")
    for kode, nama, _, bukti in gagal:
        print(f"- {kode} {nama}: {bukti}")
sys.exit(0 if not gagal else 1)
