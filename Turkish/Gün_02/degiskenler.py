# 30 Günlük python programlama
from operator import truediv


"""
ad = "Üçler"
print(type(ad))
soyad = "Gönültaş"
print(type(soyad))
tam_ad = "Üçler GÖnültaş"
print(len(tam_ad))
ulke = "Türkiye"
print(type(ulke))
sehir = "Ankara"
print(type(sehir))
yas = 25
print(type(yas))
yil = 1997
print(type(yil))
medeni_durum = True #evli ise true döner değilse false döner boolean veri tipi kullandık
print(type(medeni_durum))
is_true = False
print(type(is_true))
is_light_on = True
print(type(is_light_on))
"""

"""
#çoklu değişken bildirmek
a, b, c, d, e = 1, 2.0, "üçler", "a", "j+2"
print(a, b, c, d, e)

#adımızın ve soyadımızın uzunluğunu karşılaştıralım
print(len(ad), len(soyad)) # 5 e 8

sayi_1 = 5
sayi_2 = 4
print(sayi_1 + sayi_2)
print(sayi_2 - sayi_1)
print(sayi_1 * sayi_2)
print(sayi_1 / sayi_2)
print(sayi_2 // sayi_1)

print(sayi_1 ** sayi_2)
"""

#-------------çember-----------
# Çemberin Alanı πr²
# Çmeberin Çember 2πr

π = 3.14
r = 30
area_of_circle = (π * (r * r))
circum_of_circle = 2 * (π * r)
print(area_of_circle)
print(circum_of_circle)

#------------KULLANICI KISMI--------------

ad = input("İsminizi Girin:")
print(ad)
soyad = input("Soyadınızı Girin:")
print(soyad)
ulke = input("Ülkenizi Girin:")
print(ulke)
yas = input("yaşınızı Girin:")
print(yas)

