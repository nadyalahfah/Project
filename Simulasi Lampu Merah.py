def hitung_kendaraan():
    print("===== Program Penghitung Jumlah Kendaraan Saat Lampu Merah =====")
    
    panjang_jalan = float(input("Masukkan panjang jalan (dalam meter): "))
    lebar_jalan = float(input("Masukkan lebar jalan (dalam meter): "))
    
    durasi = float(input("Masukkan durasi lampu merah (dalam menit): "))
    if durasi <= 0:
        print("Durasi lampu merah tidak valid! Gunakan nilai default 0.5 menit.")
        durasi = 0.5

    # Dimensi rata-rata kendaraan (dalam meter) dimana terdapata panjang dan lebar
    dimensi_kendaraan = {
        "mobil": (4.5, 2.0),  
        "motor": (2.0, 0.8),
        "truk": (8.0, 2.5),
        "bus": (10.0, 2.5)
    }

    luas_jalan = panjang_jalan * lebar_jalan
    print(f"Luas jalan: {luas_jalan} m²")

    jumlah_kendaraan = {}
    for jenis, dimensi in dimensi_kendaraan.items():
        luas_kendaraan = dimensi[0] * dimensi[1]
        jumlah_kendaraan[jenis] = int(luas_jalan / luas_kendaraan)
    
    print("\n Estimasi jumlah kendaraan yang dapat tertampung:")
    for jenis, jumlah in jumlah_kendaraan.items():
        print(f"{jenis.capitalize()}: {jumlah} kendaraan")
    
    print(f"\nDurasi lampu merah: {durasi} menit")
    total_kendaraan = sum(jumlah_kendaraan.values())
    rata_rata_berhenti = total_kendaraan * durasi / 10  # asumsi perhitungan tambahan
    print(f"Rata-rata kendaraan berhenti selama {durasi} menit: {rata_rata_berhenti:.2f} kendaraan")

hitung_kendaraan()
