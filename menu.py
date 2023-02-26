from app_angka import angka, deret_angka
from app_pola import pola_bintang,sub_bintang
from app_luas import bangun_ruang,lingkaran,sub_bangunRuang
from app_karyawan import karyawan, biodata
from app_array import arrayy

print("")
print("## Program Giwi Super Menu ##")
print("=============================")
print("Silahkan pilih menu dibawah ini: ")
print("1. Membuat Pola Bintang")
print("2. Membuat Pola Angka")
print("3. Mencari Luas Bangun Ruang")
print("4. Perhitungan Gaji Karyawan")
print("5. List Daftar Nilai")
print("=============================")
pilihan = int(input("Pilihanmu (berdasarkan nomor): "))

print(f"*Home menu beralih ke menu pilihan {pilihan}")
if pilihan == 1:
    print("")
    print("## Program Bangun Ruang Berbentuk Bintang ##")
    print("============================================")
    print("Silahkan pilih menu dibawah ini: ")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga Siku Siku")
    print("4. Segitiga Terbalik")
    print("5. Piramida")
    print("6. Piramida Terbalik")
    print("7. Belah Ketupat")
    pilih = int(input("Masukan pilihan kamu (1-7): "))

    if pilih == 1:
        print("")
        print("## Persegi ##")
        print("==================")

        num_1 = int(input("Input besar persegi: "))
        result = pola_bintang(num_1)
        result.persegi_bintang()

    elif pilih == 2:
        print("")
        print("## Persegi Panjang ##")
        print("=====================")

        num_1 = int(input("Input tinggi persegi panjang: "))
        num_2 = int(input("Input lebar persegi panjang: "))
        result = sub_bintang(num_1,num_2)
        result.persegi_panjang()

    elif pilih == 3:
        print("")
        print("## Segitiga Siku-Siku ##")
        print("========================")

        num_1 = int(input("Input besar segitiga: "))
        result = pola_bintang(num_1)
        result.segitiga_bintang()

    elif pilih == 4:
        print("")
        print("## Segitiga Terbalik ##")
        print("=======================")

        num_1 = int(input("Input besar segitiga: "))
        result = pola_bintang(num_1)
        result.segitiga_tebalik()

    elif pilih == 5:
        print("")
        print("## Piramida ##")
        print("==============")

        num_1 = int(input("Input besar piramida: "))
        result = pola_bintang(num_1)
        result.piramida()

    elif pilih == 6:
        print("")
        print("## Piramida Tebalik ##")
        print("======================")

        num_1 = int(input("Input besar piramida: "))
        result = pola_bintang(num_1)
        result.piramida_tebalik()

    elif pilih == 7:
        print("")
        print("## Belah Ketupat ##")
        print("===================")

        num_1 = int(input("Input besar belah ketupat: "))
        result = pola_bintang(num_1)
        result.belah_ketupat()

    elif pilih == 2:
        print("")
        print("## Luas Persegi Panjang ##")
        print("==========================")

        input1 = int(input("Masukan panjang: "))
        input2 = int(input("Masukan lebar: "))
        persegi = bangun_ruang(input1,input2)
        persegi.luas_persegiPanjang()

    elif pilih == 3:
        print("")
        print("## Luas Segitiga ##")
        print("===================")

        input1 = int(input("Masukan alas: "))
        input2 = int(input("Masukan tinggi: "))
        segitiga = bangun_ruang(input1,input2)
        segitiga.luas_segitiga()

    elif pilih == 4:
        print("")
        print("## Luas Lingkaran ##")
        print("====================")

        input1 = int(input("Masukan jari-jari: "))
        lingkaran = lingkaran(input1)
        lingkaran.luas_lingkaran()

    elif pilih == 5:
        print("")
        print("## Luas Belah Ketupat  ##")
        print("=========================")

        input1 = int(input("Masukan panjang diagonal 1: "))
        input2 = int(input("Masukan panjang diagonal 2: "))
        belahKetupat = bangun_ruang(input1,input2)
        belahKetupat.belah_ketupat()

    elif pilih == 6:
        print("")
        print("## Luas Trapesium ##")
        print("====================")

        input1 = int(input("Masukan pangjang sisi sejajar atas: "))
        input2 = int(input("Masukan panjang sisi sejajar bawah: "))
        input3 = int(input("Masukan tinggi trapesium: "))
        trapesium = sub_bangunRuang(input1,input2,input3)
        trapesium.luas_trapesium()

    elif pilih == 7:
        print("")
        print("## Luas Permukaan Balok ##")
        print("==========================")

        input1 = int(input("Masukan panjang balok: "))
        input2 = int(input("Masukan lebar balok: "))
        input3 = int(input("Masukan tinggi balok: "))
        balok = sub_bangunRuang(input1,input2,input3)
        balok.luas_balok()

    else:
        print("Mohon input nomor yang benar!")

