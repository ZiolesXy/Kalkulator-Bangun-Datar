from calculator.menu import menu_kalkulator
from utils.display import print_garis, print_judul, pause
from utils.validation import pilihan_menu
import time

def show_about():
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

def show_main_menu():
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
            show_about()
        elif pilihan == "0":
            print_judul("TERIMA KASIH")
            break
