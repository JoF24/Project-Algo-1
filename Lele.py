import os #Mengimport module os
import datetime as dt #mengimport module datetime dan menginisiasikan menjadi dt
from prettytable import PrettyTable as pt 
import json #Mengimport module json
import time
from tqdm import tqdm

x = dt.datetime.now () #Variabel untuk menyimpan waktu saat ini
tanggal = int(x.strftime('%d')) #Variabel untuk menyimpan tanggal saat ini
bulan = int(x.strftime('%m')) #Variabel untuk menyimpan bulan saat ini
tahun = int(x.strftime('%Y')) #Variabel untuk menyimpan tahun saat ini

def loading() : #Fungsi fitur loading
  for i in tqdm(range(100)):  # Buat progress bar dengan jumlah 100
    time.sleep(0.01) 

def tahan(): #Fungsi untuk fitur tahan
    a = input("Tekan Enter Untuk Melanjutkan") #Input untuk menekan tombol enter jika ingin lanjut

def judul () : #Membuat fungsi untuk judul
    print ('=' * 43) #Mencetak '=' sebanyak 43 kali
    print ('|          Selamat Datang Di CFS          |') #Mencetak tulisan untuk header
    print ('=' * 43) #Mencetak '=' sebanyak 43 kali

def bersih () : #Membuat fungsi untuk membersihkan terminal
    os.system('cls') #Perintah untuk membersihkan terminal

def keluar1 (): #Fungsi untuk keluar dari program
    bersih() #Memanggil fungsi untuk membersihkan terminal
    print ('='*44) #Mencetak '=' sebanyak 44 kali
    print ('|Terimakasih Telah Menggunakan Program Kami|') #Mencetak string terimakasih
    print ('='*44) #Mencetak '=' sebanyak 44 kali
    exit () #Perintah keluar dari program

def homepage () : #Fungsi untuk halaman utama
    bersih () #Memanggil fungsi untuk membersihkan terminal
    judul () #Memanggil fungsi untuk menampilkan judul
    print ("HALAMAN UTAMA") #Mencetak string judul halaman utama
    print (f'Tanggal Saat Ini : {tanggal} - {bulan} - {tahun}') #Mencetak tanggal saat ini 
    fitur = ('Menu :', '1. Makan Lele', '2. Pergantian Air', '3. Keluar') #Variabel yang menyimpan pilihan menu
    for i in fitur : #Perulangan untuk mencetak fitur yang disimpan, agar fitur tercetak kebawah
        print (i) #Perintah mencetak perulangan
    print ('='*43) #Mencetak '=' sebanyak 43 kali
    pilih = input ('Masukkan pilihan anda :') #Variabel untuk menyimpak input
    if pilih == '1' : #Percabangan jika memilih '1'
        fiturpakan() #Memanggil fungsi fiturpakan
    elif pilih == '2' : #Percabangan jika memilih '2'
        fiturair() #Memanggil fungsi fiturair
    elif pilih == '3' : #Percabangan jika memilih '3'
        keluar1 () #Memanggil fungsi keluar1
    else : #Percabangan jika memilih pilihan yang tidak disediakan
        bersih() #Memanggil fungsi bersih
        judul () #Memanggil fungsi judul
        print ('Halaman Tidak Ditemukan!!!') #Mencetak kata dalam string
        pilihan = '1. Kembali','2. Keluar' #Variabel menyimpan pilihan menu
        for i in pilihan : #Perulangan untuk mencetak kebawah string yang terdapat di variabel 'pilihan'
            print (i) #Mecetak perulangan yang telah dibuat
        print ('='*43) #Mencetak '=' sebanyak 43 kali
        def ulang (): #Fungsi untuk mengulang
            putusan = input ('Masukkan pilihan anda :') #Veriabel untuk menyimpan input yang telah dimasukkan
            if putusan == '1' : #Percabangan jika memilih 1
                homepage () #Memanggil fungsi 'homepage'
            elif putusan == '2' : #Percabangan jika memilih 2
                keluar1 () #Memanggil fungsi 'keluar1'
            else : #Percabangan jika memasukkan selain pilihan yang disediakan
                ulang () #Memanggil fungsi 'ulang'
        ulang () #Memanggil fungsi 'ulang'
        
