class Browser:
    def pencarian(self):
        pass

class Chrome(Browser):
    def pencarian(self):
        return "Chrome lebih cepat dalam menjalankan laman web berat dan aplikasi berbasis web"

class Firefox(Browser):
    def pencarian(self):
        return "Firefox lebih lambat dibandingkan chrome dalam beberapa kasus, tetapi optimal untuk penggunaan sehari-hari"

class Factory:
    @staticmethod
    def buat_produk(jenis_produk):
        if jenis_produk == "Chrome":
            return Chrome()
        elif jenis_produk == "Firefox":
            return Firefox()
        else:
            raise ValueError("Pencarian ini tidak diketahui")
        
# Penggunaan Factory Pattern
produk1 = Factory.buat_produk("Chrome")
print(produk1.pencarian())
produk2 = Factory.buat_produk("Firefox")
print(produk2.pencarian())


