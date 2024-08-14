import main
from service import db

def add () :
    kode_barang = input ('kode barang :')
    nama_barang = input ('nama barang :')
    harga_barang = int(input ('harga barang :'))
    stok_barang = int(input ('stok barang :'))
    
    db.insert_item (kode_barang, nama_barang,harga_barang,stok_barang,)
    

def cek () :
    items = db.fetch_item()
    for item in items:
        kode_barang = item [0]
        nama_barang = item [1]
        harga_barang = item[2]
        stok_barang = item [3]
        print (f'''
kode : {kode_barang}
nama : {nama_barang}
harga : Rp. {harga_barang}
stok : {stok_barang}
''')
    
   
def mulai () : 
    while True :
        print ('\nini warung')
        menu= int(input ("1. tambah barang\n2. cek barang\n3. kembali\n\nsilahkan pilih : "))
        if menu == 1 :
            add()
        elif menu == 2 :
            cek()
        elif menu == 3 :
            main.menu()
       
        else : 
            break
    
    
if __name__ == '__main__' :
    mulai()