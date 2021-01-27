#naimportování knihoven (hashlib pro šifrování a datetime pro aktuální čas vytěženého bloku
import hashlib, json
from datetime import datetime

#zobrazení aktuálního času vytěženého bloku
print(datetime.now())

#defaultní konstruktor pro vlastní třídu Block
class Block:
    def __init__(self, previous_hash, data, nonce=0, index=0):

        #inicializace promennych, ktere vyuzivam z predchozich bloku
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = nonce
        self.index = index
        self.timestamp = datetime.now()

        #zabezpeci dlouhy string, ktery bude appendovat hashe za sebe
        string_to_hash = "".join(data) + previous_hash

        #data protahnu sha256 hashovaci funkci a prevedu na hexadecimalni hodnotu
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()

    def __str__(self):
        return str("Block #%s\nHash: %s\nNonce: %s" %(self.index,self.hash(),self.nonce))

"""
    def create_genesis_block():
        # Manualni vytvoreni genesis bloku - stanoveni indexu 0
        return Block(0, datetime.now(), "Genesis Block", "0")
    def next_block(last_block):
        this_index = last_block.index + 1
        this_timestamp = datetime.now()
        this_data = "Hey! I'm block #" + str(this_index)
        this_hash = last_block.hash
        return Block(this_index, this_timestamp, this_data, this_hash)
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]
    #zvoleni poctu bloku, ktere chci vytvorit
    num_of_blocks = 20
    #pridani jednotlivych bloku do blockchainu
    for i in range(0, num_of_blocks):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        # Tell everyone about it!
        print("Block #{}".format(block_to_add.index))
        print("Hash: {}\n".format(block_to_add.hash))
"""