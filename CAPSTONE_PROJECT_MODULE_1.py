daftarItemToko = {
    "1":{"Nama":"Espresso", "Ukuran (mL)":200, "Tingkat Kepahitan":"Sangat Kuat", "Stok":10, "Harga":20000},
    "2":{"Nama":"Americano", "Ukuran (mL)":500 , "Tingkat Kepahitan":"Kuat", "Stok":10, "Harga":25000},
    "3":{"Nama":"Cafe Latte", "Ukuran (mL)":500, "Tingkat Kepahitan":"Lemah", "Stok":10, "Harga":30000}
}

daftarMenuUtama = ('''
1. Tampilkan Barang
2. Tambah Barang
3. Edit Barang
4. Hapus Barang
5. Keluar Toko
''')

daftarMenuOpsi1 = ('''
1. Tampilkan Semua Barang di Toko
2. Tampilkan Barang Secara Spesifik

3. Kembali ke Menu Utama
''')

daftarMenuOpsi2 = ('''
1. Tambah Barang
2. Kembali ke Menu Utama
''')

daftarMenuOpsi3 = ('''
1. Edit Barang
2. Kembali ke Menu Utama
''')

daftarMenuOpsi4 = ('''
1. Hapus Barang
2. Kembali ke Menu Utama
''')

