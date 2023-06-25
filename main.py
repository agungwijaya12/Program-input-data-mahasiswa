import pandas as pd
import json
from os import system

filename = "database.json"


def judul():
    print('=====================================')
    print('|    PROGRAM INPUT DATA MAHASISWA   |')
    print('=====================================')


def dosen():
    system('cls')
    print('=====================================')
    print('|               Login               |')
    print('=====================================')
    print('Masukkan kode Login')
    print('\n')
    kode = input('Masuk : ')
    if kode == 'admin' or kode == 'ADMIN':
        menu_dosen()
    else:
        salah = input('Kode salah')
        dosen()


def menu_dosen():
    system('cls')
    print('=====================================')
    print('Input Data Nilai Mahasiswa'.center(40))
    print('=====================================')
    print('| 1. Tambah Data Mahasiswa          |')
    print('| 2. Lihat Data Mahasiswa           |')
    print('| 3. Ubah Data Mahasiswa            |')
    print('| 4. Hapus Data Mahasiswa           |')
    print('| 5. Selesai                        |')
    print('=====================================')
    pilih2 = input('Pilih Menu : ')
    if pilih2 == '1':
        tambah()
    elif pilih2 == '2':
        lihat()
    elif pilih2 == '3':
        ubah()
    elif pilih2 == '4':
        hapus()
    elif pilih2 == '5':
        selesai()
    else:
        tidak = input('Menu Tidak Ada ')
        system('cls')
        menu_dosen()


def tambah():
    system('cls')
    judul()
    print('Tambah Data Mahasiswa'.center(40))
    print('=====================================')
    with open(filename, "r") as f:
        temp = json.load(f)
    item_data = {}
    item_data["Nim"] = input('Masukkan Nim: ')
    item_data["Nama"] = input('Masukkan nama: ')
    item_data["Jurusan"] = input('Masukkan Jurusan: ')
    item_data["Kelas"] = input('Masukkan Kelas: ')
    item_data["Uts"] = input('Masukkan nilai Uts: ')
    item_data["Uas"] = input('Masukkan nilai Uas: ')
    temp.append(item_data)
    with open (filename, "w") as f:
        json.dump(temp, f, indent=4)
    print('INI ADALAH DAFTAR HASIL TAMBAH DATA MAHASISWA')
    df = pd.read_json("database.json")
    print(df)
    pertanyaan = input('Apakah masih ingin menambah data mahasiswa :[Y/N] ')
    while pertanyaan != 'N':
        tambah()
    kembali = input('Tekan enter untuk kembali [enter]')
    menu_dosen()


def view():
    system('cls')
    judul()
    df = pd.read_json("database.json")
    print(df)


def ubah():
    system('cls')
    print('Ubah Data Mahasiswa'.center(40))
    print('=====================================')
    judul()
    view()
    new_data = []
    with open(filename, "r") as f:
        temp = json.load(f)
        data_length = len(temp)-1
    print('*tekan [Enter] untuk kembali*')
    ubah_data = input(f'Pilih nomor yang ingin diubah 0-{data_length}: ')
    if ubah_data == '':
        menu_dosen()
    i= 0
    for entry in temp:
        if i == int(ubah_data):
            print('''
            nama - ubah nama
            nim - ubah nim
            jurusan - ubah jurusan
            kelas - ubah kode kelas
            uts - ubah nilai uts
            uas - ubah nilai uas
            all - ubah semua data\n''')
            pertanyaan = input('Apa yang ingin anda rubah? : ')
            nama = entry["Nama"]
            nim = entry["Nim"]
            jurusan = entry["Jurusan"]
            kelas = entry["Kelas"]
            uts = entry["Uts"]
            uas = entry["Uas"]

            if pertanyaan == 'nama':
                nama = input('Masukkan nama baru : ')
            elif pertanyaan == 'nim':
                nim = input('Masukkan Nim baru : ')
            elif pertanyaan == 'jurusan':
                jurusan = input('Masukkan jurusan baru : ')
            elif pertanyaan == 'kelas':
                kelas = input('Masukkan kode kelas baru : ')
            elif pertanyaan == 'uts':
                uts = input('Masukkan nilai uts baru : ')
            elif pertanyaan == 'uas':
                uas = input('Masukkan nilai uas baru : ')
            elif pertanyaan == 'all':
                nim = input('Masukkan Nim baru : ')
                nama = input('Masukkan nama baru : ')
                jurusan = input('Masukkan jurusan baru : ')
                kelas = input('Masukkan kode kelas baru : ')
                uts = input('Masukkan nilai uts baru : ')
                uas = input('Masukkan nilai uas baru : ')
            else:    
                print('Masukkan sesuai keyword yang tersedia\n')
                a = input('Tekan enter untuk melanjutkan [ENTER]')
                
                ubah()
        
            new_data.append({ "Nim":nim,"Nama": nama, "Jurusan": jurusan, "Kelas": kelas,"Uts": uts, "Uas": uas})
            i = i+1
        else:
            new_data.append(entry)
            i = i+1
    with open (filename, "w") as f:
        json.dump(new_data, f, indent=4)
    system('cls')
    print('INI ADALAH DAFTAR HASIL UPDATE DATA MAHASISWA')
    df = pd.read_json("database.json")
    print(df)
    pertanyaan = input('Apakah ingin mengubah data lagi?[Y/N]')
    while pertanyaan != 'N':
        ubah()
    a = input('Tekan enter untuk kembali [ENTER]')
    menu_dosen()
    

def hapus():
    system('cls')
    judul()
    print('Penghapusan Data Mahasiswa'.center(40))
    print('=====================================')
    view()
    new_data = []
    with open(filename, "r") as f:
        temp = json.load(f)
        data_length = len(temp)-1
    hapus_data = input('Masukkan nomor untuk hapus: ')
    y = 0
    for entry in temp:
        if y == int(hapus_data):
            pass
            y=y+1
        else:
            new_data.append(entry)
            y=y+1
    with open (filename, "w") as f:
        json.dump(new_data, f, indent=4)
        print('INI ADALAH DAFTAR HASIL HAPUS DATA MAHASISWA')
    df = pd.read_json("database.json")
    print(df)
    a = input('Tekan enter untuk kembali [ENTER]')
    menu_dosen()
        

def lihat():
    system('cls')
    print('DATA MAHASISWA'.center(40))
    print('================================================================================')
    df = pd.read_json("database.json")
    print(df)

    a = input('Tekan enter untuk kembali [ENTER]')
    menu_dosen()


def selesai():
    exit

dosen()
