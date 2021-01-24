from Block import Block

blockchain = []
mempool = []

genesis_block = Block ("Univerzita Obrany", ["3. ceta je na pozici",
                                             "Pripravte se k provedeni lecky.",
                                             "Rozumim, provedu"])

second_block = Block(genesis_block.block_hash, ["Doslo ke kontaktu s nepritelem.",
                                                "Hlaste stav jednotky.",
                                                "Dva zraneni, pozadujeme podporu."])

third_block = Block(second_block.block_hash, ["Rozkaz velitele 3. roty cislo 127 ze dne...",
                                              "Seznam osob s bezpecnostni proverkou stupne Tajne:...",
                                              "Velitelem 7. ukoloveho uskupeni rotace Bravo..."])

print("/Genesis Block\\")
print("Block hash: ",genesis_block.block_hash)

print("\n/Second Block\\")
print("Block hash: ",second_block.block_hash)

print("\n/Third Block\\")
print("Block hash: ",third_block.block_hash)

#nefunguje
print(Block)
