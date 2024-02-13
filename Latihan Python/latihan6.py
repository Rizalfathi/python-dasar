# nilai = 101

# print('Nilai anda adalah:',nilai)

# if nilai >= 80:
#   print('Selamat, anda lulus')
# if nilai > 100:
#   print('wutdaheeelll')
# if nilai < 60:
#   print('dongo amat nih anak')
# else:
#   print('Maaf anda tidak lulus 😁😁')


# nilai = int(input('Masukkan Nilai: '))

# if nilai >= 90:
#   print('Predikat A')
# if nilai >= 80:
#   print('Predikat b')
# if nilai >= 60:
#   print('Predikat C')
# if nilai >= 40:
#   print('Predikat D')
# else:
#   print('Predikat E')
#   print('Hanya Bisa Tersenyum 😅')


# nilai = int(input('Masukkan Nilai: '))

# if nilai >= 90:
#   print('Predikat A')
#   print('Kerja Baguss 👍👌')
# elif nilai >= 80:
#   print('Predikat b')
#   print('Lebih Ditingkatkan Lagi Anak Muda ✅')
# elif nilai >= 60:
#   print('Predikat C')
#   print('Sudah Diambang Kedunguan Inimah wir 🤏')
# elif nilai >= 40:
#   print('Predikat D')
#   print('Semangat, semangat ganti sekolah dek ☠')
# else:
#   print('Predikat E')
#   print('Hanya Bisa Tersenyum 😅')


keranjang_buah = ['nanas', 'apel', 'melon','anggur','paprika']
nama_buah = input('Masukkan nama buah dalam huruf kecil: ')

if (nama_buah in keranjang_buah):
  print(f'buah {nama_buah} yang anda cari tersedia!')
else:
  print(f'buah {nama_buah} yang anda cari tidak tersedia')