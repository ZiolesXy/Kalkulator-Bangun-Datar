def print_garis():
    print("=" * 58)

def print_judul(title):
    print()
    print_garis()
    print(title.center(58))
    print_garis()

def pause(message="Tekan ENTER untuk melanjutkan..."):
    input(message)