def fiturpakan() : #Fungsi untuk fitur pakan lele
    database = [] #Variabel untuk menyimpan data list
    server = 'C:/Code/Project Algo/Project Algo1/database pakan.json' #Variabel untuk menyimpan lokasi penyimpanan file database
    def membaca(data=server,listJson=database): #Fungsi untuk membaca file json 
        with open(data,'r') as file:  # Membuka file json
            reader = json.load(file) # Mengambil data dari file json
            for i in reader: #Perulangan untuk mencetak seluruh isi dari file json
                listJson.append(i) #Menambahkan isi file json ke dalam list kosong yang telah disediakan

    def tulis(data=server,listJson=database): #Fungsi untuk menulis ulang isi dari file json
        with open(data,'w') as file:  #Membuka file jsom
            json.dump(listJson,file,indent=4) #Menulis ulang file json dengan isi yang baru adalah isi dari list yang disediakan

    def tampilkandatapakan(): #Fungsi untuk menampilkan data pakan dari list yang disediakan
        x = pt() #Variabel untuk menyimpan prrettytable
        for i in range(len(database)): #Perulangan untuk mencetak isi dari list dengan range sesuai panjang dari list
            list_data_index = database[i] 
            for i in range(len(list_data_index)-1):
                x.add_column(list_data_index["hari"], list_data_index["jam"])

        print(x) 
    
    def Mengubah(): #Fungsi untuk mengubah jadwal
        print(
            "Mana yang Ingin dirubah jamnya?\n"
            "[1]. Senin\n"
            "[2]. Selasa\n"
            "[3]. Rabu\n"
            "[4]. Kamis\n"
            "[5]. Jumat\n"
            "[6]. Sabtu\n"
            "[7]. Minggu\n"
        ) #Perintah untuk mencetak kalimat yang terdapat di dalam string
        pilih = int(input("Masukkan Pilihan Anda: ")) #Variabel untuk menyimpan pilihan yang dimasukkan
        a = database[pilih-1] #Variabel untuk menyimpan indeks berdasarkan yang dimasukkan
        b = a["jam"] #Variabel untuk menyimpan akses ke dictionary yang terdapat di dalam list
        n = 0 #
        bersih() #Memanggil fungsi bersih
        judul_pakanlele() #Memanggil fungsi judul halaman
        tampilkandatapakan() #Memanggil fungsi untuk menampilkan data
        print('Pilih Jam Yang Ingin Dirubah') #Mencetak tulisan di dalam string
        for i in b: #Perulangan untuk 
            n+=1
            print("[{}]".format(n), i) 

        j = int(input("Masukkan Pilihan Anda: "))
        bersih() #Memanggil fungsi bersih
        judul_pakanlele() #Memanggil fungsi judul halaman
        tampilkandatapakan() #Memanggil fungsi menampilkan data
        b[j-1] = input("Masukkan Jam Dengan format (__:__)(Kolam) : ") #
        bersih() #Memanggil fungsi bersih
        loading() #Memanggil fungsi loading
        print("Data Sudah Dirubah!!!") #Mencetak kalimat di dalam string
        tahan() #Memanggil fungsi tahan
        tulis() #Memanggil fungsi tulis
        
    def hapusdata_jam(): #Fungsi untuk hapus data
        print(
            "Hari Apa Yang Ingin Dihapus Jamnya?\n"
            "[1]. Senin\n"
            "[2]. Selasa\n"
            "[3]. Rabu\n"
            "[4]. Kamis\n"
            "[5]. Jumat\n"
            "[6]. Sabtu\n"
            "[7]. Minggu\n"
        )
        pilih = int(input("Masukkan Pilihan Anda: "))
        a = database[pilih-1]
        b = a["jam"]
        n = 0
        bersih()
        judul_pakanlele()
        tampilkandatapakan()
        print('Pilih Jam Yang Ingin Dihapus')
        for i in b:
            n+=1
            print("[{}]".format(n), i)

        j = int(input("Masukkan Pilihan Anda: "))
        b[j-1] = "  "
        bersih()
        loading()
        print("Data Sudah Dihapus!!!")
        tahan()
        tulis()

    def judul_pakanlele ():
        print ('='*67)
        print ((' '*23)+("Jadwal Pakan Lele Seminggu"))
        print ('='*67)
    
    def keluar2 (): #Fungsi untuk keluar dari program
        tulis() #Memanggil fungsi tulis
        bersih() #Memanggil fungsi untuk membersihkan terminal
        print ('='*44) #Mencetak '=' sebanyak 44 kali
        print ('|Terimakasih Telah Menggunakan Program Kami|') #Mencetak string terimakasih
        print ('='*44) #Mencetak '=' sebanyak 44 kali
        exit () #Perintah keluar dari program
    
    def makanlele ():
        bersih()
        judul()
        print ("HALAMAN MAKAN LELE")
        print ('Menu :')
        lanjutan = ('1. Mengubah Jadwal Pemberian Pakan', '2. Melihat Jadwal Pemberian Pakan', '3. Menghapus Jam Pemberian Pakan', '4. Kembali ke Halaman Utama')
        for i in lanjutan :
            print (i)
        print ('='*43)
        keputusan = input ("Masukkan Menu Pilihan :")
        if keputusan == '1' :
            def lanjutan_1 ():
                bersih()
                judul_pakanlele()
                tampilkandatapakan()
                kembali = input ('Apakah Anda Ingin Kembali? [y/n]:')
                if kembali.lower() == 'y':
                    makanlele()
                elif kembali.lower() == 'n':
                    tulis()
                    homepage()
                else :
                    lanjutan_1()
            def ubah_lagi ():
                bersih()
                judul_pakanlele()
                tampilkandatapakan()
                def konfirmasi_ulang () :
                    konfirmasi = input('Apakah Ingin Mengubah Jam Lagi? [y/n]:')
                    if konfirmasi.lower() == 'y' :
                        bersih()
                        judul_pakanlele()
                        tampilkandatapakan()
                        Mengubah()
                        ubah_lagi()
                    elif konfirmasi.lower() == 'n' :
                        lanjutan_1()
                    else :
                        konfirmasi_ulang()
                konfirmasi_ulang()
            bersih()
            judul_pakanlele()
            tampilkandatapakan()
            Mengubah()
            ubah_lagi()
        elif keputusan == '2' :
            def lanjutan_2 () :
                putusan = input ('Apakah Ingin Kembali? [y/n] :')
                if putusan.lower() == 'y':
                    makanlele()
                elif putusan.lower() == 'n' :
                    tulis()
                    homepage()
                else :
                    lanjutan_2()
            bersih()
            judul_pakanlele()
            tampilkandatapakan()
            lanjutan_2()
        elif keputusan == '3' :
            def hapus () :
                hapusdata_jam()
                def lnjt ():
                    bersih()
                    judul_pakanlele()
                    tampilkandatapakan()
                    konfirm = input('Apakah Ingin Menghapus Jam Lagi? [y/n]: ')
                    if konfirm.lower() == 'y' :
                        bersih()
                        judul_pakanlele()
                        tampilkandatapakan()
                        hapus()
                    elif konfirm.lower() == 'n' :
                        lanjutan_3()
                    else :
                        lnjt()
                lnjt()
            def lanjutan_3():
                bersih()
                judul_pakanlele()
                tampilkandatapakan()
                putusan = input ('Apakah Ingin Kembali? [y/n] :')
                if putusan.lower() == 'y':
                    makanlele()
                elif putusan.lower() == 'n' :
                    tulis()
                    homepage()
                else :
                    lanjutan_3()
            bersih()
            judul_pakanlele()
            tampilkandatapakan()
            hapus()
        elif keputusan == '4' :
            homepage()
        else :
            bersih() #Memanggil fungsi bersih
            judul_pakanlele() #Memanggil fungsi judul
            print ('Halaman Tidak Ditemukan!!!') #Mencetak kata dalam string
            pilihan = ('1. Kembali','2. Keluar') #Variabel menyimpan pilihan menu
            for i in pilihan : 
                print (i)
            print ('='*43)
            def ulang ():
                putusan = input ('Masukkan pilihan anda :')
                if putusan == '1' :
                    makanlele() ()
                elif putusan == '2' :
                    keluar2()
                else :
                    ulang ()
            ulang ()
    membaca()
    makanlele()