elif pilihan == 2:
    print("")
    print("## Program Pola Angka ##")
    print("========================")
    print("Silahkan pilih menu dibawah ini: ")
    print("1.  Persegi")
    print("2.  Persegi Deret")
    print("3.  Segitiga")
    print("4.  Segitiga Deret")
    print("5.  Segitiga Tebalik")
    print("6.  Deret perkalian 3")
    print("7.  Deret pangkat 2")
    print("8.  Deret Genap")
    print("9.  Deret Ganjil")
    print("10. Deret Genap Dengan Range ")
    print("11. Deret Ganjil Dengan Range")
    pilih = int(input("Masukan pilihan kamu (1-11): "))

    if pilih == 1:
        print("")
        print("## Persegi Angka ##")
        print("===================")

        num_1 = int(input("Input besar persegi: "))
        result = angka(num1)
        result.persegi()

    elif pilih == 2:
        print("")
        print("## Persegi Deret Angka ##")
        print("=========================")

        num_1 =  int(input("Input besar persegi: "))
        result = angka(num_1)
        result.persegi_deret()
    
    elif pilih == 3:
        print("")
        print("## Segitiga Angka ##")
        print("====================")

        num_1 =  int(input("Input besar segitiga: "))
        result = angka(num_1)
        result.segitiga_angka()
    
    elif pilih == 4:
        print("")
        print("## Segitiga Deret Angka ##")
        print("==========================")

        num_1 =  int(input("Input besar segitiga: "))
        result = angka(num_1)
        result.segitiga_deret()
    
    elif pilih == 5:
        print("")
        print("## Segitiga Angka Tebalik ##")
        print("============================")

        num_1 =  int(input("Input besar persegi: "))
        result = angka(num_1)
        result.segitiga_tebalik()
    
    elif pilih == 6:
        print("")
        print("## Deret Perkalian 3 ##")
        print("=======================")

        num_1 =  int(input("Input jumlah deret yang diinginkan: "))
        result = angka(num_1)
        result.deret_A()
    
    elif pilih == 7:
        print("")
        print("## Deret Pangkat 2 ##")
        print("=====================")

        num_1 =  int(input("Input jumlah deret yang diinginkan: "))
        result = angka(num_1)
        result.deret_B()
    
    elif pilih == 8:
        print("")
        print("## Deret Genap ##")
        print("=========================")

        num_1 =  int(input("Input jumlah deret: "))
        result = angka(num_1)
        result.deret_genap()
    
    elif pilih == 9:
        print("")
        print("## Deret Ganjil ##")
        print("=========================")

        num_1 =  int(input("Input jumlah deret: "))
        result = angka(num_1)
        result.deret_ganjil()
    
    elif pilih == 10:
        print("")
        print("## Deret Genap Dengan Range ##")
        print("=========================")

        num_1 =  int(input("Input angka awal: "))
        num_2 =  int(input("Input angka akhir: "))
        result = deret_angka(num_1,num_2)
        result.deret_genap_withRange()
    
    elif pilih == 11:
        print("")
        print("## Deret Ganjil Dengan Range ##")
        print("=========================")

        num_1 =  int(input("Input angka awal: "))
        num_2 =  int(input("Input angka akhir: "))
        result = deret_angka(num_1,num_2)
        result.deret_ganjil_withRange()
    
    else:
        print("Mohon input pilihan menu yang benar")

