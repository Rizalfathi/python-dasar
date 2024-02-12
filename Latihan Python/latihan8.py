keranjang_buah = ['nanas', 'apel', 'melon','anggur','paprika']
nama_buah = input('Masukkan nama buah dalam huruf kecil: ')

if (nama_buah in keranjang_buah):
  print(f'buah {nama_buah} yang anda cari tersedia!')
else:
  print(f'buah {nama_buah} yang anda cari tidak tersedia')