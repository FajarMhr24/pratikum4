# Praktikum 4 - Data List

NAMA : FAJAR MAHER HABIBILLAH

NIM : 312410549

KELAS : TI.24.A5

## penjelasan kode program

```
nilai_data = []
```
- Variabel `nilai_data` adalah sebuah list kosong yang akan digunakan untuk menyimpan data mahasiswa berupa dictionary.

### input data
```
nama = input("Masukkan nama anda: ")
nim = input("Masukkan NIM anda: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))
```

- `input` digunakan untuk meminta pengguna memasukkan data:
  - `nama` : nama mahasiswa
  - `nim`  : NIM mahasiswa
  -  `tugas`, `uts`, `uas`: nilai tugas, UTS, dan UAS yang diubah menjadi tipe float untuk perhitungan

### Menghitung nilai akhir 

```
nilai_akhir = (tugas * 3 + uts * 3.5 + uas * 3.5) / 10
```

- Rumus untuk menghitung nilai akhir:
    - Bobot nilai:
    - Tugas: 30% (0.3 atau 3/10)
    - UTS: 35% (0.35 atau 3.5/10)
    - UAS: 35% (0.35 atau 3.5/10)
    - Nilai akhir dihitung dengan formula berbobot:
    - nilai_akhir
    nilai_akhir= 
    10
    (tugas×3)+(uts×3.5)+(uas×3.5)

### Menyimpan data
```
data_mahasiswa = {
    "nama": nama,
    "nim": nim,
    "tugas": tugas,
    "uts": uts,
    "uas": uas,
    "nilai_akhir": nilai_akhir
}
nilai_data.append(data_mahasiswa)
```

- Data setiap mahasiswa disimpan dalam bentuk dictionary:
  -`nama`, `nim`, `tugas`, `uts`, `uas`, dan `nilai_akhir`.
  - Kemudian, dictionary tersebut ditambahkan ke dalam list `nilai_data` menggunakan `append`.

 ### Cek perulangan

 ```
tambah_data = input("Tambah Data Lagi? (y/t): ").lower()
if tambah_data == 't':
    break
```
- Pengguna diminta untuk memilih apakah ingin menambahkan data lagi:
    - Jika `y`1, perulangan akan berlanjut.
    - Jika `t`, perulangan dihentikan menggunakan `break`.

### Header tabel
```
print("No | Nama\t|    NIM    | Tugas | UTS | UAS |  Nilai Akhir |")
print("=" * 64)
```
- Menampilkan header tabel dan garis pemisah.

### Menampilkan data 

```
for i, data in enumerate(nilai_data, start=1):
    print(f"{i}  | {data['nama']}\t| {data['nim']} | {data['tugas']}  | {data['uts']}| {data['uas']}| {data['nilai_akhir']:.2f}        |")
```
`for` digunakan untuk iterasi setiap data mahasiswa dalam `nilai_data`.
`enumerate` memberikan indeks (dimulai dari 1).
F-string digunakan untuk memformat tampilan data, termasuk pembulatan nilai akhir ke 2 desimal menggunakan `:.2f`.

###  footer tabel
```
print("=" * 64)
```
- Menambahkan garis pemisah akhir tabel.

## Flowchar

![foto](https://github.com/FajarMhr24/flochart/blob/eef2ad011054e6f13cdd35e917e4349b67155329/Screenshot%202024-11-14%20200537.png)

## output

![foto](https://github.com/FajarMhr24/foto/blob/3c903c3a53a4ee32a84e622baeeaaac329d12e50/Screenshot%202024-11-14%20201753.png)

​
 

