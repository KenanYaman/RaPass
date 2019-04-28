import random
import string
import time


password = ""
print("Rastgele şifre oluşturma uygulaması")
harf = input("Parola içerisinde Harf olsun mu ? [e/h]")
sayi = input("Parola içerisinde Sayı olsun mu ? [e/h]")
ozel = input("Parola içerisinde Özel Karakter olsun mu ? [e/h]")
karakter = int(input("Şifre kaç karakterden oluşacak ?"))

if harf == "e":
    password += string.ascii_letters
else:
    pass

if sayi == "e":
    password += str(string.digits)
else:
    pass

if ozel == "e":
    password += string.punctuation
else:
    pass

print("şifre oluşturuluyor...")
time.sleep(1)

print(''.join(random.choice(password) for i in range(karakter)))
