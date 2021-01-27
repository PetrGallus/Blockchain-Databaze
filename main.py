from Block import Block
from datetime import datetime

blockchain = []
mempool = []

#pro nasledne zobrazeni aktualniho casu ve formatu H:M:S:MS (milisekundy zaokrouhle na 3 mista)
now = datetime.now()
actual_time = now.strftime("%H:%M:%S.%f")[:-3]

#naplneni dat do jednotlivych bloku

genesis_block = Block("Univerzita Obrany", ["Foxtrot: 1. ceta je na pozici",
                                            "Alpha:   Pripravte se k provedeni lecky.",
                                            "Foxtrot: Rozumim, provedu"])

second_block = Block(genesis_block.block_hash, ["Foxtrot: Doslo ke kontaktu s nepritelem.",
                                                "Alpha:   Hlaste stav jednotky.",
                                                "Foxtrot: Dva zraneni, pozadujeme medevac."])

third_block = Block(second_block.block_hash, ["Rozkaz velitele 3. roty cislo 127 ze dne 1.4.2021..."])

fourth_block = Block(third_block.block_hash, ["Aktualni seznam osob s bezpecnostni proverkou stupne Tajne:..."])

fifth_block = Block(fourth_block.block_hash, ["Velitelem 7. ukoloveho uskupeni rotace Bravo..."])


#zobrazeni jednotlivych bloku spolecne s aktualnim casem a hashem - kazdy jednotlivy hash je zavisly na datech sveho predchoziho bloku
print("/Genesis Block\\")
print("Block hash: ",genesis_block.block_hash)
print("Time: ", actual_time)

print("\n/Block #2\\")
print("Block hash: ",second_block.block_hash)
print("Time: ", actual_time)

print("\n/Block #3\\")
print("Block hash: ",third_block.block_hash)
print("Time: ", actual_time)

print("\n/Block #4\\")
print("Block hash: ",fourth_block.block_hash)
print("Time: ", actual_time)

print("\n/Block #5\\")
print("Block hash: ",fifth_block.block_hash)
print("Time: ", actual_time)

#nefunguje
print("\n",Block)