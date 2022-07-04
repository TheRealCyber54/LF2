from cgitb import text
import tkinter as tk
import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="lernfeld"
)

my_cursor = my_db.cursor()
my_cursor.execute("SHOW TABLES")

for db in my_cursor:
    print(db)


#GUI nachfolgend Elemente
window = tk.Tk()

#Variablen
art= tk.IntVar()
art.set(1)
ErgebnisString = tk.StringVar()
Ergebnis = 0


#Nimmt die Anzahl der Kilometer als Argument, gibt den Preis in € zurück
def preisEntfernung(kilometer):
    kosten = kilometer * 0.89
    insert_strecke(kilometer, kosten)
    show_all_data_strecke()
    return kosten


#Nimmt die Anzahl der Minuten als Argument, gibt den Preis in € zurück
def preisMinuten(minuten):
    kosten = minuten * 0.21
    insert_dauer(minuten, kosten)
    show_all_data_dauer()
    return kosten



def insert_strecke(distance, preis):

    val = (f"{distance}", f"{preis}")
    sql = f'INSERT INTO strecke(strecke, preis) VALUES(%s,%s)'
    my_cursor.execute(sql, val)
    my_db.commit()


def insert_dauer(zeit, preis):

    val = (f"{zeit}", f"{preis}")
    sql = f'INSERT INTO dauer(dauer, preis) VALUES(%s,%s)'
    my_cursor.execute(sql, val)
    my_db.commit()


def show_all_data_dauer():
    my_cursor.execute("SELECT * FROM dauer")
    result = my_cursor.fetchall()

    for _ in result:
        print(_)


def show_all_data_strecke():
    my_cursor.execute("SELECT * FROM strecke")
    result = my_cursor.fetchall()

    for _ in result:
        print(_)




#Auswahl aus welcher Berechnungsmethode

def AuswahlMethode():
    if art.get()==1: 
        preis=preisEntfernung(float(text_box_wert.get(1.0, "end-1c")))

    else:
        preis=preisMinuten(float(text_box_wert.get(1.0, "end-1c")))

    print(preis)
    ErgebnisString.set(str(preis))



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

