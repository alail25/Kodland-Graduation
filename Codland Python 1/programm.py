import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = int(input("Masukkan panjang password: "))

password = ""

for i in range(length):
    password += random.choice(characters)

print("Password yang dihasilkan:", password)