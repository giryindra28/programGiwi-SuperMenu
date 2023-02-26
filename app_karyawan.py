
class karyawan():
    def __init__ (self,nama,golongan,jam_kerja):
        self.nama = nama
        self.golongan = golongan
        self.jam_kerja = jam_kerja
    
    def gaji(self):
        uang_lembur = (self.jam_kerja-48)*4000
        if self.golongan == 'A' or self.golongan == 'a':
            upah = 5000
        elif self.golongan == 'B' or self.golongan == 'b':
            upah = 7000
        elif self.golongan == 'C' or self.golongan == 'c':
            upah = 8000
        elif self.golongan == 'D' or self.golongan == 'd':
            upah = 10000
        
        total_gaji = upah * self.jam_kerja

        if self.jam_kerja > 48:
            total_gaji = total_gaji + uang_lembur
        print(f"{self.nama} menerima upah Rp. {total_gaji} per minggu")

class biodata(karyawan):
    def __init__ (self,nama,golongan,jam_kerja,divisi,kota_asal, alamat):
        karyawan.__init__ (self,nama,golongan,jam_kerja)
        self.divisi = divisi
        self.kota_asal = kota_asal
        self.alamat = alamat
    
    def data(self):
        print("")
        print("## Biodata sukses terisi ##")
        print("===========================")
        print(f"Nama: {self.nama}")
        print(f"Golongan: {self.golongan}")
        print(f"Jam kerja: {self.jam_kerja}")
        print(f"Divisi: {self.divisi}")
        print(f"Kota Asal: {self.kota_asal}")
        print(f"Alamat: {self.alamat}")
      

