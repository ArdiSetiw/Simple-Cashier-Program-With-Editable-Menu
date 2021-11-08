from random import choice
import secrets as gaca

# List Berbagai Macam List
list_drink = ["air","teh","kopi"]   # List Menu Minuman
harga_drink = [3000,5000,10000]     # List Harga Minuman
list_food = ["sate","borger"]       # List Menu Makanan
harga_food = [15000,20000]          # List Harga Makanan
drink_cart = []                     # Keranjang Pesanan Minuman
food_cart = []                      # Keranjang Pesanan Makanan
price_drink = []                    # Harga Pesanan Minuman
price_food = []                     # Harga Pesanan Makanan

# Fungsi Menu dan Pesanan
def show_menu ():
    print("="*57)
    print("\033[32m-----------------------Menu Saat Ini---------------------\033[39m")
    print("\033[34m-> Menu Minuman")
    for p,q in zip (list_drink,harga_drink):
        print("-",p,"=",q,)
    print("-> Menu Makanan")
    for r,s in zip (list_food,harga_food):
        print("-",r,"=",s)
    print("\033[39m")
def show_menu_drink ():
    print("="*57)
    print("\033[32m---------------------Proses Pemesanan--------------------\033[39m")
    print("\033[36m-> Menu Minuman")
    for p,q in zip (list_drink,harga_drink):
        print("-",p,"=",q,)
    print("\033[39m")
def show_menu_food():
    print("="*57)
    print("\033[36m-> Menu Makanan")
    for r,s in zip (list_food,harga_food):
        print("-",r,"=",s)
    print("\033[39m")
def ordering_drink():
    print("="*57)
    print("> Ketik pesanan sesuai yang tertera di menu")
    print("> Ketik 'end' untuk berhenti memesan")
    x = 1 
    while x > 0 :
        pesan = str(input("Pesanan Minuman = "))
        if pesan in list_drink :
            drink_cart.append(pesan)
            i = list_drink.index(pesan)
            price = harga_drink[i]
            price_drink.append(price)
        elif pesan == "end":
            print("\033[32mPesanan Telah Disimpan\033[39m")
            x-=1
        else :
            print("\033[31mMaaf, Kita tidak memiliki menu tersebut\033[39m")
def ordering_food():
    print("="*57)
    print("> Ketik pesanan sesuai yang tertera di menu")
    print("> Ketik 'end' untuk berhenti memesan")
    x = 1 
    while x > 0 :
        pesan = str(input("Pesanan Makanan = "))
        if pesan in list_food :
            food_cart.append(pesan)
            i = list_food.index(pesan)
            price = harga_food[i]
            price_food.append(price)
        elif pesan == "end":
            print("\033[32mPesanan Telah Disimpan\033[39m")
            x-=1
        else :
            print("\033[31mMaaf, Kita tidak memiliki menu tersebut\033[39m")
