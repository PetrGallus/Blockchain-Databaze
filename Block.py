#naimportování knihoven (hashlib pro šifrování a datetime pro aktuální čas vytěženého bloku
import hashlib
from datetime import datetime

#zobrazení aktuálního času vytěženého bloku
print(datetime.now())

#defaultní konstruktor pro vlastní třídu Block
class Block:
    def __init__(self, previous_hash, data, nonce=0, number=0):
        #inicializace promennych, ktere vyuzivam z predchozich bloku
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = nonce
        self.number = number
        self.timestamp = datetime.now()
        #zabezpeci dlouhy string, ktery bude appendovat hashe za sebe
        string_to_hash = "".join(data) + previous_hash
        #data protahnu sha256 hashovaci funkci a prevedu na hexadecimalni hodnotu
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()

    def __str__(self):
        return str("Block #%s\nHash: %s\nNonce: %s" %(self.number,self.hash(),self.nonce))
