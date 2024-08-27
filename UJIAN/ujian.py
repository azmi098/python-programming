jumlah_siswa = int(input("masukan jumlah siswa"))

for i in range (jumlah_siswa):
    nilai_tugas1 = int(input("Masukkan nilai tugas 1: ")):
    nilai_tugas2 = int(input("Masukkan nilai tugas 2: ")):
    nilai_tugas3 = int(input("Masukkan nilai tugas 3: ")):

rata_rata_nilai = (nilai_tugas1 + nilai_tugas2 + nilai_tugas3) / 3

if rata_rata_nilai >= 70:
    print ("Lulus")
elif rata_rata_nilai >= 50 and rata_rata_nilai < 70:
    print ("Perbaikan")
else:
    print ("Tidak Lulus")

