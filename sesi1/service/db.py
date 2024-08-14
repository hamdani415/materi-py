import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'lapak_hamdani'
)
def insert_item ( kode_barag,nama_barang,harga_barang, stok_barang):
    cursor = db.cursor()
    cursor.execute('INSERT INTO lapak_hamdani (kode_barang, nama_barang, harga_barang , stok_barang) VALUES(%s,%s,%s,%s)',  (kode_barag,nama_barang,harga_barang,stok_barang))
    db.commit()
    
    if cursor.rowcount> 0 :
        print ('data berhasil di simpan')
        
    else:
        print ('data gagal di masukan')
        
def fetch_item () :
    cursor = db.cursor()
    cursor.execute("SELECT * FROM lapak_hamdani")
    return cursor.fetchall()
    
