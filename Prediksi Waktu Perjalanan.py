def prediksi_waktu_perjalanan():
    print("=== Prediksi Waktu Perjalanan ===")

    jarak = float(input("Masukkan jarak perjalanan (dalam kilometer): "))
    if jarak <= 0:
        print("Jarak tidak valid! Harus lebih besar dari 0.")
        return

    kecepatan_rata_rata = float(input("Masukkan kecepatan rata-rata kendaraan (dalam km/jam): "))
    if kecepatan_rata_rata <= 0:
        print("Kecepatan tidak valid! Harus lebih besar dari 0.")
        return

    jumlah_lampu_merah = int(input("Masukkan jumlah lampu merah di rute perjalanan: "))
    if jumlah_lampu_merah < 0:
        print("Jumlah lampu merah tidak valid! Harus 0 atau lebih.")
        return

    durasi_lampu_merah = float(input("Masukkan durasi rata-rata lampu merah (dalam detik): "))
    if durasi_lampu_merah < 0:
        print("Durasi lampu merah tidak valid! Harus 0 atau lebih.")
        return

    waktu_tempuh = jarak / kecepatan_rata_rata * 60  # waktu dalam menit
    waktu_berhenti_lampu_merah = jumlah_lampu_merah * (durasi_lampu_merah / 60)  # waktu dalam menit
    waktu_total = waktu_tempuh + waktu_berhenti_lampu_merah

    print("\n=== Hasil Prediksi Waktu Perjalanan ===")
    print(f"Jarak perjalanan: {jarak:.2f} km")
    print(f"Kecepatan rata-rata: {kecepatan_rata_rata:.2f} km/jam")
    print(f"Jumlah lampu merah: {jumlah_lampu_merah}")
    print(f"Durasi rata-rata lampu merah: {durasi_lampu_merah:.2f} detik")
    print(f"Waktu tempuh tanpa hambatan: {waktu_tempuh:.2f} menit")
    print(f"Waktu berhenti karena lampu merah: {waktu_berhenti_lampu_merah:.2f} menit")
    print(f"Waktu total perjalanan: {waktu_total:.2f} menit")
    print(f"Estimasi waktu total dalam jam: {waktu_total / 60:.2f} jam")

prediksi_waktu_perjalanan()