def paydiscount():
    # Diskon Minuman
    total_drink = sum(price_drink)
    if len(drink_cart) >= 3 :
        print("="*57)
        print("\033[32m-> Ini Pesanan Minuman Anda")
        for x,y in zip (drink_cart,price_drink):
            print("-",x,"= Rp",y)
        print("Total Harga Minuman = Rp",total_drink,"\033[39m")
        print("| Anda dapat 10% Diskon karena membeli setidaknya 3 Minuman")
        total_drink = total_drink - (total_drink*10/100)
        print("\033[32mTotal Harga Minuman = Rp",total_drink,"\033[39m")
    else :
        print("="*57)
        print("\033[32m-> Ini Pesanan Minuman Anda")
        for x,y in zip (drink_cart,price_drink):
            print("-",x,"= Rp",y)
        print("Total Harga Minuman = Rp",total_drink,"\033[39m")
    # Diskon Makanan
    total_food = sum(price_food)
    if len(food_cart) >= 2 :
        print("="*57)
        print("\033[32m-> Ini Pesanan Makanan Anda")
        for x,y in zip (food_cart,price_food):
            print("-",x,"= Rp",y)
        print("Total Harga Makanan = Rp",total_food,"\033[39m")
        print("| Anda dapat 5% Diskon karena membeli setidaknya 2 Makanan")
        total_food = total_food - (total_food*5/100)
        print("\033[32mTotal Harga Makanan = Rp",total_food,"\033[39m")
    else :
        print("="*57)
        print("\033[32m-> Ini Pesanan Makanan Anda")
        for x,y in zip (food_cart,price_food):
            print("-",x,"= Rp",y)
        print("Total Harga Makanan = Rp",total_food,"\033[39m")
    price = total_drink + total_food 
    print("="*57)
    print("\033[32mHarga Makanan dan Minuman = Rp",price,"\033[39m")
    print("="*57)
    # Diskon Hari
    # Hari beli 
    day = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
    hari = gaca.choice(day)
    print("\033[32m          Anda Memesan Pesanan Ini Pada",hari,"\033[39m")
    print("="*57)
    if hari == "Sabtu" or hari == "Minggu" :
        print("Karena Anda memesan ini di hari",hari,"Anda mendapatkan 5% Diskon")
        price = price - (price * 5/100)
        print("\033[32mHarga Setelah Diskon = Rp",price,"\033[39m")
    else :
        print("Karena Anda memesan ini di hari",hari,"Anda mendapatkan 10% Diskon")
        price = price - (price * 10/100)
        print("\033[32mHarga Setelah Diskon = Rp",price,"\033[39m")
    # Pembayaran and The End of the program
    print("="*57)
    print("""\033[36mPilih Pembayaran
    1. Cash
    2. CC Card
    3. eMoney\033[39m""")
    print("="*57)
    bayar = str(input("Pembayaran = "))
    if bayar == "3" :
        print("Pembayaran eMoney, Anda mendapatkan 5% Diskon")
        price = price - (price * 5/100)
        print("\033[32mTotal Harga = Rp",price,"\033[39m")
        print("="*57)
    else : 
        print("\033[32mTotal Harga = Rp",price,"\033[39m")
        print("="*57)
# Fungsi Menambah Menu
def normaladddrink():       # Menambah Menu MINUMAN Pada Akhir List
    print("List Minuman =",list_drink)
    tambah_drink = str(input("Tambah Menu Minuman = "))
    tambah_hargadrink = int(input("Masukkan Harga Minuman = "))
    list_drink.append(tambah_drink)
    harga_drink.append(tambah_hargadrink)
    print("\033[32mMENU DISIMPAN\033[39m")
def indexadddrink():        # Menambah Menu MMINUMAN Berdasarkan Index
    print("List Minuman =",list_drink)
    i = int(input("Masukkan Index Menambah List = "))
    tambah_drink = str(input("Tambah Menu Minuman = "))
    tambah_hargadrink = int(input("Masukkan Harga = "))
    list_drink.insert(i,tambah_drink)
    harga_drink.insert(i,tambah_hargadrink)
    print("\033[32mMENU DISIMPAN\033[39m")
def normaladdfood():        # Menambah Menu MAKANAN Pada Akhir List
    print("List Makanan =",list_food)
    tambah_food = str(input("Tambah Menu Makanan = "))
    tambah_hargafood = int(input("Masukkan Harga Makanan = "))
    list_food.append(tambah_food)
    harga_food.append(tambah_hargafood)
    print("\033[32mMENU DISIMPAN\033[39m")
def indexaddfood():         # Menambah Menu MAKANAN Berdasarkan Index
    print("List Makanan =",list_food)
    i = int(input("Masukkan Index Menambah List = "))
    tambah_food = str(input("Tambah Menu Makanan = "))
    tambah_hargafood = int(input("Masukkan Harga Makanan = "))
    list_food.insert(i,tambah_food)
    harga_food.insert(i,tambah_hargafood)
    print("\033[32mMENU DISIMPAN\033[39m")
# Fungsi Menghapus Menu
def deleteindexdrink():     # Menghapus Menu MINUMAN Metode Index
    print("List Minuman = ",list_drink)
    i = int(input("Masukkan Indext List yang akan dihapus = "))
    if 0 <= i < len(list_drink) :
        print("Ingin Menghapus Menu",list_drink[i],"?")
        x = str(input("1. Ya\n0. Tidak\nPilih = "))
        if x == "1" :
            del list_drink[i]
            del harga_drink[i]
            print("\033[32mMENU TELAH DIHAPUS\033[39m")
        else :
            print("\033[31mBatal Menghapus\033[39m")
    else :
        print("\033[31mNilai Index Tidak Ada Dalam List !\033[39m")
