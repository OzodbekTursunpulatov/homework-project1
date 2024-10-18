# Foydalanuvchidan ma'lumotlarni olishBu dastur foydalanuvchidan zarur ma'lumotlarni olib,
#  har bir transport turiga sarflanadigan mablag'ni hisoblab chiqadi
#  va qaysi transportdan foydalanishi mumkinligini ko'rsatadi.

pul = float(input("Sizda qancha pul bor?:  "))
km = float(input(" (km) qancha?:  "))
taxi_narxi = float(input("Taxi narxi  qancha?:  "))
avtobus_narxi = float(input("Avtobus narxi qancha?:  "))
nechta_avtobus = int(input("Nechta avtobusda ketasiz?:  "))
metro_narxi = float(input("Metro narxi qancha?:  "))

taxi_xarajat = km * taxi_narxi
avtobus_xarajat = avtobus_narxi * nechta_avtobus
metro_xarajat = metro_narxi

print("\nSizning mablag'ingiz: ", pul)
if pul >= taxi_xarajat:
    print("Siz taxi bilan borishingiz mumkin.")
else:
    print("Taxi uchun mablag'ingiz yetmaydi.")

if pul >= avtobus_xarajat:
    print("Siz avtobus bilan borishingiz mumkin.")
else:
    print("Avtobus uchun mablag'ingiz yetmaydi.")

if pul >= metro_xarajat:
    print("Siz metro bilan borishingiz mumkin.")
else:
    print("Metro uchun mablag'ingiz yetmaydi.")
