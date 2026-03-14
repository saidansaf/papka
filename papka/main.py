matn = input("Matn kiriting: ")

with open("matn.txt", "w", encoding="utf-8") as f:
    f.write(matn)

print("1-vazifa bajarildi: Matn faylga yozildi")

with open("matn.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("2-vazifa natijasi:", text.upper())

with open("qatorlar.txt", "w", encoding="utf-8") as f:
    for i in range(1, 6):
        f.write(f"Qator {i}\n")

with open("qatorlar.txt", "r", encoding="utf-8") as f:
    qatorlar = f.readlines()

print("3-vazifa natijasi:", qatorlar)

with open("matn.txt", "r", encoding="utf-8") as f:
    words = f.read().split()

print("4-vazifa natijasi:")
for word in words:
    if len(word) > 5:
        print(word)

with open("matn.txt", "a", encoding="utf-8") as f:
    f.write("\nYangi qoshilgan malumot")

with open("matn.txt", "r", encoding="utf-8") as f:
    yangi = f.read()

print("5-vazifa natijasi:")
print(yangi)