def deleteindexfood():      # Menghapus Menu MAKANAN Metode Index
    print("List Makanan =",list_food)
    i = int(input("Masukkan Index List yang akan dihapus = "))
    if 0 <= i < len(list_food) :
        print("Ingin Menghapus Menu",list_food[i],"?")
        x = str(input("1. Ya\n0. Tidak\nPilih = "))
        if x == "1" :
            del list_food[i]
            del harga_food[i]
            print("\033[32mMENU TELAH DIHAPUS\033[39m")
        else :
            print("\033[31mBatal Menghapus\033[39m")
    else :
        print("\033[31mNilai Index Tidak Ada Dalam List !\033[39m")
def itemdeletedrink():      # Menghapus Menu MINUMAN Metode Item List
    print("List Minuman =",list_drink)
    x = str(input("Ketik Item sesuai yang ada pada List = "))
    if x not in list_drink :
        print("\033[31mItem Tidak Ada Dalam List !\033[39m")
    else :
        i = list_drink.index(x)
        list_drink.remove(x)
        del harga_drink[i]
        print("\033[32mMENU TELAH DIHAPUS\033[39m")
def itemdeletefood():       # Menghapus Menu MAKANAN Metode Item List
    print("List Makanan =",list_food)
    x = str(input("Ketik Item sesuai yand ada pada List = "))
    if x not in list_food :
        print("\033[31mItem Tidak Ada Dalam List !\033[39m")  
    else :
        i = list_food.index(x)
        list_food.remove(x)
        del harga_food[i]
        print("\033[32mMENU TELAH DIHAPUS\033[39m")
# Fungsi Mengubah 
def changedrink():          # Mengubah nama Menu MINUMAN 
    print("List Minuman =",list_drink)
    i = int(input("Masukkan Index list yang akan diubah = "))
    if 0 <= i < len(list_drink) :
        print("Ingin Mengubah Menu",list_drink[i],"?")
        x = str(input("1. Ya\n0. Tidak\nPilih = "))
        if x == "1" :
            change = str(input("Masukkan Perubahan Nama = "))
            list_drink[i] = change
            print("\033[32mMENU TELAH DIUBAH\033[39m")
        else :
            print("\033[31mBatal Mengubah\033[39m")
    else :
        print("\033[31mNilai Index Tidak Ada Dalam List !\033[39m")
def changefood():           # Mengubah nama Menu MAKANAN
    print("List Makanan =",list_food)
    i = int(input("Masukkan Index list yang akan diubah = "))
    if 0 <= i < len(list_food) :
        print("Ingin Mengubah Menu",list_food[i],"?")
        x = str(input("1. Ya\n0. Tidak\nPilih = "))
        if x == "1" :
            change = str(input("Masukkan Perubahan Nama = "))
            list_food[i] = change
            print("\033[32mMENU TELAH DIUBAH\033[39m")
        else :
            print("\033[31mBatal Mengubah\033[39m")
    else :
        print("\033[31mNilai Index Tidak Ada Dalam List !\033[39m")
        
