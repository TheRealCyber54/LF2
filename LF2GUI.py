from cgitb import text
import tkinter as tk

#GUI nachfolgend Elemente
window = tk.Tk()

#Variablen
art= tk.IntVar()
art.set(1)
ErgebnisString = tk.StringVar()
Ergebnis = 0

#Nimmt die Anzahl der Kilometer als Argument, gibt den Preis in € zurück
def preisEntfernung(kilometer):
    return kilometer * 0.89

#Nimmt die Anzahl der Minuten als Argument, gibt den Preis in € zurück
def preisMinuten(minuten):
    return minuten * 0.21

#Auswahl aus welcher Berechnungsmethode

def AuswahlMethode():
    if art.get()==1: 
        Ergebnis=preisEntfernung(float(text_box_wert.get(1.0, "end-1c")))
    else:
        Ergebnis=preisMinuten(float(text_box_wert.get(1.0, "end-1c")))
    print(Ergebnis)
    ErgebnisString.set(str(Ergebnis))


#GUI Frage
frage1 = tk.Label(text="Berrechnung über Strecke oder Dauer?")
frage1.pack()

#GUI Element Auswahl der Methode
tk.Radiobutton(window, 
            text="Dauer",
            variable=art, 
            value=2).pack()
tk.Radiobutton(window, 
            text="Strecke",
            variable=art, 
            value=1).pack()


frage2= tk.Label(text="Bitte den Wert eingeben(Distanz in Km und Dauer in Min)")
frage2.pack() 

text_box_wert = tk.Text(window,height=2, width=10)
text_box_wert.pack()

tk.Button(window, text="Berechnen", command=AuswahlMethode).pack()

Antwortfeld= tk.Label(text="Ergebnis in Euro:")
Antwortfeld.pack() 

antwort= tk.Label(textvariable=ErgebnisString)
antwort.pack()


window.mainloop()