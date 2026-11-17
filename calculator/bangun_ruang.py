import math

def hitung_kubus(sisi):
  luas_permukaan = 6 * (sisi**2)
  volume = sisi**3

  return luas_permukaan, volume

def hitung_balok(panjang, lebar, tinggi):
  luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
  volume = panjang * lebar * tinggi

  return luas_permukaan, volume

def hitung_tabung(jari_jari, tinggi):
  luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
  volume = math.pi * (jari_jari**2) * tinggi

  return luas_permukaan, volume

def hitung_kerucut(jari_jari, tinggi):
  garis_pelukis = math.sqrt((jari_jari**2) + (tinggi**2))

  luas_permukaan = math.pi * jari_jari * (jari_jari + garis_pelukis)
  volume = (1 / 3) * math.pi * (jari_jari**2) * tinggi

  return luas_permukaan, volume

def hitung_bola(jari_jari):
  luas_permukaan = 4 * math.pi * (jari_jari**2)
  volume = (4 / 3) * math.pi * (jari_jari**3)
  
  return luas_permukaan, volume

def hitung_prisma_segitiga(alas_segitiga, tinggi_segitiga, sisi2, sisi3, tinggi_prisma):
  if (
      alas_segitiga + sisi2 <= sisi3
      or alas_segitiga + sisi3 <= sisi2
      or sisi2 + sisi3 <= alas_segitiga
  ):
    raise ValueError("Ketiga sisi alas tidak dapat membentuk segitiga")

  luas_alas = (alas_segitiga * tinggi_segitiga) / 2
  keliling_alas = alas_segitiga + sisi2 + sisi3

  luas_permukaan = (2 * luas_alas) + (keliling_alas * tinggi_prisma)
  volume = luas_alas * tinggi_prisma
  return luas_permukaan, volume

def hitung_limas_segitiga(sisi_alas, tinggi_limas):
  tinggi_alas = (math.sqrt(3) / 2) * sisi_alas
  luas_alas = (sisi_alas * tinggi_alas) / 2

  apotema_alas = tinggi_alas / 3
  
  tinggi_sisi_tegak = math.sqrt((apotema_alas**2) + (tinggi_limas**2))
  luas_selimut = 3 * ((sisi_alas * tinggi_sisi_tegak) / 2)

  luas_permukaan = luas_alas + luas_selimut
  volume = (1 / 3) * luas_alas * tinggi_limas

  return luas_permukaan, volume

def hitung_limas_segiempat(sisi_alas, tinggi_limas):
  tinggi_sisi_tegak = math.sqrt(((sisi_alas / 2) ** 2) + (tinggi_limas**2))
  luas_alas = sisi_alas**2
  luas_selimut = 4 * ((sisi_alas * tinggi_sisi_tegak) / 2)

  luas_permukaan = luas_alas + luas_selimut
  volume = (1 / 3) * luas_alas * tinggi_limas
  return luas_permukaan, volume