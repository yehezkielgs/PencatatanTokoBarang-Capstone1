dataBarang = [
    {'Kode' : 'ITEM001',
    'Jenis' : 'Headset', 
    'Nama' : 'Rexus Thundervox HX30',
    'Stock' : '10',
    'Harga' : '50000'},
    {'Kode' : 'ITEM002',
    'Jenis' : 'Mouse',
    'Nama' : 'Fantech Helios XD3',
    'Stock' : '15',
    'Harga' : '100000'}
]

def ReportDataSeluruh(data):
    if(data == []):
        print('***Tidak Ada Data Barang***')
    else:
        print('Daftar Barang:\n')
        for i in range(len(data)):
            print('{}. Kode : {}, Jenis: {}, Nama: {}, Stock = {}, Harga = {}'.
            format((i+1),data[i]['Kode'],data[i]['Jenis'],data[i]['Nama'],data[i]['Stock'],data[i]['Harga']))
    
def ReportDataSebagian(data):
    if(data == []):
        print('***Tidak Ada Data Barang***')
    else:
        kodeItem = []
        for i in range(len(data)):
            kodeItem.append(data[i]['Kode'])
        while(True):
            barangTampil = input('Masukan Kode:').upper()    
            if(barangTampil in kodeItem):
                for i in range(len(data)):
                    if (data[i]['Kode'] == barangTampil):
                        print('Data Barang dengan Kode : {}'.format(barangTampil))
                        print('1. Kode : {}, Jenis: {}, Nama: {}, Stock = {}, Harga = {}'.
                        format(data[i]['Kode'],data[i]['Jenis'],data[i]['Nama'],data[i]['Stock'],data[i]['Harga']))
                break
            else:
                print('***Tidak Ada Data Barang***')
            

def CreateData(data):
    kodeItem = []
    for i in range(len(data)):
        kodeItem.append(data[i]['Kode'])
    
    kodeCreate = input('Masukan Kode: ').upper()
    if kodeCreate in kodeItem:
        print('''Data sudah ada''')
    else:
        jenisCreate = input('Masukan Jenis Barang: ').capitalize()
        namaCreate = input('Masukan Nama Barang: ').capitalize()
        stockCreate = input('Masukan Stock Barang: ')
        hargaCreate = input('Masukan Harga Barang: ')
        while(True):
            simpanData = input('Apakah Data akan disimpan? (Y/N): ').upper()
            if simpanData == 'Y':
                data.append({'Kode':kodeCreate,'Jenis':jenisCreate,'Nama':namaCreate,'Stock':stockCreate,'Harga':hargaCreate})
                break
            elif simpanData == 'N':
                break

def UpdateData(data):
    kodeItem = []
    for i in range(len(data)):
        kodeItem.append(data[i]['Kode'])
    
    kodeUpdate = input('Masukan kode: ').upper()
    if kodeUpdate not in kodeItem:
        print('''Data tidak ada''')
    else:
        for i in range(len(data)):
            if (data[i]['Kode'] == kodeUpdate):         
                print('1. Kode : {}, Jenis: {}, Nama: {}, Stock = {}, Harga = {}'.
                format(data[i]['Kode'],data[i]['Jenis'],data[i]['Nama'],data[i]['Stock'],data[i]['Harga']))
        while(True):
            updateData = input('Tekan Y jika ingin lanjut Update data atau N jika ingin cancel Update (Y/N) :').upper()
            if (updateData == 'Y'):
                kolomUpdate = input('Masukan kolom/keterangan yang ingin diubah :').capitalize()
                dataUpdate = input('Masukan {} Baru:'.format(kolomUpdate)) 
                while(True):
                    dataUpdate2 = input('Apakah Data akan diupdate? (Y/N):').upper()
                    if dataUpdate2 == 'Y':
                        for i in range(len(data)):
                            if (data[i]['Kode'] == kodeUpdate): 
                                data[i][kolomUpdate] = dataUpdate
                        print('Data Updated')
                        break
                    if dataUpdate2 == 'N':
                        print('Data tidak terupdate')
                        break
                break
            elif (updateData == 'N'):
                break

def DeleteData(data):
    kodeItem = []
    for i in range(len(data)):
        kodeItem.append(data[i]['Kode'])
    
    kodeDelete = input('Masukan kode: ').upper()
    if kodeDelete not in kodeItem:
        print('''Data tidak ada''')
    else:
        while(True):
            deleteData = input('Apakah Data akan dihapus? (Y/N):').upper()
            if deleteData == 'Y':
                for i in range(len(data)):
                    if (data[i]['Kode']==kodeDelete):
                        deletedIndex = i
                del data[deletedIndex]
                print('Data Deleted')
                break
            if deleteData == 'N':
                print('Data tidak terhapus')
                break


while(True):
    mainMenu = input('''
    ====Data Penjualan Barang Toko====

    1. Report Data Barang
    2. Menambahkan Data Barang
    3. Mengubah Data Barang
    4. Menghapus Data Barang
    5. Exit
    Silakan Pilih Main_Menu [1-5] :''')
    if (mainMenu=='1'):
        while(True):
            menuReport = input('''
            ++++Report Data Barang++++

            1. Report Seluruh Data
            2. Report Data tertentu
            3. Kembali Ke Menu Utama
            Silakan Pilih Sub Menu Read Data [1-3]:''')
            if(menuReport=='1'):
                ReportDataSeluruh(dataBarang)
            elif(menuReport=='2'):
                ReportDataSebagian(dataBarang)
            elif(menuReport=='3'):
                break
    elif (mainMenu=='2'):
        while(True):
            menuCreate = input('''
            ++++Menambah Data Barang++++

            1. Tambah Data Barang
            2. Kembali Ke Menu Utama
            Silakan Pilih Sub Menu Read Data [1-2]:''')
            if (menuCreate=='1'):
                CreateData(dataBarang)  
            elif (menuCreate=='2'):
                break      
    elif (mainMenu=='3'):
        while(True):
            menuUpdate = input('''
            ++++Mengubah Data Barang++++

            1. Ubah Data Barang
            2. Kembali Ke Menu Utama
            Silakan Pilih Sub Menu Read Data [1-2]:''')
            if (menuUpdate=='1'):
                UpdateData(dataBarang)
            elif (menuUpdate=='2'):
                break
    elif (mainMenu=='4'):
        while(True):
            menuDelete = input('''
            ++++Menghapus Data Barang++++

            1. Hapus Data Barang
            2. Kembali Ke Menu Utama
            Silakan Pilih Sub Menu Read Data [1-2]:''')
            if (menuDelete=='1'):
                DeleteData(dataBarang)
            elif (menuDelete=='2'):
                break
    elif (mainMenu=='5'):
        break
    else:
        print('Pilihan user salah')