#Nimmt die Anzahl der Kilometer als Argument, gibt den Preis in € zurück
def preisEntfernung(kilometer):
    return kilometer * 0.89

#Nimmt die Anzahl der Minuten als Argument, gibt den Preis in € zurück
def preisMinuten(minuten):
    return minuten * 0.21

print("""Mietart auswählen:
1 Abrechnung nach Strecke
2 Abrechnung nach Dauer""")
#Fragt Nutzer nach der Art der Miete
mietart = input("Mietart (1 oder 2): ")
print("")
#wird ausgeführt wenn nach Strecke abgerechnet werden soll
if mietart == "1":
    kilometer = float(input("Anzahl der Kilometer eingeben (z.B. 2.5): "))
    print(f"Die Fahrt kostete {preisEntfernung(kilometer)}€")
#wird ausgeführt, wenn nach Zeit abgerechnet werden soll
elif mietart == "2":
    minuten = float(input("Anzahl der Minuten eingeben (z.B. 2.5): "))
    print(f"Die Fahrt kostete {preisMinuten(minuten)}€")
#wird ausgeführt, wenn die Eingabe nicht 1 oder 2 ist
else:
    print("Ungültige Eingabe")