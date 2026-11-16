import pandas as pd
from .bangun_datar import(
    hitung_persegi,
    hitung_persegi_panjang,
    hitung_segitiga,
    hitung_lingkaran,
    hitung_jajar_genjang,
    hitung_trapesium,
    hitung_belah_ketupat
)
from utils.validation import cek_angka_positif, pilihan_menu
from utils.display import print_judul, print_garis

def hitung_bangun(pilihan):
    if pilihan == "1":
        sisi = cek_angka_positif("Masukan Panjang sisi (cm) : ")

        keliling, luas = hitung_persegi(sisi)

        return "Persegi", {
            "Sisi": sisi
        }, keliling, luas

    if pilihan == "2":
        panjang = cek_angka_positif("Masukan Panjang (cm) : ")
        lebar = cek_angka_positif("Masukan Lebar (cm) : ")

        keliling, luas = hitung_persegi_panjang(panjang, lebar)

        return "Persegi Panjang", {
            "Panjang": panjang,
            "Lebar": lebar
        }, keliling, luas

    if pilihan == "3":
        alas = cek_angka_positif("Masukan Panjang Alas (cm) : ")
        sisi2 = cek_angka_positif("Masukan Panjang Sisi ke-2 (cm) : ")
        sisi3 = cek_angka_positif("Masukan Panjang Sisi ke-3 (cm) : ")
        tinggi = cek_angka_positif("Masukan Tinggi (cm) : ")

        keliling, luas = hitung_segitiga(alas, sisi2, sisi3, tinggi)

        return "Segitiga", {
            "Alas": alas,
            "Sisi 2": sisi2,
            "Sisi 3": sisi3,
            "Tinggi": tinggi
        }, keliling, luas

    if pilihan == "4":
        jari_jari = cek_angka_positif("Masukan Jari Jari (cm) : ")

        keliling, luas = hitung_lingkaran(jari_jari)

        return "Lingkaran", {
            "Jari Jari": jari_jari,
        }, keliling, luas

    if pilihan == "5":
        alas = cek_angka_positif("Masukan Alas (cm) : ")
        sisi_miring = cek_angka_positif("Masukan Sisi Miring (cm) : ")
        tinggi = cek_angka_positif("Masukan Tinggi (cm) : ")

        keliling, luas = hitung_jajar_genjang(alas, sisi_miring, tinggi)

        return "Jajar Genjang", {
            "Alas": alas,
            "Sisi Miring": sisi_miring,
            "Tinggi": tinggi
        }, keliling, luas

    if pilihan == "6":
        sisi1 = cek_angka_positif("Masukan Sisi ke-1 (cm) : ")
        sisi2 = cek_angka_positif("Masukan Sisi ke-2 (cm) : ")
        sisi3 = cek_angka_positif("Masukan Sisi ke-3 (cm) : ")
        sisi4 = cek_angka_positif("Masukan Sisi ke-4 (cm) : ")
        tinggi = cek_angka_positif("Masukan Tinggi (cm) : ")

        keliling, luas = hitung_trapesium(sisi1, sisi2, sisi3, sisi4, tinggi)

        return "Trapesium", {
            "Sisi 1": sisi1,
            "Sisi 2": sisi2,
            "Sisi 3": sisi3,
            "Sisi 4": sisi4,
            "Tinggi": tinggi
        }, keliling, luas

    if pilihan == "7":
        diameter1 = cek_angka_positif("Masukan Panjang Diameter Pertama (cm) : ")
        diameter2 = cek_angka_positif("Masukan Panjang Diameter Kedua (cm) : ")
        sisi = cek_angka_positif("Masukan Panjang Sisi (cm) : ")

        keliling, luas = hitung_belah_ketupat(diameter1, diameter2, sisi)

        return "Belah Ketupat", {
            "Diameter Pertama": diameter1,
            "Diameter Kedua": diameter2,
            "Sisi": sisi
        }, keliling, luas

def simpan_excel(riwayat_data):
    if not riwayat_data:
        return

    df = pd.DataFrame(riwayat_data)
    nama_file = "data/hasil_perhitungan_bangun_datar.xlsx"
    df.to_excel(nama_file, index=False)
    print(f"Berhasil menyimpan data ke file: {nama_file}")

def menu_kalkulator():
    riwayat_perhitungan = []
    while True:
        print_judul("PENGHITUNG LUAS DAN KELILING BANGUN DATAR")

        print("[1] Persegi")
        print("[2] Persegi Panjang")
        print("[3] Segitiga")
        print("[4] Lingkaran")
        print("[5] Jajar Genjang")
        print("[6] Trapesium")
        print("[7] Belah Ketupat")
        print("[8] Simpan Ke Excel")
        print("[9] Bersihkan Excel")
        print("[0] Kembali ke Menu Utama")

        print_garis()

        valid = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

        pilihan = pilihan_menu("Pilih Bangun Datar : ", valid)
        if pilihan == "0":
            return
        elif pilihan == "8":
            simpan_excel(riwayat_perhitungan)
            continue
        elif pilihan == "9":
            riwayat_perhitungan.clear
            continue

        while True:
            try:
                nama_bangun, detail, keliling, luas = hitung_bangun(pilihan)
                print_judul("HASIL PERHITUNGAN")

                for label, value in detail.items():
                    print(f"{label:<14}: {value:g} cm")

                print(f"Keliling      : {keliling:.2f} cm")
                print(f"Luas          : {luas:.2f} cm2")

                data_baru = {"Bangun Datar": nama_bangun}
                data_baru.update(detail)
                data_baru["Keliling (cm)"] = round(keliling, 2)
                data_baru["Luas (cm2)"] = round(luas, 2)
                riwayat_perhitungan.append(data_baru)

                print_garis()

            except ValueError as error:
                print(f"Perhitungan Gagal: {error}")

            print("[1] Hitung Lagi")
            print("[2] Pilih Bangun Lain")
            print("[0] Menu Utama")

            valid = ("0", "1", "2")
            aksi = pilihan_menu("Pilih Aksi : ", valid)

            if aksi == "1":
                continue
            elif aksi == "2":
                break
            elif aksi == "0":
                return