def new_func():
    try:
        angka1 = float(input('Masukkan Angka Pertama: '))
        angka2 = float(input('Masukkan Angka Kedua: '))
    except ValueError:
        print("Ini Kalkulator Bjir Bukan Catatan")
        return

    hasil = angka1 + angka2
    print('Hasil Penjumlahan: ', hasil)

    hasil = angka1 - angka2
    print('Hasil Pengurangan: ', hasil)

    hasil = angka1 * angka2
    print('Hasil Perkalian: ', hasil)

    if angka2 != 0:
        hasil = angka1 / angka2
        print('Hasil Pembagian: ', hasil)
    else:
        print('Tidak Bisa Dibagi Nol')

new_func()
