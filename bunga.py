import sqlite3

# Koneksi ke database
conn = sqlite3.connect('database.db')

# Membuat tabel pengguna
conn.execute('''CREATE TABLE IF NOT EXISTS pengguna
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             NAMA TEXT NOT NULL,
             EMAIL TEXT NOT NULL UNIQUE,
             PASSWORD TEXT NOT NULL);''')

# Fungsi untuk menambahkan pengguna baru
def tambah_pengguna(nama, email, password):
    conn.execute("INSERT INTO pengguna (NAMA, EMAIL, PASSWORD) \
                  VALUES (?, ?, ?)", (nama, email, password))
    conn.commit()

# Formulir pendaftaran pengguna
nama = input("Masukkan nama lengkap: ")
email = input("Masukkan alamat email: ")
password = input("Masukkan password: ")

# Menambahkan pengguna baru ke database
tambah_pengguna(nama, email, password)

# Menampilkan pesan berhasil
print("Pendaftaran berhasil!")
