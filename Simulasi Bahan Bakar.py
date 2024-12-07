def estimasi_bahan_bakar():
    print("=== Program Estimasi Pengeluaran Bahan Bakar ===")
    
    jarak = float(input("Masukkan jarak perjalanan (dalam kilometer): "))
    
    print("\n Jenis Kendaraan:")
    print("1. Motor")
    print("2. Mobil")
    print("3. Truk")
    jenis_kendaraan = int(input("Pilih jenis kendaraan (1/2/3): "))
    
    if jenis_kendaraan == 1:
        konsumsi_bbm = 40  
        saran_bensin = ["Pertalite", "Pertamax"]
    elif jenis_kendaraan == 2:
        konsumsi_bbm = 12  
        saran_bensin = ["Pertalite", "Pertamax Turbo"]
    elif jenis_kendaraan == 3:
        konsumsi_bbm = 8  # 
        saran_bensin = ["Solar", "Dexlite"]
    else:
        print("Pilihan kendaraan tidak valid! Default digunakan: Mobil.")
        konsumsi_bbm = 12  
        saran_bensin = ["Pertalite", "Pertamax Turbo"]

    bensin_dict = {
        "Pertalite": 10000,
        "Pertamax": 12400,
        "Pertamax Turbo": 13850,
        "Solar": 6800,
        "Dexlite": 13700
    }

    print("\n Jenis Bahan Bakar:")
    for i, jenis in enumerate(bensin_dict.keys(), 1):
        print(f"{i}. {jenis} (Rp {bensin_dict[jenis]:,}/liter)")
    jenis_bensin = int(input("Pilih jenis bahan bakar (1/2/3/4/5): "))
    nama_bbm = list(bensin_dict.keys())[jenis_bensin - 1] if 1 <= jenis_bensin <= 5 else "Pertalite"

    if nama_bbm not in saran_bensin:
        print(f"\nSaran bahan bakar untuk kendaraan Anda: {', '.join(saran_bensin)}")
        ganti_bbm = input(f"Apakah Anda ingin mengganti ke salah satu saran? (y/n): ").lower()
        if ganti_bbm == "y":
            print("\nPilih salah satu dari saran bahan bakar berikut:")
            for i, saran in enumerate(saran_bensin, 1):
                print(f"{i}. {saran} (Rp {bensin_dict[saran]:,}/liter)")
            saran_pilihan = int(input("Pilih bahan bakar (1/2): "))
            if 1 <= saran_pilihan <= len(saran_bensin):
                nama_bbm = saran_bensin[saran_pilihan - 1]
            else:
                print("Pilihan tidak valid, tetap menggunakan pilihan awal.")

    harga_bbm = bensin_dict[nama_bbm]
    
    kebutuhan_bbm = jarak / konsumsi_bbm
    total_biaya = kebutuhan_bbm * harga_bbm
    
    print("\n=== Estimasi Pengeluaran Bahan Bakar ===")
    print(f"Jenis kendaraan: {'Motor' if jenis_kendaraan == 1 else 'Mobil' if jenis_kendaraan == 2 else 'Truk'}")
    print(f"Jenis bahan bakar yang digunakan: {nama_bbm}")
    print(f"Konsumsi bahan bakar rata-rata: {konsumsi_bbm} km/liter")
    print(f"Kebutuhan bahan bakar: {kebutuhan_bbm:.2f} liter")
    print(f"Estimasi total biaya: Rp {total_biaya:,.2f}")

estimasi_bahan_bakar()
