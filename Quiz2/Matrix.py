# F55123044_I Wayan Arigayu Saputra
# Cara 1: Menggunakan NumPy
import numpy as np

def hitung_dengan_numpy():
    A = np.array([[2, 0, -3], [1, 4, 5]])
    B = np.array([[3, 1], [-1, 0], [4, 2]])
    C = np.array([[4, 7], [2, 1], [1, -1]])

    # Menghitung AB dan AC
    AB = np.dot(A, B)
    AC = np.dot(A, C)

    # Menghitung AB + AC
    hasil = AB + AC
    return hasil

# Cara 2: Tanpa Menggunakan NumPy
def perkalian_matriks(A, B):
    # A: m x n, B: n x p, hasil akan berupa matriks m x p
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    hasil = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                hasil[i][j] += A[i][k] * B[k][j]
    return hasil

def penjumlahan_matriks(X, Y):
    # X dan Y harus memiliki ukuran yang sama
    m = len(X)
    n = len(X[0])
    hasil = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            hasil[i][j] = X[i][j] + Y[i][j]
    return hasil

def hitung_tanpa_numpy():
    A = [[2, 0, -3], [1, 4, 5]]
    B = [[3, 1], [-1, 0], [4, 2]]
    C = [[4, 7], [2, 1], [1, -1]]

    # Menghitung AB dan AC
    AB = perkalian_matriks(A, B)
    AC = perkalian_matriks(A, C)

    # Menghitung AB + AC
    hasil = penjumlahan_matriks(AB, AC)
    return hasil

# Menampilkan hasil
print("Hasil dengan NumPy:")
print(hitung_dengan_numpy())

print("\nHasil tanpa NumPy:")
print(hitung_tanpa_numpy())