elif pilihan == 3:

    print("")
    print("## Program Hitung Luas Bangun Ruang ##")
    print("======================================")
    print("Silahkan pilih menu dibawah ini: ")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Belah Ketupat")
    print("6. Trapesium")
    print("7. Permukaan Balok")
    print("=====================")
    pilihan = int(input("pilihanmu (berdasarkan nomor): "))

    if pilihan == 1:
        print("")
        print("## Luas Persegi ##")
        print("==================")

        input1 = int(input("Masukan sisi 1 persegi: "))
        input2 = int(input("Masukan sisi 2 persegi: "))
        persegi = bangun_ruang(input1,input2)
        persegi.persegi()

    elif pilihan == 2:
        print("")
        print("## Luas Persegi Panjang ##")
        print("==========================")

        input1 = int(input("Masukan panjang: "))
        input2 = int(input("Masukan lebar: "))
        persegi = bangun_ruang(input1,input2)
        persegi.luas_persegiPanjang()

    elif pilihan == 3:
        print("")
        print("## Luas Segitiga ##")
        print("===================")

        input1 = int(input("Masukan alas: "))
        input2 = int(input("Masukan tinggi: "))
        segitiga = bangun_ruang(input1,input2)
        segitiga.luas_segitiga()

    elif pilihan == 4:
        print("")
        print("## Luas Lingkaran ##")
        print("====================")

        input1 = int(input("Masukan jari-jari: "))
        lingkaran = lingkaran(input1)
        lingkaran.luas_lingkaran()

    elif pilihan == 5:
        print("")
        print("## Luas Belah Ketupat  ##")
        print("=========================")

        input1 = int(input("Masukan panjang diagonal 1: "))
        input2 = int(input("Masukan panjang diagonal 2: "))
        belahKetupat = bangun_ruang(input1,input2)
        belahKetupat.belah_ketupat()

    elif pilihan == 6:
        print("")
        print("## Luas Trapesium ##")
        print("====================")

        input1 = int(input("Masukan pangjang sisi sejajar atas: "))
        input2 = int(input("Masukan panjang sisi sejajar bawah: "))
        input3 = int(input("Masukan tinggi trapesium: "))
        trapesium = sub_bangunRuang(input1,input2,input3)
        trapesium.luas_trapesium()

    elif pilihan == 7:
        print("")
        print("## Luas Permukaan Balok ##")
        print("==========================")

        input1 = int(input("Masukan panjang balok: "))
        input2 = int(input("Masukan lebar balok: "))
        input3 = int(input("Masukan tinggi balok: "))
        balok = sub_bangunRuang(input1,input2,input3)
        balok.luas_balok()

    else:
        print("Mohon input nomor yang benar!")
        
elif pilihan == 4:
    print("")
    print("## Program Perhitungan Gaji Karyawan ##")
    print("=======================================")
    print("Silahkan pilih menu dibawah ini: ")
    print("1. Gaji")
    print("2. Menampilkan Biodata Karyawan")
    pilihan = int(input("pilihanmu (berdasarkan nomor): "))
    print("")

    if pilihan == 1:
        print("")
        print("## Perhitungan Gaji Karyawan ##")
        print("===============================")

        nama = input("Nama: ")
        golongan = input("Golongan: ")
        jam_kerja = int(input("Jam Kerja: "))

        result = karyawan(nama,golongan,jam_kerja)
        result.gaji()
    
    elif pilihan == 2:
        print("")
        print("## Pengisian Biodata Karyawan ##")
        print("===============================")

        nama = input("Nama: ")
        golongan = input("Golongan: ")
        jam_kerja = int(input("Jam Kerja: "))
        divisi = input("Divisi: ")
        kota_asal = input("Kota Asal: ")
        alamat = input("Alamat: ")

        result = biodata(nama,golongan,jam_kerja,divisi,kota_asal,alamat)
        result.data()

elif pilihan == 5:

    print("")
    print("## Program List Daftar Nilai ##")
    print("===============================")
    print("Silahkan pilih menu dibawah ini: ")
    print("1. Mencari Nilai Terbesar ")
    print("2. Mencari Nilai Terkecil ")
    print("3. Penjumlahan Array ")
    print("4. Mencari Nilai Rata-Rata ")
    print("5. Mecari Data Dalam List ")
    pilihan = int(input("pilihanmu (berdasarkan nomor): "))
    print("")

    if pilihan == 1:
        print("")
        print("## Mencari Nilai Tersebesar Dalam List ##")
        print("=========================================")

        num_1 = int(input("Input jumlah element list: "))
        result = arrayy(num_1)
        result.find_max()
    
    elif pilihan == 2:
        print("")
        print("## Mencari Nilai Terkecil Dalam List ##")
        print("=========================================")

        num_1 = int(input("Input jumlah element list: "))
        result = arrayy(num_1)
        result.find_min()
    
    elif pilihan == 3:
        print("")
        print("## Penjumlahan Dalam List/Array ##")
        print("==================================")

        num_1 = int(input("Input jumlah element list: "))
        result = arrayy(num_1)
        result.find_sum()

    elif pilihan == 4:
        print("")
        print("## Mencari Nilai Rata-Rata Dalam List ##")
        print("========================================")

        num_1 = int(input("Input jumlah element list: "))
        result = arrayy(num_1)
        result.find_avg()

    elif pilihan == 5:
        print("")
        print("## Mencari Data Dalam List ##")
        print("=========================================")

        num_1 = int(input("Input jumlah element list: "))
        result = arrayy(num_1)
        result.find_array() 

else:
    print("Pilih nomor menu yang benar")
    


    



