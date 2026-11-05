from calculator.menu import menu_kalkulator
from utils.display import print_garis, print_judul, pause
from utils.validation import pilihan_menu

def show_about():
    print_judul("TENTANG APLIKASI")
    
    print("Nama : Kalkulator Bangun Datar")
    pause()

def show_main_menu():
    while True:
        print_judul("Kalkulator Bangun Datar")

        print_garis()

        print("[1] Kalkulator Bangun Datar")
        print("[2] Quiz")
        print("[3] Tentang Aplikasi")
        print("[0] Keluar")

        valid = ("1", "3", "0")
        pilihan = pilihan_menu("Masukan Pilihan Anda: ", valid)

        if pilihan == "1":
            menu_kalkulator()
        elif pilihan == "3":
            show_about()
        elif pilihan == "0":
            print_judul("TERIMA KASIH")
            break