while True:
    userLoginID = input("Masukkan ID: ")
    userLoginPassword = input("Masukkan Password: ")
    loginID = "admin"
    loginPassword = "snami_bog"
    if userLoginID != loginID or userLoginPassword != loginPassword:
        print("ID atau Password salah. Silahkan coba kembali.")
        
    else:

        while True:
            print("Selamat Datang di Coffee Shop Kiko")
            print(daftarMenuUtama)
            userInput = int(input("Silahkan pilih menu (1-5): "))
        #============================================================================================================================================ Menu 5 (Exit)    
            if userInput == 5:
                print('''
        Terima kasih telah berkunjung ke Coffee Shop Kiko
        Sampai Jumpa!
                ''')
                break
            while True:
        #============================================================================================================================================ Menu 1 (Tampilkan Barang)        
                if userInput < 1 or userInput > 5:
                    print()
                    print("Opsi yang Anda masukkan tidak valid. Anda akan diarahkan ke menu utama.")
                    print()
                    break
                elif userInput == 1:
                    print('Anda telah masuk di menu "Tampilkan Barang di Toko".')
                    if len(daftarItemToko) == 0:
                        print()
                        print("Tidak ada barang yang tersedia. Anda akan diarahkan ke Menu Utama.")
                        print()
                        break
                    else:
                        print(daftarMenuOpsi1)
                        userInput2 = int(input("Silahkan pilih layanan (1-3): "))
                        if userInput2 == 1:
                            print(f'{"Nomor Item":<20}| {"Nama Kopi":<20}| {"Ukuran (mL)":<20}| {"Tingkat Kepahitan":<20}| {"Stok":<20}| {"Harga":<20} ')
                            print("===================================================================================================================")
                            for i in daftarItemToko:
                                nama = daftarItemToko[i]['Nama']
                                ukuran = daftarItemToko[i]['Ukuran (mL)']
                                tingkatPahit = daftarItemToko[i]['Tingkat Kepahitan']
                                stok = daftarItemToko[i]['Stok']
                                harga = daftarItemToko[i]['Harga']
                                print(f'{i:<20}| {nama:<20}| {ukuran:<20}| {tingkatPahit:<20}| {stok:<20}| {harga:<20}')
                        elif userInput2 == 2:
                            userInput3 = input("Masukkan Nomor Item: ")
                            search_key = userInput3
                            if search_key in daftarItemToko.keys():
                                print(f'{"Nomor Item":<20}| {"Nama Kopi":<20}| {"Ukuran (mL)":<20}| {"Tingkat Kepahitan":<20}| {"Stok":<20}| {"Harga":<20} ')
                                print("===================================================================================================================")
                                nama = daftarItemToko[search_key]['Nama']
                                ukuran = daftarItemToko[search_key]['Ukuran (mL)']
                                tingkatPahit = daftarItemToko[search_key]['Tingkat Kepahitan']
                                stok = daftarItemToko[search_key]['Stok']
                                harga = daftarItemToko[search_key]['Harga']
                                print(f'{search_key:<20}| {nama:<20}| {ukuran:<20}| {tingkatPahit:<20}| {stok:<20}| {harga:<20}')
                                print()
                            else:
                                print()
                                print("Barang tidak ada didalam toko. Anda akan diarahkan ke Menu 'Tampilkan Barang di Toko'.")
                                print()
                        elif userInput2 == 3:
                            break
        #============================================================================================================================================ Menu 2 (Tambah Barang)        
                elif userInput == 2:
                    print('Anda telah masuk di menu "Tambah Barang".')
                    print(daftarMenuOpsi2)
                    userInputTambahBarang = int(input("Silahkan pilih layanan (1-2): "))
                    if userInputTambahBarang == 0 or userInputTambahBarang > 2:
                        print()
                        print("Opsi yang Anda masukkan tidak valid. Silahkan pilih layanan (1-2)")
                        print()
                    elif userInputTambahBarang == 2:
                        break
                    else:
                        userInput4 = input("Masukkan Nomor Item Baru: ")
                        search_key2 = userInput4
                        if search_key2 in daftarItemToko.keys():
                            print()
                            print("Barang sudah terdaftar pada inventori.")
                            print()
                        else:
                            userInput5 = input("Masukkan Nama Kopi Baru: ")
                            userInput6 = int(input("Masukkan Ukuran (mL) Kopi Baru: "))
                            userInput15 = input("Masukkan Tingkat Kepahitan Kopi Baru: ")
                            userInput7 = int(input("Masukkan Stok Kopi Baru: "))
                            userInput8 = int(input("Masukkan Harga Kopi Baru: "))
                            daftarBarangBaru = {userInput4:{"Nama":userInput5, "Ukuran (mL)":userInput6, "Tingkat Kepahitan":userInput15, "Stok":userInput7, "Harga":userInput8}}
                            print()
                            userInputKonfirmasi7 = input("Apakah Anda yakin ingin menambah barang ini? (Y/N)")
                            print()
                            userInputKonfirmasi8 = userInputKonfirmasi7.lower()
                            if userInputKonfirmasi8 == "y":
                                daftarItemToko.update(daftarBarangBaru)
                                print(f'{"Nomor Item":<20}| {"Nama Kopi":<20}| {"Ukuran (mL)":<20}| {"Tingkat Kepahitan":<20}| {"Stok":<20}| {"Harga":<20} ')
                                print("===================================================================================================================")
                                print(f'{userInput4:<20}| {userInput5:<20}| {userInput6:<20}| {userInput15:<20}| {userInput7:<20}| {userInput8:<20}')
                                print()                            
                                print("Barang berhasil ditambah.")
                                print()
                            elif userInputKonfirmasi8 == "n":
                                print()
                                print("Barang gagal ditambah. Anda akan diarahkan ke menu 'Tambah Barang'.")
                                print()
                                continue
                            else:
                                print()
                                print('Opsi yang Anda masukkan tidak valid.')
                                print()
            #============================================================================================================================================ Menu 3 (Edit Barang)        
                elif userInput == 3:
                    print('Anda telah masuk di menu "Edit Barang".')
                    print(daftarMenuOpsi3)
                    userInputEditBarang = int(input("Silahkan pilih layanan (1-2): "))
                    if userInputEditBarang == 0 or userInputEditBarang > 2:
                        print()
                        print("Opsi yang Anda masukkan tidak valid. Silahkan pilih layanan (1-2)")
                        print()
                    elif userInputEditBarang == 1:
                        userInput9 = input("Masukkan nomor item yang ingin diedit: ")
                        search_key3 = userInput9
                        if search_key3 not in daftarItemToko.keys():
                            print()
                            print("Item tidak terdaftar.")
                            print()
                        else:
                            print(f'{"Nomor Item":<20}| {"Nama Kopi":<20}| {"Ukuran (mL)":<20}| {"Tingkat Kepahitan":<20}| {"Stok":<20}| {"Harga":<20} ')
                            print("===================================================================================================================")
                            nama = daftarItemToko[search_key3]['Nama']
                            ukuran = daftarItemToko[search_key3]['Ukuran (mL)']
                            tingkatPahit = daftarItemToko[search_key3]['Tingkat Kepahitan']
                            stok = daftarItemToko[search_key3]['Stok']
                            harga = daftarItemToko[search_key3]['Harga']
                            print(f'{search_key3:<20}| {nama:<20}| {ukuran:<20}| {tingkatPahit:<20}| {stok:<20}| {harga:<20}')
                            print()                            
                            userInputKonfirmasi1 = input("Apakah Anda yakin ingin edit barang ini? (Y/N)")
                            print()
                            userInputKonfirmasi2 = userInputKonfirmasi1.lower()
                            if userInputKonfirmasi2 == "n":
                                print()
                                print('Anda akan diarahkan ke menu "Edit Barang".')
                                print()
                                continue
                            elif userInputKonfirmasi2 != "y" and "n" :
                                print()
                                print("Opsi yang Anda masukkan tidak valid.")
                                print()
                            else:
                                userInput10 = input("Masukkan Nama Kopi baru: ")
                                userInput11 = int(input("Masukkan Ukuran (mL) Baru: "))
                                userInput16 = input("Masukkan Tingkat Kepahitan Baru: ")
                                userInput12 = int(input("Masukkan Stok Kopi Baru: "))
                                userInput13 = int(input("Masukkan Harga Kopi Baru: "))
                                daftarBarangEdit = {"Nama":userInput10, "Ukuran (mL)":userInput11, "Tingkat Kepahitan":userInput16, "Stok":userInput12, "Harga":userInput13}
                                print()
                                userInputKonfirmasi3 = input("Apakah Anda benar-benar yakin ingin EDIT barang ini? (Y/N)")
                                print()
                                userInputKonfirmasi4 = userInputKonfirmasi3.lower()
                                if userInputKonfirmasi4 == "y":
                                    daftarItemToko[search_key3] = daftarBarangEdit
                                    print(f'{"Nomor Item":<20}| {"Nama Kopi":<20}| {"Ukuran (mL)":<20}| {"Tingkat Kepahitan":<20}| {"Stok":<20}| {"Harga":<20} ')
                                    print("===================================================================================================================")
                                    print(f'{search_key3:<20}| {userInput10:<20}| {userInput11:<20}| {userInput16:<20}| {userInput12:<20}| {userInput13:<20}')
                                    print()   
                                    print("Barang berhasil diedit.")
                                    print()
                                elif userInputKonfirmasi4 == "n":
                                    print()
                                    print('Barang gagal diedit.')
                                    print()
                                    continue
                                else:
                                    print()
                                    print("Opsi yang Anda masukkan tidak valid.")
                                    print()
                    elif userInputEditBarang == 2:
                        break
    #============================================================================================================================================ Menu 4 (Hapus Barang)        
                elif userInput == 4:
                    print('Anda telah masuk di menu "Hapus Barang".') 
                    print(daftarMenuOpsi4)
                    userInputHapusBarang = int(input("Silahkan pilih layanan (1-2): "))
                    if userInputHapusBarang == 0 or userInputHapusBarang > 2:
                        print()
                        print("Opsi yang Anda masukkan tidak valid. Silahkan pilih layanan (1-2)")
                        print()
                    elif userInputHapusBarang == 1:
                        userInput14 = input("Masukkan nomor barang yang ingin dihapus: ")
                        search_key4 = userInput14
                        if search_key4 not in daftarItemToko.keys():
                            print()
                            print("Barang tidak terdaftar")
                            print()
                        else:
                            print(f'{"Nomor Item":<20}| {"Nama Kopi":<20}| {"Ukuran (mL)":<20}| {"Tingkat Kepahitan":<20}| {"Stok":<20}| {"Harga":<20} ')
                            print("===================================================================================================================")
                            print(f'{search_key4:<20}| {daftarItemToko[search_key4]["Nama"]:<20}| {daftarItemToko[search_key4]["Ukuran (mL)"]:<20}| {daftarItemToko[search_key4]["Tingkat Kepahitan"]:<20}| {daftarItemToko[search_key4]["Stok"]:<20}| {daftarItemToko[search_key4]["Harga"]:<20}')
                            print()                            
                            userInputKonfirmasi5 = input("Apakah Anda benar-benar yakin ingin HAPUS barang ini? (Y/N)")
                            userInputKonfirmasi6 = userInputKonfirmasi5.lower()
                            print()
                            if userInputKonfirmasi6 == "y":
                                del daftarItemToko[search_key4]
                                print(f'{"Nomor Item":<20}| {"Nama Kopi":<20}| {"Ukuran (mL)":<20}| {"Tingkat Kepahitan":<20}| {"Stok":<20}| {"Harga":<20} ')
                                print("===================================================================================================================")
                                for i in daftarItemToko:
                                    nama = daftarItemToko[i]['Nama']
                                    ukuran = daftarItemToko[i]['Ukuran (mL)']
                                    tingkatPahit = daftarItemToko[i]['Tingkat Kepahitan']
                                    stok = daftarItemToko[i]['Stok']
                                    harga = daftarItemToko[i]['Harga']
                                    print(f'{i:<20}| {nama:<20}| {ukuran:<20}| {tingkatPahit:<20}| {stok:<20}| {harga:<20}')
                                print()
                                print("Barang berhasil dihapus.")
                                print()
                            elif userInputKonfirmasi6 == "n":
                                print()
                                print("Barang gagal dihapus.")
                                print()
                                continue
                            else:
                                print()
                                print("Opsi yang Anda masukkan tidak valid.")
                                print()
                    elif userInputHapusBarang == 2:
                        break               
