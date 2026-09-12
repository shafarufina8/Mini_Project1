Daftar_ekskul = [("Basket", "Rabu", "Pak Rudi"),("Badminton", "Sabtu", "Pak Dayat")]

while True:
    print("'MANAJEMEN EKSTRAKURIKULER'")
    print("1. Lihat Jadwal Ekskul")
    print("2. Tambah Ekskul Baru")
    print("3. Ubah Data Ekskul")
    print("4. Hapus Ekskul")
    print("5. Keluar")
    Pilihan = input("Masukkan pilihan menu (1-4): ")

    if Pilihan == "1":
        print("'JADWAL EKSTRAKURIKULER'")
        if not Daftar_ekskul:
            print("Belum ada ada jadwal ekskul")
        for i, e in enumerate(Daftar_ekskul, 1):
            print(f"{i}, Ekskul: {e[0]}, Hari: {e[1]}, Pembina: {e[2]}")

    elif Pilihan == "2":
        Nama = input("Nama ekskul: ")
        Hari = input("Hari ekskul: ")
        Pembina = input("Nama pembina: ")
        Daftar_ekskul.append((Nama, Hari, Pembina))
        print("Data ekskul berhasil ditambahkan!")

    elif Pilihan == "3":
        if len(Daftar_ekskul) == 0:
            print("Belum ada ekskul yang diubah")
        else:
            Pilihan_no = input("Masukkan nomor ekskul yang ingin diubah: ")
            if Pilihan_no.isdigit():
                no = int(Pilihan_no) - 1
                if 0 <= no < len(Daftar_ekskul):
                    Nama = input("Nama ekskul baru: ")
                    Hari = input("Hari ekskul baru: ")
                    Pembina = input("Nama pembina baru: ")

                    Daftar_ekskul[no] = (Nama, Hari, Pembina)
                    print("Data ekskul berhasil diubah!")
                else:
                    print("Nomor ekskul tidak ditemukan!")
            else:
                print("Harap masukkan angka!")

    elif Pilihan == "4":
        if not Daftar_ekskul:
            print("Belum ada ekskul yang bisa dihapus")
        else:
            Pilihan_no = input("Masukkan nomor ekskul: ")
            if Pilihan_no.isdigit():
                no = int(Pilihan_no) - 1
                if 0 <= no < len(Daftar_ekskul):
                    data_dihapus = Daftar_ekskul.pop(no)
                    print(f"Ekskul {data_dihapus[0]} berhasil dihapus!")
                else:
                    print("Nomor ekskul tidak ditemukan!")
            else:
                print("Harap masukkan angka")

    elif Pilihan == "5":
        print("Terima Kasih")
        break
    else:
        print("Pilihan tidak valid, silahkan coba lagi.")



