import time
menu = {
    1: 'Input Angka',
    2: 'Tampil Hasil Pengurutan',
    3: 'Selesai',
}
data = []

def printMenu():
    for i in menu.keys():
        print (i, '.', menu[i] )

# input
def inputAngka():
     print('Masukkan jumlah angka yang akan diinput:3')
     print('Input angka secara acak')
     print("-----------------------------------------")
     data.append(int(input("Angka 1 : ")))
     data.append(int(input("Angka 2 : ")))
     data.append(int(input("Angka 3 : ")))
     angkaUrut = sorted(data)
     print('Nilai Tugas :',*angkaUrut)
     time.sleep(3)
     print('\n')

# output
def tampilHasil():
     if len(data) == 0:
          print('Data belum tersedia')
          time.sleep(3)
          print('\n')
     else:
          angkaUrut = sorted(data)
          print('---------------------------')
          print('Tampil Hasil Pengurutan')
          print('Nilai Tugas : ', *angkaUrut)
          print('\n')
          time.sleep(3)
          

if __name__=='__main__':
     while(True):
          printMenu()
          options = ''
          try:
               options = int(input('Masukkan Pilihan [1/2/3]'))       
          except:
               print('input angka 1-3')
          if options == 1:
               inputAngka()
          elif options == 2:
               tampilHasil()
          elif options == 3:
               print('Terima Kasih')
               exit()
          else:
               print('Pilihan tidak sesuai!')
               