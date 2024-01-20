import datetime
import time

menu_options = {
    1: 'Jabatan',
    2: 'Selesai',
}


def print_menu():
    for key in menu_options.keys():
        print (key, '.', menu_options[key] )

class Pegawai:
     namaPerusahaan = "PT.Argo Industri"
     def __init__(self,nip,nama,tahunMasuk,gajiPokok):
          self.nip = nip
          self.nama = nama
          self.tahunMasuk = tahunMasuk
          self.gajiPokok = gajiPokok

class Satpam(Pegawai):
     def __init__(self, nip, nama, tahunMasuk, gajiPokok):
          super().__init__(nip, nama, tahunMasuk, gajiPokok)
     def lembur(self):
          totalLembur = int(input('Masukkkan Jumlah Lembur: '))
          self.__honorLembur = totalLembur * 20000
          self.gajiAkhir = self.__honorLembur + self.gajiPokok
          return self.gajiAkhir
     
class Sales(Pegawai):
     def __init__(self, nip, nama, tahunMasuk, gajiPokok):
          super().__init__(nip, nama, tahunMasuk, gajiPokok)
     def komisi(self):
          totalKomisi = int(input('Masukkkan Jumlah Pelanggan: '))
          self.honorKomisi = totalKomisi * 50000
          self.gajiAkhir = self.honorKomisi + self.gajiPokok
          return self.gajiAkhir
     
class Administrasi(Pegawai):
     def __init__(self, nip, nama, tahunMasuk, gajiPokok):
          super().__init__(nip, nama, tahunMasuk, gajiPokok)
     def tunjangan(self):
          x = datetime.datetime.now() 
          b = x.year - self.tahunMasuk
          if b >= 5:
               self.honorTunjangan = (self.gajiPokok*3)/100
               self.gajiAkhir = self.honorTunjangan + self.gajiPokok
               return self.gajiAkhir
          elif b >=3:
               self.honorTunjangan = (self.gajiPokok*1)/100
               self.gajiAkhir = self.honorTunjangan + self.gajiPokok
               return self.gajiAkhir
          elif b < 3:
               self.gajiAkhir = self.gajiPokok
               return self.gajiAkhir
          

class Manajer(Pegawai):
     def __init__(self, nip, nama, tahunMasuk, gajiPokok):
          super().__init__(nip, nama, tahunMasuk, gajiPokok)
     def tunjangan(self):
          penjualanBefore = int(input('Masukkan Total Pendapatan Penjualan tahun Lalu : '))
          penjualanAfter = int(input('Masukkan Total Pendapatan Penjualan tahun sekarang : '))
          selisih = penjualanAfter - penjualanBefore
          rasio = (selisih /penjualanBefore)*100
          if rasio >= 10:
               self.bonus = (self.gajiPokok*10)/100
               self.gajiAkhir = self.bonus + self.gajiPokok
               return self.gajiAkhir
          
          elif rasio >= 6 and rasio <= 10 :
               self.bonus = (self.gajiPokok*5)/100
               self.gajiAkhir = self.bonus + self.gajiPokok
               return self.gajiAkhir
          
          elif rasio >= 1 and rasio <= 5 :
               self.bonus = (self.gajiPokok*2)/100
               self.gajiAkhir = self.bonus + self.gajiPokok
               return self.gajiAkhir
          
          else:
               self.gajiAkhir = self.gajiPokok
               return self.gajiAkhir   

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Masukkan pilihan [1/2] : '))
        except:
            print('Hanya boleh menginput angka 1-3.')
        if option == 1:
             print("Pilih Jabatan Anda")
             print("1. Satpam")
             print("2. Sales")
             print("3. Administrasi")
             print("4. Manajer")
             print('-------------------------')
             jabatan = int(input('Masukkan Pilihan [1/2/3/4]'))
             nip = input("Masukkan NIP: ")
             nama = input("Masukkan Nama: ")
             tahunMasuk = int(input("Masukkan Tahun Masuk: "))
             gajiPokok = int(input("Masukkan Gaji Pokok : "))
             if jabatan == 1:
                  data = Satpam(nip,nama,tahunMasuk,gajiPokok)
                  print('\n')
                  time.sleep(2)
                  print(f' ===== {data.namaPerusahaan} ===== \n Nama       : {data.nama} \n Total Gaji : Rp.{data.lembur():,.2f}'.replace('Rp.-','-Rp.'))
                  print('------------------------------')

             elif jabatan == 2:
                  data = Sales(nip,nama,tahunMasuk,gajiPokok)
                  print('\n')
                  time.sleep(2)
                  print(f' ===== {data.namaPerusahaan} ===== \n Nama       : {data.nama} \n Total Gaji : Rp.{data.komisi():,.2f}'.replace('Rp.-','-Rp.'))
                  print('------------------------------')

               
             elif jabatan == 3:
                  data = Administrasi(nip,nama,tahunMasuk,gajiPokok)
                  print('\n')
                  time.sleep(2)
                  print(f' ===== {data.namaPerusahaan} ===== \n Nama       : {data.nama} \n Total Gaji : Rp.{data.tunjangan():,.2f}'.replace('Rp.-','-Rp.'))
                  print('------------------------------')
          
             elif jabatan == 4:
                  data = Manajer(nip,nama,tahunMasuk,gajiPokok)
                  print('\n')
                  time.sleep(2)
                  print(f' ===== {data.namaPerusahaan} ===== \n Nama       : {data.nama} \n Total Gaji : Rp.{data.tunjangan():,.2f}'.replace('Rp.-','-Rp.'))
                  print('------------------------------')
        elif option == 2:
            print('Terima kasih')
            exit()
        else:
            print('Pilihan tidak sesuai. Silahkan pilih 1-3.')
          
          