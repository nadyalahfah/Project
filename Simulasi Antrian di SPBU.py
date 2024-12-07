def simulasi_antrian_spbu():
    print("=== Simulasi Antrian di SPBU ===")

    jumlah_pompa = int(input("Masukkan jumlah pompa bahan bakar di SPBU: "))
    if jumlah_pompa <= 0:
        print("Jumlah pompa tidak valid! Default digunakan: 1 pompa.")
        jumlah_pompa = 1

    jumlah_kendaraan = int(input("Masukkan jumlah kendaraan yang mengantre: "))
    if jumlah_kendaraan <= 0:
        print("Jumlah kendaraan tidak valid! Default digunakan: 1 kendaraan.")
        jumlah_kendaraan = 1

    waktu_per_kendaraan = float(input("Masukkan waktu rata-rata pengisian bahan bakar per kendaraan (dalam menit): "))
    if waktu_per_kendaraan <= 0:
        print("Waktu rata-rata tidak valid! Default digunakan: 5 menit per kendaraan.")
        waktu_per_kendaraan = 5

    kendaraan_per_pompa = jumlah_kendaraan / jumlah_pompa
    waktu_total = kendaraan_per_pompa * waktu_per_kendaraan

    print("\n=== Hasil Simulasi ===")
    print(f"Jumlah pompa bahan bakar: {jumlah_pompa}")
    print(f"Jumlah kendaraan mengantre: {jumlah_kendaraan}")
    print(f"Waktu rata-rata pengisian per kendaraan: {waktu_per_kendaraan:.2f} menit")
    print(f"Waktu total hingga semua kendaraan selesai: {waktu_total:.2f} menit")
    print(f"Estimasi rata-rata waktu tunggu per kendaraan: {waktu_total / jumlah_kendaraan:.2f} menit")

simulasi_antrian_spbu()
