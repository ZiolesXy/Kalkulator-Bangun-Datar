# Potongan Kode untuk 4.1.2 (Code Generation)

Lima potongan kode inti beserta penjelasannya. Potongan diambil dari source code
apa adanya (hanya dipangkas bagian yang tidak relevan), jadi aman ditempel ke laporan.

Setiap potongan disertai **kalimat siap pakai** agar penyusun laporan tidak perlu
menebak maksud kodenya.

---

## 1. Validasi input angka — `utils/validation.py`

```python
def cek_angka(prompt):
    while True:
        try:
            nilai = float(
                input(prompt).strip().replace(",", ".")
            )

            if not math.isfinite(nilai):
                print("Masukkan angka yang valid.")
                continue

            return nilai

        except ValueError:
            print("Input harus berupa angka.")
```

**Penjelasan:**

- Perulangan `while True` membuat program terus meminta input sampai nilai valid,
  sehingga aplikasi tidak pernah berhenti karena kesalahan pengguna.
- `input(prompt).strip()` menghapus spasi di awal dan akhir, misalnya `" 5 "` tetap
  dibaca sebagai `5`.
- `.replace(",", ".")` menyesuaikan kebiasaan penulisan desimal Indonesia: pengguna
  boleh mengetik `7,5` dan program membacanya sebagai `7.5`.
- `float(...)` mengubah teks menjadi bilangan; bila gagal, Python melempar `ValueError`
  yang ditangkap blok `except` dan diterjemahkan menjadi pesan yang mudah dipahami.
- `math.isfinite()` menolak nilai `inf`, `-inf`, dan `NaN` yang secara sintaks memang
  bilangan valid, tetapi tidak bermakna untuk perhitungan geometri.

**Kalimat untuk laporan:**
> Fungsi `cek_angka()` menerapkan pola *defensive programming* dengan perulangan dan
> penanganan pengecualian `ValueError`. Selain memastikan input berupa bilangan,
> fungsi ini menormalkan pemisah desimal dan menolak nilai tak hingga menggunakan
> `math.isfinite()`.

---

## 2. Validasi nilai positif — `utils/validation.py`

```python
def cek_angka_positif(prompt):
    while True:
        value = cek_angka(prompt)

        if value > 0:
            return value

        print("Nilai harus lebih besar dari 0.")
```

**Penjelasan:**

- Fungsi ini **mendelegasikan** pemeriksaan tipe data ke `cek_angka()`, lalu menambah
  aturan domain: panjang sisi, jari-jari, dan tinggi tidak boleh nol atau negatif.
- Pemisahan tanggung jawab ini membuat kode tidak berulang: aturan "harus angka"
  cukup ditulis sekali dan dipakai oleh seluruh 15 bangun.
- Pemeriksaan `value > 0` juga otomatis menolak `-0.0` dan nilai negatif.

**Kalimat untuk laporan:**
> Aturan validasi dipisahkan menjadi dua lapis, yaitu pemeriksaan tipe data pada
> `cek_angka()` dan pemeriksaan domain nilai pada `cek_angka_positif()`. Pendekatan ini
> menghindari duplikasi kode dan memastikan seluruh modul kalkulator memakai aturan
> validasi yang sama.

---

## 3. Validasi geometri segitiga — `calculator/bangun_datar.py`

```python
def hitung_segitiga(alas, sisi2, sisi3, tinggi):
    if alas + sisi2 <= sisi3 or alas + sisi3 <= sisi2 or sisi2 + sisi3 <= alas:
        raise ValueError("Ketiga sisi tidak dapat membentuk segitiga")

    keliling = alas + sisi2 + sisi3
    luas = (alas * tinggi) / 2

    return keliling, luas
```

**Penjelasan:**

- Ketiga sisi baru dapat membentuk segitiga bila jumlah dua sisi selalu **lebih besar**
  dari sisi ketiga. Bila salah satu kondisi dilanggar, program menolak perhitungan.
- Fungsi **melempar** `ValueError`, bukan langsung mencetak pesan. Dengan begitu fungsi
  perhitungan tetap murni (tanpa efek samping) dan pesan kesalahan ditangani di lapisan
  antarmuka, yaitu `calculator/menu.py` pada blok `except ValueError`.
