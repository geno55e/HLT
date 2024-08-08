import tkinter as tk
from tkinter import ttk
from plot import plot

window_height = 680
window_width = 1065

'Instanziere das Hauptfenster'
master = tk.Tk()

# Lokal
Frame_Geraete_lokal = tk.Frame(master, highlightthickness=1)
Button_Geraete_lokal = tk.Button(master, text="Geräte lokal bedienen")

# HM8143
Frame_HM8143_Quelle = tk.LabelFrame(master, text="Spannungsquelle HM8143")
Label_Ueberschrift_HM8143_Quelle = tk.Label(master, text="Spannungsquelle HM8143")

Label_Spannung_links_HM8143_Quelle = tk.Label(master, text="Spannung links")
Label_Spannung_rechts_HM8143_Quelle = tk.Label(master, text="Spannung rechts")

Eingabe_Spannung_links_HM8143_Quelle = tk.Entry(master)
Eingabe_Spannung_links_HM8143_Quelle.insert(0, "0")
Eingabe_Spannung_rechts_HM8143_Quelle = tk.Entry(master)
Eingabe_Spannung_rechts_HM8143_Quelle.insert(0, "0")

Label_Strom_links_HM8143_Quelle = tk.Label(master, text="Strom links")
Label_Strom_rechts_HM8143_Quelle = tk.Label(master, text="Strom rechts")

Eingabe_Strom_links_HM8143_Quelle = tk.Entry(master)
Eingabe_Strom_links_HM8143_Quelle.insert(0,"0.095")
Button_on_off_HM8143_Quelle = tk.Button(master, text="Off")
Eingabe_Strom_rechts_HM8143_Quelle = tk.Entry(master)
Eingabe_Strom_rechts_HM8143_Quelle.insert(0,"0.095")


# HM8150
Label_Ueberschrift_HM8150_Freq = tk.Label(master, text="Funktionsgenerator HM8150")

Label_Wellenform_HM8150_Freq = tk.Label(master, text="Wellenform")
Label_Amplitude_HM8150_Freq = tk.Label(master, text="Amplitude")
Label_Frequenz_HM8150_Freq = tk.Label(master, text="Frequenz")
Label_Offset_HM8150_Freq = tk.Label(master, text="Offset")

Combo_Wellenform_HM8150_Freq = ttk.Combobox(
    master,
    state="readonly",
    values=["Sinus", "Rechteck", "Dreieck", "Puls", "Sägezahn"]
)
Combo_Wellenform_HM8150_Freq.current(0)

Eingabe_Amplitude_HM8150_Freq = tk.Entry(master)
Eingabe_Amplitude_HM8150_Freq.insert(0,"0.5")
Eingabe_Frequenz_HM8150_Freq = tk.Entry(master)
Eingabe_Frequenz_HM8150_Freq.insert(0,"1000")
Eingabe_Offset_HM8150_Freq = tk.Entry(master)
Eingabe_Offset_HM8150_Freq.insert(0,"0")

Label_Output_Button_HM8150_Freq = tk.Label(master, text="Output")
Label_Offset_Button_HM8150_Freq = tk.Label(master, text="Offset")

Button_Output_on_off_HM8150_Freq = tk.Button(master, text="Off")
Button_Offset_on_off_HM8150_Freq = tk.Button(master, text="Off")


# Fluke
Label_Ueberschrift_Fluke = tk.Label(master, text="Multimeter Fluke 8846")

Label_Messgroesse_Fluke = tk.Label(master, text="Messgröße")
Label_Messbereich_Fluke = tk.Label(master, text="Messbereich")

Combo_Messgroesse_Fluke = ttk.Combobox(
    master,
    state="readonly",
    values=["Gleichspannung", "Wechselspannung", "Gleichstrom", "Wechselstrom", "Widerstand"]
)
Combo_Messgroesse_Fluke.current(0)

Combo_Messbereich_Fluke = ttk.Combobox(
    master,
    state="readonly",
    values=["1V", "10V", "100V", "1000Ohm", "10A"]
)
Combo_Messbereich_Fluke.current(0)

Label_Variable_Fluke = tk.Label(master, text="Variable")
Label_Startwert_Fluke = tk.Label(master, text="Startwert")
Label_Schrittweite_Fluke = tk.Label(master, text="Schrittweite")
Label_Zielwert_Fluke = tk.Label(master, text="Zielwert")

