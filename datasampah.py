import pandas as pd

jabar_data = pd.read_csv("sampah.csv")
jabar_data.dropna(inplace=True)


df = pd.DataFrame(jabar_data)

# 2
total_tertentu = {}
for _,r in df.iterrows():
    tahun = r["tahun"]
    total = r["jumlah_produksi_sampah"]
    if tahun == 2015 :
        if tahun in total_tertentu :
            total_tertentu[tahun] += total
        else :
            total_tertentu[tahun] = total

for tahun, total in total_tertentu.items():
    print (f"Di tahun {tahun} sampah yang diproduksi di Jawa Barat adalah {total} ton")

data_tertentu = pd.DataFrame(list(total_tertentu.items()), columns=["tahun", "jumlah_produksi_sampah"])
data_tertentu.to_csv('tertentu.csv', index=False)
data_tertentu.to_excel('tertentu.xlsx', index=False)


# 3
total_pertahun = {}
for _,r in df.iterrows():
    tahun = r["tahun"]
    total = r["jumlah_produksi_sampah"]

    if tahun in total_pertahun :
        total_pertahun[tahun] += total
    else:
        total_pertahun[tahun] = total

for tahun, total in total_pertahun.items():
    print(f"Tahun {tahun} = {total} ton")

data_pertahun = pd.DataFrame(list(total_pertahun.items()), columns=["tahun", "jumlah_produksi_sampah"])
data_pertahun.to_csv('pertahun.csv', index=False)
data_pertahun.to_excel('pertahun.xlsx', index=False)

# 4
total_perkota_pertahun = {}
for _, r in df.iterrows():
    kota = r["nama_kabupaten_kota"]
    tahun = r["tahun"]
    jumlah = r["jumlah_produksi_sampah"]

    if tahun not in total_perkota_pertahun:
        total_perkota_pertahun[tahun] = {}
    
    if kota in total_perkota_pertahun[tahun]:
        total_perkota_pertahun[tahun][kota] += jumlah
    else:
        total_perkota_pertahun[tahun][kota] = jumlah


for tahun, data_kota in total_perkota_pertahun.items():
    print(f"Tahun {tahun}:")
    for kota, total in data_kota.items():
        print(f"  {kota}: {total} ton")

data_list = []
for tahun, data_kota in total_perkota_pertahun.items():
    for kota, total in data_kota.items():
        data_list.append({"tahun": tahun, "nama_kabupaten_kota": kota, "jumlah_produksi_sampah": total})

data_perkota_pertahun = pd.DataFrame(data_list)
data_perkota_pertahun.to_csv('perkota_pertahun.csv', index=False)
data_perkota_pertahun.to_excel('perkota_pertahun.xlsx', index=False)

# tambahan
total_perkota = {}
for _,r in df.iterrows():
    kota = r["nama_kabupaten_kota"]
    total = r["jumlah_produksi_sampah"]

    if kota in total_perkota :
        total_perkota[kota] += total
    else:
        total_perkota[kota] = total

for kota, total in total_perkota.items():
    print(f" {kota} = {total} ton")

data_perkota = pd.DataFrame(list(total_perkota.items()), columns=["nama_kabupaten_kota", "jumlah_produksi_sampah"])
data_perkota.to_csv('perkota.csv', index=False)
data_perkota.to_excel('perkota.xlsx', index=False)