def fiturair () :
    server = 'C:/Code/Project Algo/Project Algo1/database kolam.json'
    wadah = []

    def baca(data=server,listJson=wadah): # Fungsi untuk membaca file json
        with open(data,'r') as file:  # Membuka file json
            reader = json.load(file) 
            for i in reader:
                listJson.append(i)
    
    def tampilkandataair():
        x = pt( )
        for i in range(len(wadah)):
            list_data_index = wadah[i]
            for i in range(len(list_data_index)-1):
                x.add_column(list_data_index["Kolam"], list_data_index["Hari"])

        print(x)

    def tulis(data=server,listJson=wadah):
        with open(data,'w') as file: 
            json.dump(listJson,file,indent=4)

    def rubahwaktu():
        tampilkandataair()
        tanggal = int(x.strftime('%d'))
        bulan = int(x.strftime('%m'))
        tahun = int(x.strftime('%Y'))
        print(
            "Mana Yang Ingin Dirubah Jamnya?\n"
            "[1]. Kolam 1\n"
            "[2]. Kolam 2\n"
            "[3]. Kolam 3\n"
            "[4]. Kolam 4\n"
            "[5]. Kolam 5\n"
        )
        pilih = int(input("Masukkan Pilihan Anda: "))

        a = wadah[pilih-1]
        b = a["Hari"]
        n = 0
        bersih()
        judul_gantiair()
        tampilkandataair()
        print('Pilih Tanggal Yang Ingin Dirubah:')
        for i in b:
            n+=1
            print("[{}]".format(n), i)

        j = int(input("Masukkan Pilihan Anda: "))
        print (f'Tanggal Saat Ini : {tanggal} - {bulan} - {tahun}')
        b[j-1] = input("Masukkan Tanggal - Bulan -Tahun : ")
        bersih()
        loading()
        print("Tanggal Berhasil Dirubah!!!")
        tahan()
        tulis()
    
    def tambahkolam():
        bersih()
        judul_gantiair()
        tampilkandataair()
        dict_dasar = {
            "Kolam": "Kolam 1",
            "Hari": [
                "  ",
                "  ",
                "  "
            ]
        }

        tambah = input("Masukkan Nama Kolam (Kolam (_)): ")
        tambah_kolam = []
        for i in range(3):
            a = "  "
            tambah_kolam.append(a)
        dict_dasar["Kolam"] = tambah
        dict_dasar["Hari"] = tambah_kolam
        wadah.append(dict_dasar)
        tulis()
        bersih()
        loading()
        print("Kolam Sudah Ditambahkan!!!")
        tahan()

    def hapus_tanggal ():
        bersih()
        judul_gantiair()
        tampilkandataair()
        print('Kolam Nomor Berapa Yang Ingin Dihapus Tanggalnya?')
        print('(Ket : Nomor 1 Dimulai Dari Kiri)')
        pilih = int(input("Masukkan Pilihan Anda: "))
        a = wadah[pilih-1]
        b = a["Hari"]
        n = 0
        print('Pilih Tanggal Yang Ingin Dihapus')
        for i in b:
            n+=1
            print("[{}]".format(n), i)

        j = int(input("Masukkan Pilihan Anda: "))
        b[j-1] = "  "
        bersih()
        loading()
        print("Tanggal Berhasil Dihapus!!!")
        tahan()
        tulis()
    
    def hapus_kolam():
        bersih()
        judul_gantiair()
        tampilkandataair()
        print ("Kolam Berapa Yang Ingin Dihapus?")
        print('Ket : Nomor 1 Dimulai Dari Kiri')
        a = int (input ("Masukkan Pilihan Anda : "))
        wadah.pop (a-1)
        bersih()
        loading()
        print('Kolam Berhasil Dihapus!!!')
        tahan()
    
    def judul_gantiair ():
        print ('='*67)
        print ((' '*23)+("Jadwal Mengganti Air Kolam"))
        print ('='*67)
    
    def keluar3(): #Fungsi untuk keluar dari program
        tulis () #Memanggil fungsi 'tulis'
        bersih () #Memanggil fungsi 'bersih'
        print (('='*44)) #Mencetak '=' sebanyak 44 kali
        print (('|Terimakasih Telah Menggunakan Program Kami|')) #Mencetak kalimat yang terdapat di dalam string
        print (('='*44)) #Mencetak '=' sebanyak 44 kali
        exit () #Perintah keluar dari program
    
    def gantiair ():
        bersih()
        judul()
        print ("HALAMAN MENGGANTI AIR KOLAM")
        print ('Menu :')
        lanjutan = ('1. Mengubah Jadwal Penggantian Air', '2. Melihat Jadwal Penggantian Air', '3. Menghapus Jadwal', '4. Menambahkan Kolam', '5. Kembali ke Halaman Utama')
        for i in lanjutan :
            print (i)
        print ('='*43)
        keputusan = input ("Masukkan Menu Pilihan :")
        if keputusan == '1' :
            def ulang ():
                def ulang_lagi ():
                    putusan = input('Apakah Ingin Mengubah Tanggal Lagi? [y/n]:')
                    if putusan.lower() == 'y' :
                        bersih()
                        judul_gantiair()
                        rubahwaktu()
                        ulang()
                    elif putusan.lower() == 'n' :
                        lanjutan_1()
                    else :
                        ulang_lagi()
                bersih()
                judul_gantiair()
                tampilkandataair()
                ulang_lagi()
                
            def lanjutan_1 () :
                bersih()
                judul_gantiair()
                tampilkandataair()
                kembali = input("Apakah Anda Ingin Kembali? [y/n]:")
                if kembali.lower() == 'y':
                    gantiair ()
                elif kembali.lower() == 'n':
                    tulis()
                    homepage()
                else :
                    lanjutan_1()
            bersih()
            judul_gantiair ()
            rubahwaktu ()
            ulang()  
        elif keputusan == '2' :
            def lanjutan_2 () :
                putusan = input ('Apakah Ingin Kembali? [y/n] :')
                if putusan.lower() == 'y':
                    gantiair ()
                elif putusan.lower() == 'n' :
                    tulis()
                    homepage()
                else :
                    lanjutan_2 ()
            bersih()
            judul_gantiair ()
            tampilkandataair()
            lanjutan_2 ()
        elif keputusan == '3' :
            def lanjutan_3 ():
                bersih()
                judul_gantiair()
                tampilkandataair()
                putusan = input ('Apakah Ingin Kembali? [y/n] :')
                if putusan.lower() == 'y':
                    cabang()
                elif putusan.lower() == 'n' :
                    tulis()
                    homepage()
                else :
                    lanjutan_3 ()
                    
            def hapus_kolam_2 ():
                def hapus_lanjut():
                    pilihan = input('Apakah Anda Ingin Menghapus Kolam Lagi? [y/n]: ')
                    if pilihan.lower() == 'y':
                        hapus_kolam()
                        hapus_kolam_2()
                    elif pilihan.lower() == 'n' :
                        lanjutan_3()
                    else :
                        hapus_lanjut()
                bersih()
                judul_gantiair()
                tampilkandataair()
                hapus_lanjut()
                
            def hapus_tanggal_2 ():
                def hapus_lagi():
                    pilihan = input('Apakah Anda Ingin Menghapus Tanggal Lagi? [y/n]: ')
                    if pilihan.lower() == 'y':
                        hapus_tanggal()
                        hapus_tanggal_2()
                    elif pilihan.lower() == 'n' :
                        lanjutan_3()
                    else :
                        hapus_lagi()
                bersih()
                judul_gantiair()
                tampilkandataair()
                hapus_lagi()
                
            def cabang ():
                def keputusan_cabang ():
                    print ('='*67)
                    apa = int(input ('Masukkan Pilihan Anda :'))
                    if apa == 1 :
                        hapus_tanggal()
                        hapus_tanggal_2()
                    elif apa == 2 :
                        hapus_kolam()
                        hapus_kolam_2()
                    elif apa == 3 :
                        gantiair()
                    else :
                        keputusan_cabang()
                bersih()
                judul_gantiair()
                print('Manakah Yang Ingin Anda Hapus?')
                pilihan = '[1] Menghapus Tanggal', '[2] Menghapus Kolam', '[3] Kembali'
                for i in pilihan:
                    print(i)
                keputusan_cabang()
            bersih ()
            judul_gantiair ()
            cabang()
        elif keputusan == '4' :
            def lanjutan_4 ():
                bersih()
                judul_gantiair()
                tampilkandataair()
                putusan = input ('Apakah Ingin Kembali? [y/n] :')
                if putusan.lower() == 'y':
                    gantiair()
                elif putusan.lower() == 'n' :
                    tulis()
                    homepage()
                else :
                    lanjutan_4 ()
                    
            def tambah ():
                def tambah_selanjutnya ():
                    putusan = input ('Apakah Anda Ingin Menambahkan Kolam Lagi? [y/n] :')
                    if putusan.lower() == 'y' :
                        tambahkolam()
                        tambah()
                    elif putusan.lower() == 'n' :
                        lanjutan_4()
                    else :
                        tambah_selanjutnya()
                bersih()
                judul_gantiair()
                tampilkandataair()
                tambah_selanjutnya()
            bersih()
            judul_gantiair()
            tambahkolam()
            tambah()
        elif keputusan == '5' :
            homepage ()
        else :
            bersih() #Memanggil fungsi bersih
            judul_gantiair() #Memanggil fungsi judul
            print ('Halaman Tidak Ditemukan!!!') #Mencetak kata dalam string
            pilihan = ('1. Kembali','2. Keluar') #Variabel menyimpan pilihan menu
            for i in pilihan : 
                print (i)
            print ('='*43)
            def ulang ():
                putusan = input ('Masukkan pilihan anda :')
                if putusan == '1' :
                    fiturair()
                elif putusan == '2' :
                    keluar3()
                else :
                    ulang ()
            ulang ()
    baca()
    gantiair()
homepage()