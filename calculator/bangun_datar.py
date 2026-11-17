import math

def hitung_persegi(sisi):
    keliling = sisi * 4
    luas = sisi * sisi

    return keliling, luas

def hitung_persegi_panjang(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    luas = panjang * lebar

    return keliling, luas

def hitung_segitiga(alas, sisi2, sisi3, tinggi):
    if alas + sisi2 <= sisi3 or alas + sisi3 <= sisi2 or sisi2 + sisi3 <= alas:
        raise ValueError("Ketiga sisi tidak dapat membentuk segitiga")

    keliling = alas + sisi2 + sisi3
    luas = (alas * tinggi) / 2

    return keliling, luas

def hitung_lingkaran(jari_jari):
    diameter = 2 * jari_jari

    keliling = math.pi * diameter
    luas = math.pi * (jari_jari * jari_jari)

    return keliling, luas

def hitung_jajar_genjang(alas, sisi_miring, tinggi):
    keliling = 2 * (alas + sisi_miring)
    luas = alas * tinggi

    return keliling, luas

def hitung_trapesium(sisi1, sisi2, sisi3, sisi4, tinggi):
    keliling = sisi1 + sisi2 + sisi3 + sisi4
    luas = ((sisi1 + sisi2) * tinggi) / 2

    return keliling, luas

def hitung_belah_ketupat(diameter1, diameter2, sisi):
    keliling = 4 * sisi
    luas = (diameter1 * diameter2) / 2

    return keliling, luas