- Logika yang sama dipakai pada `hitung_prisma_segitiga()` untuk memeriksa sisi alas.

**Kalimat untuk laporan:**
> Penerapan ketidaksamaan segitiga mencegah hasil perhitungan yang tidak bermakna
> secara geometri. Fungsi perhitungan tidak menampilkan pesan sendiri, melainkan
> melempar `ValueError` yang ditangkap lapisan antarmuka, sehingga pemisahan antara
> logika bisnis dan tampilan tetap terjaga.

---

## 4. Perhitungan dengan fungsi matematika — `calculator/bangun_ruang.py`

```python
def hitung_kerucut(jari_jari, tinggi):
    garis_pelukis = math.sqrt((jari_jari**2) + (tinggi**2))

    luas_permukaan = math.pi * jari_jari * (jari_jari + garis_pelukis)
    volume = (1 / 3) * math.pi * (jari_jari**2) * tinggi

    return luas_permukaan, volume
```

**Penjelasan:**

- Garis pelukis kerucut tidak diminta dari pengguna, tetapi dihitung dari jari-jari dan
  tinggi memakai teorema Pythagoras: `s = √(r² + t²)`. Ini mengurangi beban input dan
  mencegah ketidakkonsistenan data.
- `math.pi` dipakai agar nilai π konsisten dan presisi, bukan angka 3,14 yang dibulatkan.
- Fungsi mengembalikan **dua nilai sekaligus** dalam bentuk tuple, sehingga pemanggil
  dapat menampungnya dengan `luas_permukaan, volume = hitung_kerucut(r, t)`.

**Kalimat untuk laporan:**
> Nilai turunan seperti garis pelukis kerucut dihitung di dalam fungsi agar pengguna
> hanya memasukkan besaran dasar. Modul `math` menyediakan `math.pi` dan `math.sqrt`
> sehingga hasil lebih presisi dibanding konstanta yang dibulatkan manual.

---

## 5. Penyimpanan hasil ke Excel — `calculator/menu.py`

```python
def simpan_excel(riwayat_data, nama_file):
    if not riwayat_data:
        return

    df = pd.DataFrame(riwayat_data)
    direktori = f"data/{nama_file}.xlsx"
    df.to_excel(direktori, index=False)
    print(f"Berhasil menyimpan data ke file: {direktori}")
```

**Penjelasan:**

- Riwayat perhitungan disimpan sebagai *list of dictionary*. Setiap kunci dictionary
  menjadi nama kolom, sehingga tabel Excel terbentuk otomatis tanpa mendefinisikan
  kolom satu per satu.
- `if not riwayat_data: return` mencegah pembuatan file kosong.
  **Catatan jujur:** pada kondisi ini program tidak menampilkan pesan apa pun — sudah
  tercatat sebagai temuan C3 di `test-case.md`.
- `pd.DataFrame(...)` mengubah list menjadi tabel dua dimensi.
- `to_excel(..., index=False)` menulis file tanpa kolom indeks baris (0, 1, 2, ...),
  agar tabel bersih saat dibuka di Excel.
- Parameter `nama_file` membuat satu fungsi dapat melayani dua jenis data
  (`hasil_perhitungan_bangun_datar` dan `hasil_perhitungan_bangun_ruang`).

**Kalimat untuk laporan:**
> Integrasi pandas memungkinkan riwayat perhitungan diubah menjadi tabel dan langsung
> diekspor ke berkas `.xlsx` melalui `DataFrame.to_excel()`. Penggunaan parameter
> `nama_file` membuat satu fungsi penyimpanan dapat dipakai ulang untuk kedua kategori
> bangun, sedangkan `index=False` menjaga format tabel tetap rapi.

---

## Cara memakai file ini

1. Tempel kode dan penjelasan ke 4.1.2 dengan urutan di atas (dari validasi menuju
   penyimpanan) agar alurnya runtut.
2. Sebelum menempel, jalankan `py main.py` dan pastikan potongan kode masih sama dengan
   file aslinya. **Jangan mengubah kode setelah laporan dikunci.**
3. Nomor baris pada laporan sebaiknya disesuaikan dengan file asli di editor, bukan
   disalin dari file ini, karena potongan sengaja dipangkas.
