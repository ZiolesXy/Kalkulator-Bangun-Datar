import math
from utils.display import pause

def pilihan_menu(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()

        if choice in valid_choices:
            return choice

        print("Pilihan tidak valid. Silakan coba lagi.")
        pause()


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


def cek_angka_positif(prompt):
    while True:
        value = cek_angka(prompt)

        if value > 0:
            return value

        print("Nilai harus lebih besar dari 0.")


def cek_angka_negatif(prompt):
    while True:
        nilai = cek_angka(prompt)

        if nilai >= 0:
            return nilai

        print("Nilai tidak boleh negatif.")


def cek_bilangan_asli(prompt):
    while True:
        try:
            nilai = int(input(prompt).strip())

            if nilai > 0:
                return nilai

            print("Jumlah harus lebih besar dari 0.")

        except ValueError:
            print("Masukkan bilangan bulat positif.")
