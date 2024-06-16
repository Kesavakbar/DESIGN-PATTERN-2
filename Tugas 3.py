class BumbuDapur:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._bumbu_list = []
        return cls._instance
    
    def tambah_bumbu(self, bumbu):
        self._bumbu_list.append(bumbu)
    
    def daftar_bumbu(self):
        return self._bumbu_list

if __name__ == "__main__":
    dapur = BumbuDapur()
    dapur.tambah_bumbu("Garam")
    dapur.tambah_bumbu("Lada")
    dapur.tambah_bumbu("Kunyit")
    
   
    dapur_lain = BumbuDapur()
    dapur_lain.tambah_bumbu("Jahe")
    
    print("Bumbu di dapur:")
    print(dapur.daftar_bumbu())
    print("Bumbu di dapur lain:")
    print(dapur_lain.daftar_bumbu())
