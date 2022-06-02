listraket = {
    'Yonex Astrox 99 JP 3UG5': {'Nama':'Yonex Astrox 99 JP 3UG5', 'Balance Point':'Head Heavy', 'Flex':'Very Stiff', 'Stock': 5, 'Harga': 2600000},
    'Victor Thruster F Special Edition 4UG5': {'Nama':'Victor Thruster F Special Edition 4UG5', 'Balance Point':'Head Heavy', 'Flex':'Stiff', 'Stock': 12, 'Harga': 2500000},
    'Yonex Astrox 100 ZZ Kurenai 4UG5': {'Nama':'Yonex Astrox 100 ZZ Kurenai 4UG5', 'Balance Point':'Head Heavy', 'Flex':'Stiff', 'Stock': 32, 'Harga': 2400000},
    'Yonex Nanoflare 800 4UG5': {'Nama':'Yonex Nanoflare 800 4UG5', 'Balance Point':'Head Light', 'Flex':'Stiff', 'Stock': 10, 'Harga': 2000000},
    'Victor DriveX 9X 4UG5' : {'Nama':'Victor DriveX 9X 4UG5', 'Balance Point':'Head Light', 'Flex':'Stiff', 'Stock': 9, 'Harga': 2500000} }



cart = []

while True :
    pmenu = input('''
        Selamat Datang di Lumbung Sport, Distributor Raket Badminton no. 1 di Karawang!

        Ada yang bisa kami bantu?
        1. Ada raket apa saja sih di Lumbung Sport?
        2. Saya lagi cari raket ini nih, apakah ada stocknya?
        3. SAYA MAU BELI RAKET BARU KOH!
        4. Koh saya mau supply raket baru koh. Tolong bantu jual ya.
        5. Khusus pegawai: Hapus data raket.
        6. Khusus pegawai: Edit data raket.
        7. Gak jadi nanya koh, cmn mau lihat-lihat.

        Masukkan angka menu piilihan anda : ''')

    if(pmenu == '1') :

        print('Daftar Raket Lumbung Sport\n')
        print('Nomor\t| Nama  \t| Stock\t| Harga\t| Balance Point\t| Flex')
        for i in listraket :
            print('{}\t| {}  \t| {}\t| {}\t| {}\t| {}'.format(i,listraket[i]['Nama'],listraket[i]['Stock'],listraket[i]['Harga'],listraket[i]['Balance Point'],listraket[i]['Flex']))
    
    elif(pmenu == '2') :

        #READ DATA
        def checkout():
            
            namaraket = input('Masukkan Nama Raket yang Anda Cari (Mohon gunakan format seperti contoh (Yonex Astrox 99 JP 4UG5)) ')
            if namaraket in listraket:
                 print ('Ada bos barangnya \t')
                 print (listraket[namaraket])
                 print ('Kalau mau beli, bisa akses lewat menu beli ya bos!')
        
            else:
                print('Belum ada barangnya bos')
               
        maulagi= 'iya'
        while maulagi == 'iya':
            checkout()
            maulagi= input('Apa ada raket lain yang mau dicari bos?\t (Tolong jawab dengan iya/tidak)')
                       
            if maulagi =='tidak':
                break
    #Beli
    elif(pmenu == '3'):
        cart=[]
        maulagi = 'iya'
        while maulagi=='iya':
            print('Daftar Raket Lumbung Sport\n')
            print('Nomor\t| Nama  \t| Stock\t| Harga\t| Balance Point\t| Flex')
            for i in listraket :
                print('{}\t| {}  \t| {}\t| {}\t| {}\t| {}'.format(i,listraket[i]['Nama'],listraket[i]['Stock'],listraket[i]['Harga'],listraket[i]['Balance Point'],listraket[i]['Flex']))
            beli= input('Ketik nama raket yang anda mau beli (Tolong lengkap sesuai daftar raket): ')
            if beli not in listraket:
                print('Nama produk tidak sesuai/tidak ada')
                break
            jmlbeli= input('Jumlah raket yang anda mau beli? ')
            harga= listraket[beli]['Harga']
            if int(jmlbeli) > int(listraket[beli]['Stock']):
                print('Stocknya kurang bos, tolong dikurangi')
                break
            else:
                cart.append([beli, jmlbeli, '@', listraket[beli]['Harga']])
                print('Thank you bos masuk keranjang tinggal bayar')
            print('Isi keranjang: ')
            print(cart)
            listraket[beli]['Stock'] -= int(jmlbeli)
            maulagi = input('Mau belanja raket lain? (iya/tidak)')
        tagihan = 0
        if maulagi == 'tidak':
            uangbayar=input('masukkan jumlah bayar')
            for x in cart:
                tagihan += int(x[1])*int(x[3])
        if int(uangbayar)<=tagihan:
            input('Maaf uang kurang bos, coba lagi ya')
        else:
            kembalian = int(int(uangbayar)-tagihan)
            print('ini kembaliannya bos {}, terimakasih sudah belanja di kami. '. format(kembalian))
            cart.clear()
            break
  
    #Create Data
    elif(pmenu == '4') :
        maulagi = 'iya'
        while maulagi=='iya':
            namabaru = input('Boleh bos, tolong isi formulirnya berurutan ya. Raketnya series apa? (Contoh: Yonex Astrox 99 JP 4UG5): ')
            for i in listraket:
                if namabaru == listraket[i]['Nama']:
                    print ('Sudah ada bos barangnya, coba menu edit ya')
                    break
                else:
                    def create():
                      
                        stockbaru = input('Ada berapa banyak barangnya? ')
                        hargabaru = input('Harga berapa kasih saya? ')
                        bpbaru = input('Balance Pointnya head heavy atau head light? ')
                        flexbaru = input('Flexible atau stiff? ')
                        
                        print('Oke bos, sudah masuk datanya')
                        listraket[namabaru]={'Nama':namabaru, 'Stock':stockbaru, 'Harga':hargabaru, 'Balance Point':bpbaru, 'Flex':flexbaru}
                        print('Daftar Raket Lumbung Sport\n')
                        print('KODE\t| Nama  \t| Stock\t| Harga\t| Balance Point\t| Flex')
                        for i in listraket :
                            print('{}\t| {}  \t| {}\t| {}\t| {}\t| {}'.format(i,listraket[i]['Nama'],listraket[i]['Stock'],listraket[i]['Harga'],listraket[i]['Balance Point'],listraket[i]['Flex']))

                    create()
                    break
                
                     
           
            maulagi =input ('Apa ada raket lain yang mau dititip jual bos?\t (Tolong jawab dengan iya/tidak)')
            if maulagi =='tidak':
                break



    #Delete Data
    elif(pmenu == '5') :
        maulagi = 'iya'
        while maulagi == 'iya':
            pwd=input('Masukkan kata sandi pegawai:  ')
            if pwd == 'tokoraket':
                print('Daftar Raket Lumbung Sport\n')
                print('KODE\t| Nama  \t| Stock\t| Harga\t| Balance Point\t| Flex')
                for i in listraket :
                    print('{}\t| {}  \t| {}\t| {}\t| {}\t| {}'.format(i,listraket[i]['Nama'],listraket[i]['Stock'],listraket[i]['Harga'],listraket[i]['Balance Point'],listraket[i]['Flex']))

                def hapus():
                    ihapus= input('Ketik nama barang yang mau dihapus:  ')
                    if ihapus in listraket:
                        del listraket[ihapus]
                        print('Data berhasil dihapus')
                        print('Daftar Raket Lumbung Sport\n')
                        print('KODE\t| Nama  \t| Stock\t| Harga\t| Balance Point\t| Flex')
                        for i in listraket :
                            print('{}\t| {}  \t| {}\t| {}\t| {}\t| {}'.format(i,listraket[i]['Nama'],listraket[i]['Stock'],listraket[i]['Harga'],listraket[i]['Balance Point'],listraket[i]['Flex']))
                              
                    else:
                        print('Data tidak ditemukan')
                    
                        
                hapus()
                maulagi = input('Apakah anda mau coba lagi? (jawab iya/tidak) \t')
                if maulagi == 'tidak':
                    break
            else:
                print('Password yang anda masukkan salah')
                maulagi = input('Apakah anda mau coba lagi? (jawab iya/tidak) \t')
                if maulagi == 'tidak':
                    break
     #Update Data
    elif(pmenu == '6') :
        maulagi = 'iya'
        while maulagi == 'iya':
            pwd=input('Masukkan kata sandi pegawai:  ')
            if pwd == 'tokoraket':
                print('Daftar Raket Lumbung Sport\n')
                print('KODE\t| Nama  \t| Stock\t| Harga\t| Balance Point\t| Flex')
                for i in listraket :
                    print('{}\t| {}  \t| {}\t| {}\t| {}\t| {}'.format(i,listraket[i]['Nama'],listraket[i]['Stock'],listraket[i]['Harga'],listraket[i]['Balance Point'],listraket[i]['Flex']))

                def rubah():
                    irubah= input('Ketik nama barang yang mau diubah:  ')
                    if irubah in listraket:
                        namabaru = input('Nama baru produk (isi nama lama bila tidak berubah): ')
                        stockbaru = input('Sekarang stocknya berapa? ')
                        hargabaru = input('Harga baru jadi berapa? ')
                        bpbaru = input('Balance pointnya? ')
                        flexbaru = input('Flexible atau stiff? ')
                        listraket[irubah]['Nama']='{}'.format(namabaru)
                        listraket[irubah]['Stock']='{}'.format(stockbaru)
                        listraket[irubah]['Harga']='{}'.format(hargabaru)
                        listraket[irubah]['Balance Point']='{}'.format(bpbaru)
                        listraket[irubah]['Flex']='{}'.format(flexbaru)
                        print('Data berhasil diubah')
                        print('Daftar Raket Lumbung Sport\n')
                        print('KODE\t| Nama  \t| Stock\t| Harga\t| Balance Point\t| Flex')
                        for i in listraket :
                            print('{}\t| {}  \t| {}\t| {}\t| {}\t| {}'.format(i,listraket[i]['Nama'],listraket[i]['Stock'],listraket[i]['Harga'],listraket[i]['Balance Point'],listraket[i]['Flex']))
                              
                    else:
                        print('Data tidak ditemukan')
                    
                        
                rubah()
                maulagi = input('Apakah anda mau coba lagi? (jawab iya/tidak) \t')
                if maulagi == 'tidak':
                    break
            else:
                print('Password yang anda masukkan salah')
                maulagi = input('Apakah anda mau coba lagi? (jawab iya/tidak) \t')
                if maulagi == 'tidak':
                    break            
                   
            

    elif(pmenu == '7') :
        break
