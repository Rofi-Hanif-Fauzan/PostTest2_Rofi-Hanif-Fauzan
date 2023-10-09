# Nama: Rofi Hanif Fauzan
# NIM: 2309116026


# Menambahkan modul PrettyTable
from prettytable import PrettyTable

# Tabel parfum
tabel_parfum = PrettyTable()
tabel_parfum.field_names = ["Nomor", "Nama Parfum", "Kapasitas (ml)", "Harga (Rp)"]

# Data parfum
data_parfum = [
    ["HMNS", 50, 250000],
    ["Labcitane", 120, 185000],
    ["Oullu", 150, 390000],
    ["Onix Fragrance", 60, 200000],
    ["Daze Delacour", 80, 315000],
    ["Euodia Parfums", 80, 350000],
    ["The Living Potion by KIEV", 100, 135000],
    ["Wardah Eau de Toilette", 50, 100000],
    ["Morris", 120, 50000],
    ["Scentcode", 100, 132000]
]

# Fungsi menampilkan tabel
def show_table():
    print(tabel_parfum)

# Menambahkan data parfum ke tabel
for nomor, parfum in enumerate(data_parfum, start=1):
    tabel_parfum.add_row([nomor] + parfum)

# Fungsi menambahkan data
def create_data(nama, kapasitas, harga):
    global data_parfum
    nomor = len(data_parfum) + 1
    data_parfum.append([nama, kapasitas, harga])
    tabel_parfum.add_row([nomor, nama, kapasitas, harga])

# Fungsi memperbarui data
def update_data(nomor, nama, kapasitas, harga):
    for idx, row in enumerate(data_parfum):
        if idx + 1 == nomor:
            row[0] = nama
            row[1] = kapasitas
            row[2] = harga
            break

    for row in tabel_parfum.rows:
        if int(row[0]) == nomor:
            row[1] = nama
            row[2] = kapasitas
            row[3] = harga
            break

# Fungsi menghapus data
def delete_data(nomor):
    global data_parfum
    data_parfum = [row for idx, row in enumerate(data_parfum, start=1) if idx != nomor]

    # Hapus baris di tabel
    tabel_parfum.clear_rows()

    for idx, parfum in enumerate(data_parfum, start=1):
        tabel_parfum.add_row([idx] + parfum)

# Role Admin
def admin_role():
    while True:
        print("\nMenu Admin:")
        print("1. Tambahkan data")
        print("2. Tampilkan data")
        print("3. Perbarui data")
        print("4. Hapus data")
        print("5. Keluar")
        pilihan = int(input("Pilih perintah: "))

        if pilihan == 1:
            nama = input("Masukkan nama parfum: ")
            kapasitas = int(input("Masukkan kapasitas parfum (ml): "))
            harga = int(input("Masukkan harga parfum (Rp): "))
            create_data(nama, kapasitas, harga)
        elif pilihan == 2:
            show_table()
        elif pilihan == 3:
            nomor = int(input("Masukkan nomor parfum yang ingin diupdate: "))
            nama = input("Masukkan nama parfum baru: ")
            kapasitas = int(input("Masukkan kapasitas parfum baru (ml): "))
            harga = int(input("Masukkan harga parfum baru (Rp): "))
            update_data(nomor, nama, kapasitas, harga)
        elif pilihan == 4:
            nomor = int(input("Masukkan nomor parfum yang ingin dihapus: "))
            delete_data(nomor)
        elif pilihan == 5:
            break
        else:
            print("Pilihan tidak valid. Silahkan dicoba lagi.")

# Fungsi untuk melakukan transaksi pembelian parfum
def buy_parfume():
    show_table()
    print("Selamat datang di Toko Parfum Rofi99")
    print("-"*15)
    nomor = int(input("Masukkan nomor parfum yang ingin dibeli: "))

    for idx, row in enumerate(data_parfum, start=1):
        if idx == nomor:
            harga = row[2]
            break
    else:
        print("Nomor parfum tidak valid.")
        return

    uang = int(input(f"Masukkan jumlah uang Anda (Rp {harga}): "))

    if uang >= harga:
        kembalian = uang - harga
        print(f"Terimakasih sudah membeli! Ini uang kembalian Anda: Rp {kembalian}.")
    else:
        print("Uang Anda tidak cukup.")

# Role Pembeli
def buyer_role():
    while True:
        print("\nMenu Pembeli:")
        print("1. Beli Parfum")
        print("2. Keluar")
        pilihan = int(input("Pilih perintah: "))

        if pilihan == 1:
            buy_parfume()
        elif pilihan == 2:
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Program utama
while True:
    print("\nMenu Utama:")
    print("1. Admin")
    print("2. Pembeli")
    print("3. Keluar")
    role = int(input("Pilih role: "))

    if role == 1:
        admin_role()
    elif role == 2:
        buyer_role()
    elif role == 3:
        break
    else:
        print("Peran tidak valid. Silakan coba lagi.")
