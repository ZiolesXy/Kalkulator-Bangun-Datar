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

def simpan_excel(riwayat_data, nama_file):
    if not riwayat_data:
        return

    df = pd.DataFrame(riwayat_data)
    direktori = f"data/{nama_file}.xlsx"
    df.to_excel(direktori, index=False)
    print(f"Berhasil menyimpan data ke file: {direktori}")