nilai_data = []

while True:
    nama = input("Masukkan nama anda: ")
    nim = input("Masukkan NIM anda: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    
    nilai_akhir = (tugas * 3 + uts * 3.5 + uas * 3.5) / 10
    
    data_mahasiswa = {
        "nama": nama,
        "nim": nim,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir
    }
    nilai_data.append(data_mahasiswa)
    
    tambah_data = input("Tambah Data Lagi? (y/t): ").lower()
    if tambah_data == 't':
        break
    
print("No | Nama\t|    NIM    | Tugas | UTS | UAS |  Nilai Akhir |")
print("=" * 64)
for i, data in enumerate(nilai_data, start=1):
    print(f"{i}  | {data['nama']}\t| {data['nim']} | {data['tugas']}  | {data['uts']}| {data['uas']}| {data['nilai_akhir']:.2f}        |")
print("=" * 64)