# Proses
x = 1
while x > 0 :
    print("="*57)
    print("\033[36m-----------------------Pilih Program---------------------\n1. Pesan Makanan dan Minuman\n2. Edit Menu Makanan dan Minuman\n\033[31m0. Berhenti\033[39m")
    pilih = str(input("Pilih = "))
    if pilih == "1" :
        y = 1
        while y > 0 :
            print("="*57)
            print("\033[36m   > Pemesanan <\n1. Lanjut Pemesanan\n\033[31m0. Kembali\033[39m")
            choice = str(input("Pilih = "))
            if choice == "1" :
                show_menu_drink()
                ordering_drink()
                show_menu_food()
                ordering_food()
                paydiscount()
            elif choice == "0" :
                y-=1
            else :
                print("\033[31mMohon Ketik Pilihan Yang Tertera\033[39m")
    elif pilih == "2" :
        y = 1
        while y > 0 :
            show_menu()
            print("="*57)
            print("\033[36m   > Pilihan Edit Menu <\n1. Menambah Menu\n2. Menghapus Menu\n3. Mengubah Nama Menu\n\033[31m0. Kembali\033[39m")
            pilih2 = str(input("Pilih Edit Menu = "))
            if pilih2 == "0":
                y-=1
            elif pilih2 == "1":
                print("="*57)
                print("\033[32m   > Metode Menambah <\n1. Tambah Menu di Akhir Menu\n2. Tambah Menu Berdasarkan Index\n\033[31m0. Kembali\033[39m")
                choice = str(input("Pilih Metode Tambahan = "))
                if choice == "1" :
                    z = 1
                    while z > 0 :
                        print("="*57)
                        print("  > Menu yang ditambah <\n1. Minuman\n2. Makanan\n\033[31m0. Kembali\033[39m")
                        choice2 = str(input("Pilih Menu yang akan di tambah = "))
                        if choice2 == "1" :
                            print("="*57)
                            print("MENAMBAH MENU MINUMAN")
                            normaladddrink()
                        elif choice2 == "2":
                            print("="*57)
                            print("MENAMBAH MENU MAKANAN")
                            normaladdfood()
                        elif choice2 == "0":
                            z-=1
                        else :
                            print("\033[31mMohon Ketik Pilihan Yang Tertera\033[39m")
                elif choice == "2" :
                    a = 1
                    while a > 0 : 
                        print("="*57)
                        print("  > Menu yang ditambah <\n1. Minuman\n2. Makanan\n\033[31m0. Kembali\033[39m")
                        choice2 = str(input("Pilih Menu yang akan di tambah = "))
                        if choice2 == "1" :
                            print("="*57)
                            print("MENAMBAH MENU MINUMAN")
                            indexadddrink()
                        elif choice2 == "2":
                            print("="*57)
                            print("MENAMBAH MENU MAKANAN")
                            indexaddfood()
                        elif choice2 == "0":   
                            a-=1   
                        else : 
                            print("\033[31mMohon Ketik Pilihan Yang Tertera\033[39m")
            elif pilih2 == "2" :
                print("="*57)
                print("\033[32m   > Metode Menghapus Menu <\n1. Menghapus Berdasarkan Index\n2. Menghapus Berdasarkan Item List\n\033[31m0. Kembali\033[39m")
                choice = str(input("Pilih Metode Menghapus Menu = "))
                if choice == "1" :
                    z = 1
                    while z > 0 :
                        print("="*57)
                        print("   > Menu Yang Dihapus <\n1. Minuman\n2. Makanan\n\033[31m0. Kembali\033[39m")
                        choice2 = str(input("Pilih Menu yang akan dihapus = "))
                        if choice2 == "1" :
                            print("="*57)
                            print("MENGHAPUS MENU MINUMAN")
                            deleteindexdrink()
                        if choice2 == "2" :
                            print("="*57)
                            print("MENGHAPUS MENU MAKANAN")
                            deleteindexfood()
                        elif choice2 == "0" :
                            z-=1
                elif choice == "2" :
                    a = 1
                    while a > 0 : 
                        print("="*57)
                        print("   > Menu Yang Dihapus <\n1. Minuman\n2. Makanan\n\033[31m0. Kembali\033[39m")
                        choice2 = str(input("Pilih Menu yang akan dihapus = "))
                        if choice2 == "1" :
                            print("="*57)
                            print("MENGHAPUS MENU MINUMAN")
                            itemdeletedrink()
                        if choice2 == "2" :
                            print("="*57)
                            print("MENGHAPUS MENU MAKANAN")
                            itemdeletefood()
                        elif choice2 == "0" :
                            a-=1
                else :
                    print("\033[31mMohon Ketik Pilihan Yang Tertera\033[39m")
            elif pilih2 == "3" :
                z = 1
                while z > 0 :
                    print("="*57)
                    print("   > Menu yang diubah <\n1. Minuman\n2. Makanan\n\033[31m0. Kembali\033[39m")
                    choice = str(input("Pilih Menu yang akan diubah = "))
                    if choice == "1":
                        print("="*57)
                        print("MENGUBAH MENU MINUMAN")
                        changedrink()
                    elif choice == "2" :
                        print("="*57)
                        print("MENGUBAH MENU MAKANAN")
                        changefood()
                    elif choice == "0" :
                        z-=1
                    else : 
                        print("\033[31mMohon Ketik Pilihan Yang Tertera\033[39m")
            else : 
                print("\033[31mMohon Ketik Pilihan Yang Tertera\033[39m")
    elif pilih == "0" :
        print("Program Berhenti")
        x-=1
    else :
        print("\033[31mMohon Ketik Pilihan Yang Tertera\033[39m")








