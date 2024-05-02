#DAFTAR BARANG BESERTA HAGANYA
print("|===================================|")
print("|== DAFTAR BARANG BESERTA HARGANYA ==|")
print("|===================================|")
Daftar_barang = {
    "Beras":10000,
    "Gula":8000,
    "Telur":2000,
    "Minyak goreng":15000,
    "Garam":5000,
}

# MENAMPLKAN NAMA BARANG

print(f"Daftar barang:")
for  barang, harga in Daftar_barang.items():
    print(f"{barang}:Rp {harga}")
    
#INPUT JUMLAH BARANG YANG DI BELI

total_belanja=0
jumlah_barang=int(input("Masukan jumlah barang yang ingin di beli:"))

#MENGHITUANG TOTAL BELNJA

for i in range (jumlah_barang):
    barang = input(f"Masukan nama barang ke {i+1}:")
    if barang in Daftar_barang:
        total_belanja += Daftar_barang[barang]
    else:
        print(f"{barang}tidak ada dalam Daftar barang.")
        
#MENAMPILKN TOTAL BELANJA

print(f"\ntotal belanja anda adalah{total_belanja}:")
        