"""
Program perulangan membaca buku dengan while
"""

jumlah_buku = 10
print('perintah ibu,"Baca semua bukumu"')
print("*" * 40)

jumlah_buku_yang_sudah_dibaca = 0
print(f"jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca} buku")
print("*" * 40)

while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
    print(f"jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca} buku")

print("*" * 40)
print(f"jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca} buku")







