# Array x dengan 10 elemen
x = [3, 6, 8, 11, 14, 17, 20, 23, 26, 29]

# Meminta input angka dari pengguna
y = int(input("Masukkan angka untuk y1: "))

# Logika untuk mengecek keberadaan y1 di dalam x
if y in x:
    index = x.index(y)  # Mencari indeks di mana y ditemukan dalam array
    if y % 2 == 0:
        print(f"{y} adalah genap dan ada di dalam array pada indeks {index}.")
    else:
        print(f"{y} ada di dalam array pada indeks {index}, tetapi bukan genap.")
else:
    print("Variabel tidak ada dalam array.")
6