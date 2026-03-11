import random
import time

print("======================================================")
print(" DETEKTOR KŁAMSTW v2.0")
print("======================================================")
print("Odpowiadaj tylko: tak / nie")
print("System sprawdzi, czy mówisz prawdę...\n")

punkty_podejrzenia = 0

imie = input("Podaj swije imię: ")
print("\nWitaj,", imie + ".")
print("Uruchamiam skaner prawdy...")
time.sleep(1)

odp1 = input("\nCzy lubisz pizzę? ").lower()
if odp1 == "nie":
    punkty_podejrzenia += 1

odp2 = input("Czy lubisz spać? ").lower()
if odp2 == "nie":
    punkty_podejrzenia += 3

odp3 = input("Czy lubisz słodycze? ").lower()
if odp3 == "nie":
    punkty_podejrzenia += 1

odp4 = input("Czy lubisz pracować? ").lower()
if odp4 == "tak":
    punkty_podejrzenia += 6

odp5 = input("Czy jestes dziś w 100% grzeczna? ").lower()
if odp5 == "tak":
    punkty_podejrzenia += 4

odp6 = input("Czy zawsze mówisz prawdę? ").lower()
if odp6 == "tak":
    punkty_podejrzenia += 5

odp7 = input("Czy dziś wszystko jest dobrze? ").lower()
if odp7 == "nie":
    punkty_podejrzenia += 2

print("\nAnalizuję odpowiedzi...")
for i in range(0, 101, 20):
    print("Postęp skanowania:", i, "%")
    time.sleep(0.5)

procent = random.randint(35, 75) + punkty_podejrzenia * 3

if procent > 100:
    procent = 100

print("\n====================================================")
print(" WYNIK ANALIZY")
print("=====================================================")
print("Poziom podejrzanego zachowania:", procent, "%")

if procent <= 40:
    print("Wynik: Wygląda na to, że jesteś całkiem niewinna.")
    print("System nie wykrył większych kłamstw.")
elif procent <= 65:
    print("Wynik: Coś tu wygląda podejrzanie...")
    print("Możliwe drobne ukrywanie prawdy.")
elif procent <= 85:
    print("Wynik: Wysoki poziom podejrzeń!")
    print("System uważa, że cos kombinujesz")
else:
    print("WYNIK: KŁAMSTWO WYKRYTE!")
    print("System twierdzi, że jesteś bardzo podejrzana")

losowy_tekst = random.choice([
    "Skaner wykrył lekkie drgania podejrzanego zachowania.",
    "System zarejestrował dziwną energię odpowiedzi.",
    "Wykryto ślady kłamstwa.",
    "Poziom niewinności został zakwestionowany.",
    "Analiza zakończona. Wynik może byc totalnie losowy"
])

print("\nDowolny komentarz systemu:")
print(losowy_tekst)

print("\nDziękujemy za udział w teście,", imie + "!")
print("Koniec programu.")