from utils.display import print_judul, print_garis, pause
from calculator.menu import simpan_excel, hitung_bangun
from utils.validation import pilihan_menu
import time

def main_menu():
    while True:
        print_judul("Kalkulator Bangun Datar")

        print_garis()

        print("[1] Kalkulator Bangun Datar")
        print("[2] Tentang Aplikasi")
        print("[0] Keluar")

        valid = ("1", "2", "0")
        pilihan = pilihan_menu("Masukan Pilihan Anda: ", valid)

        if pilihan == "1":
            menu_kalkulator()
        elif pilihan == "2":
            menu_about()
        elif pilihan == "0":
            print_judul("TERIMA KASIH")
            break

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
            simpan_excel(riwayat_perhitungan, "hasil_perhitungan_bangun_datar")
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

def menu_about():
    print_judul("TENTANG APLIKASI")
    
    print("Ini adalah Aplikasi peghitung luas dan keliling dari suatu \nbangun luar yang dilengkapi oleh fitur simpan ke xlsx")
    print_garis()
    print("Aplikasi ini dibangun oleh : ")
    print_garis()
    time.sleep(0.5)
    print("1.Raden Byrru Walidayn Ariyanto (15260979)")
    time.sleep(0.5)
    print("2.Javas Amran (15260999)")
    time.sleep(0.5)
    print("3.Harlin Ghatan Aldzikra (15260816)")
    time.sleep(0.5)
    print("4.Gilang Saputra (15260981)")
    time.sleep(0.5)
    print("5.Muhammad Pasha Prabasakti (15260786)")
    time.sleep(0.5)
    print_garis()
    pause()