# Variable
Combo_Variable = ttk.Combobox(
    master,
    state="readonly",
    values=["Spannung links", "Spannung rechts"]
)
Combo_Variable.current(0)

Eingabe_Startwert_Variable = tk.Entry(master)
Eingabe_Startwert_Variable.insert(0,"0")
Eingabe_Schrittweite_Variable = tk.Entry(master)
Eingabe_Schrittweite_Variable.insert(0,"0.03")
Eingabe_Zielwert_Variable = tk.Entry(master)
Eingabe_Zielwert_Variable.insert(0,"1")

# Messung
Button_Start_Messung = tk.Button(master, text="Start")
Button_Stop_Messung = tk.Button(master, text="Stop")

graph = tk.PhotoImage(file=r"C:\Users\anton\OneDrive\TU-Berlin\Abschlussarbeit\HLT\graph.png")

# GRID
Button_Geraete_lokal.grid(row=0, column=1, columnspan=3, pady=2)


Label_Ueberschrift_HM8143_Quelle.grid(row=1, column=1, columnspan=3, pady=2)

Label_Spannung_links_HM8143_Quelle.grid(row=2, column=0, pady=2)
Label_Spannung_rechts_HM8143_Quelle.grid(row=2, column=4, pady=2)

Eingabe_Spannung_links_HM8143_Quelle.grid(row=3, column=0, pady=2)
Eingabe_Spannung_rechts_HM8143_Quelle.grid(row=3, column=4, pady=2)

Label_Strom_links_HM8143_Quelle.grid(row=4, column=0, pady=2)
Label_Strom_rechts_HM8143_Quelle.grid(row=4, column=4, pady=2)

Eingabe_Strom_links_HM8143_Quelle.grid(row=5, column=0, pady=2)
Button_on_off_HM8143_Quelle.grid(row=5, column=1, columnspan=3, pady=2)
Eingabe_Strom_rechts_HM8143_Quelle.grid(row=5, column=4, pady=2)


Label_Ueberschrift_HM8150_Freq.grid(row=6, column=1, columnspan=3, pady=2)

Label_Wellenform_HM8150_Freq.grid(row=7, column=0, pady=2)
Label_Amplitude_HM8150_Freq.grid(row=7, column=2, pady=2)
Label_Frequenz_HM8150_Freq.grid(row=7, column=3, pady=2)
Label_Offset_HM8150_Freq.grid(row=7, column=4, pady=2)

Combo_Wellenform_HM8150_Freq.grid(row=8, column=0, pady=2)
Eingabe_Amplitude_HM8150_Freq.grid(row=8, column=2, pady=2)
Eingabe_Frequenz_HM8150_Freq.grid(row=8, column=3, pady=2)
Eingabe_Offset_HM8150_Freq.grid(row=8, column=4, pady=2)

Label_Output_Button_HM8150_Freq.grid(row=9, column=0, pady=2)
Label_Offset_Button_HM8150_Freq.grid(row=9, column=1, pady=2)

Button_Output_on_off_HM8150_Freq.grid(row=10, column=0, pady=2)
Button_Offset_on_off_HM8150_Freq.grid(row=10, column=1, pady=2)


Label_Ueberschrift_Fluke.grid(row=11, column=1, columnspan=3, pady=2)

Label_Messgroesse_Fluke.grid(row=12, column=0, pady=2)
Label_Messbereich_Fluke.grid(row=12, column=3, pady=2)

Combo_Messgroesse_Fluke.grid(row=13, column=0, pady=2)
Combo_Messbereich_Fluke.grid(row=13, column=3, pady=2)

Label_Variable_Fluke.grid(row=14, column=0, pady=2)
Label_Startwert_Fluke.grid(row=14, column=2, pady=2)
Label_Schrittweite_Fluke.grid(row=14, column=3, pady=2)
Label_Zielwert_Fluke.grid(row=14, column=4, pady=2)

Combo_Variable.grid(row=15, column=0, pady=2)
Eingabe_Startwert_Variable.grid(row=15, column=2, pady=2)
Eingabe_Schrittweite_Variable.grid(row=15, column=3, pady=2)
Eingabe_Zielwert_Variable.grid(row=15, column=4, pady=2)

Button_Start_Messung.grid(row=16, column=0, columnspan=2, pady=2)
Button_Stop_Messung.grid(row=16, column=4, columnspan=2, pady=2)

plot(master)

master.mainloop()

