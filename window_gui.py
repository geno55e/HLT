import pyvisa
import tkinter as tk
from tkinter import ttk
from plot import plot
from time import sleep


# HM8143 Spannungsquelle
def HM8143_Quelle_remoteOn():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('RM1')
    my_instrument.close()


def HM8143_Quelle_remoteOff():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('RM0')
    my_instrument.close()


def HM8143_Quelle_SpannungLinks(spannung):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('SU1:'+str(spannung))
    my_instrument.close()


def HM8143_Quelle_SpannungRechts(spannung):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('SU2:'+str(spannung))
    my_instrument.close()


def HM8143_Quelle_StromLinks(strom):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('SI1:'+str(strom))
    my_instrument.close()


def HM8143_Quelle_StromRechts(strom):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('SI2:'+str(strom))
    my_instrument.close()


def HM8143_Quelle_AusgangOn():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('OP1')
    my_instrument.close()


def HM8143_Quelle_AusgangOff():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('OP0')
    my_instrument.close()


def HM8143_Quelle_Toggle_Ausgang():
    if Button_on_off_HM8143_Quelle.cget("text") == 'Off':
        HM8143_Quelle_AusgangOn()
        Button_on_off_HM8143_Quelle["text"] = "On"
    else:
        HM8143_Quelle_AusgangOff()
        Button_on_off_HM8143_Quelle["text"] = "Off"


# Fluke
def Fluke_LeseGleichspannung(messbereich):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL5::INSTR', read_termination = '\r\n', query_delay = 0.21)
    my_instrument.write('*RST;*CLS;CONF:VOLT:DC '+str(messbereich)+';:VOLT:DC:NPLC 1;:TRIG:SOUR BUS')
    spannung = my_instrument.query(':INIT;*TRG;FETCH?')
    my_instrument.write('*RST;*CLS;syst:local')
    my_instrument.close()
    return spannung


window_height = 680
window_width = 1065


# ##########################################################################

# Instanziiere das Hauptfenster'

master = tk.Tk()
master.geometry("1065x500")
master.title("Halbleiterpraktikumleittechnik")

Frame_Steuerung = ttk.Frame(master)
Frame_Plot = ttk.Frame(master)

Frame_Steuerung.place(x=0, y=0, relwidth=0.4, relheight=1)
Frame_Plot.place(relx=0.4, y=0, relwidth=0.6, relheight=1)


# Lokal
Frame_Lokal = ttk.Frame(Frame_Steuerung)
Button_Geraete_lokal = ttk.Button(Frame_Lokal, text="Geräte lokal bedienen")
Frame_Lokal.pack()
Button_Geraete_lokal.pack(padx=10, pady=10)


# HM8143 Power
Frame_HM8143_Quelle = ttk.LabelFrame(Frame_Steuerung, text="Spannungsquelle HM8143")

Label_Spannung_links_HM8143_Quelle = ttk.Label(Frame_HM8143_Quelle, text="Spannung links")
Label_Spannung_rechts_HM8143_Quelle = ttk.Label(Frame_HM8143_Quelle, text="Spannung rechts")

Eingabe_Spannung_links_HM8143_Quelle = ttk.Entry(Frame_HM8143_Quelle, width=7)
Eingabe_Spannung_links_HM8143_Quelle.insert(0, "0,095")
Eingabe_Spannung_links_HM8143_Quelle.bind("<Return>", (lambda event: HM8143_Quelle_SpannungLinks(Eingabe_Spannung_links_HM8143_Quelle.get())))
Eingabe_Spannung_rechts_HM8143_Quelle = ttk.Entry(Frame_HM8143_Quelle, width=7)
Eingabe_Spannung_rechts_HM8143_Quelle.insert(0, "0")
Eingabe_Spannung_rechts_HM8143_Quelle.bind("<Return>", (lambda event: HM8143_Quelle_SpannungRechts(Eingabe_Spannung_rechts_HM8143_Quelle.get())))

Label_Strom_links_HM8143_Quelle = ttk.Label(Frame_HM8143_Quelle, text="Strom links")
Label_Strom_rechts_HM8143_Quelle = ttk.Label(Frame_HM8143_Quelle, text="Strom rechts")

Eingabe_Strom_links_HM8143_Quelle = ttk.Entry(Frame_HM8143_Quelle, width=7)
Eingabe_Strom_links_HM8143_Quelle.insert(0,"0.095")
Eingabe_Strom_links_HM8143_Quelle.bind("<Return>", (lambda event: HM8143_Quelle_StromLinks(Eingabe_Strom_links_HM8143_Quelle.get())))
Button_on_off_HM8143_Quelle = ttk.Button(Frame_HM8143_Quelle, text="Off", command=HM8143_Quelle_Toggle_Ausgang)
Eingabe_Strom_rechts_HM8143_Quelle = ttk.Entry(Frame_HM8143_Quelle, width=7)
Eingabe_Strom_rechts_HM8143_Quelle.insert(0,"0.095")
Eingabe_Strom_rechts_HM8143_Quelle.bind("<Return>", (lambda event: HM8143_Quelle_StromRechts(Eingabe_Strom_rechts_HM8143_Quelle.get())))

# HM8143 Design
Frame_HM8143_Quelle.pack()
Label_Spannung_links_HM8143_Quelle.grid(column=0, row=0, sticky="W", padx=5, pady=1)
Label_Spannung_rechts_HM8143_Quelle.grid(column=2, row=0, sticky="E", padx=5, pady=1)
Eingabe_Spannung_links_HM8143_Quelle.grid(column=0, row=1, sticky="W", padx=5, pady=1)
Eingabe_Spannung_rechts_HM8143_Quelle.grid(column=2, row=1, sticky="E", padx=5, pady=1)

Label_Strom_links_HM8143_Quelle.grid(column=0, row=2, sticky="W", padx=5, pady=1)
Label_Strom_rechts_HM8143_Quelle.grid(column=2, row=2, sticky="E", padx=5, pady=1)
Eingabe_Strom_links_HM8143_Quelle.grid(column=0, row=3, sticky="W", padx=5, pady=1)
Button_on_off_HM8143_Quelle.grid(column=1, row=3, padx=5, pady=1)
Eingabe_Strom_rechts_HM8143_Quelle.grid(column=2, row=3, sticky="E",  padx=5, pady=1)

# HM8150 Frequenzgenerator
Frame_HM8150_Freq = ttk.LabelFrame(Frame_Steuerung, text="Funktionsgenerator HM8150")

Label_Wellenform_HM8150_Freq = ttk.Label(Frame_HM8150_Freq, text="Wellenform")
Label_Amplitude_HM8150_Freq = ttk.Label(Frame_HM8150_Freq, text="Amplitude")
Label_Frequenz_HM8150_Freq = ttk.Label(Frame_HM8150_Freq, text="Frequenz")
Label_Offset_HM8150_Freq = ttk.Label(Frame_HM8150_Freq, text="Offset")

Combo_Wellenform_HM8150_Freq = ttk.Combobox(
    Frame_HM8150_Freq,
    state="readonly",
    values=["Sinus", "Rechteck", "Dreieck", "Puls", "Sägezahn"],
    width=13
)
Combo_Wellenform_HM8150_Freq.current(0)

Eingabe_Amplitude_HM8150_Freq = ttk.Entry(Frame_HM8150_Freq, width=7)
Eingabe_Amplitude_HM8150_Freq.insert(0,"0.5")
Eingabe_Frequenz_HM8150_Freq = ttk.Entry(Frame_HM8150_Freq, width=7)
Eingabe_Frequenz_HM8150_Freq.insert(0,"1000")
Eingabe_Offset_HM8150_Freq = ttk.Entry(Frame_HM8150_Freq, width=7)
Eingabe_Offset_HM8150_Freq.insert(0,"0")

Label_Output_Button_HM8150_Freq = ttk.Label(Frame_HM8150_Freq, text="Output")
Label_Offset_Button_HM8150_Freq = ttk.Label(Frame_HM8150_Freq, text="Offset")
Button_Output_on_off_HM8150_Freq = ttk.Button(Frame_HM8150_Freq, text="Off")
Button_Offset_on_off_HM8150_Freq = ttk.Button(Frame_HM8150_Freq, text="Off")

# HM8150 Design
Frame_HM8150_Freq.pack()
Label_Wellenform_HM8150_Freq.grid(column=0, row=0, sticky="W", padx=5, pady=1)
Label_Amplitude_HM8150_Freq.grid(column=1, row=0, padx=5, pady=1)
Label_Frequenz_HM8150_Freq.grid(column=2, row=0, padx=5, pady=1)
Label_Offset_HM8150_Freq.grid(column=3, row=0, padx=5, pady=1)
Combo_Wellenform_HM8150_Freq.grid(column=0, row=1, sticky="W", padx=5, pady=1)
Eingabe_Amplitude_HM8150_Freq.grid(column=1, row=1, padx=5, pady=1)
Eingabe_Frequenz_HM8150_Freq.grid(column=2, row=1, padx=5, pady=1)
Eingabe_Offset_HM8150_Freq.grid(column=3, row=1, padx=5, pady=1)
Label_Output_Button_HM8150_Freq.grid(column=0, row=2, columnspan=2, padx=5, pady=1)
Label_Offset_Button_HM8150_Freq.grid(column=2, row=2, columnspan=2, padx=5, pady=1)
Button_Output_on_off_HM8150_Freq.grid(column=0, row=3, columnspan=2, padx=5, pady=1)
Button_Offset_on_off_HM8150_Freq.grid(column=2, row=3, columnspan=2, padx=5, pady=1)


# Fluke
Frame_Fluke = ttk.LabelFrame(Frame_Steuerung, text="Multimeter Fluke 8846")

Label_Messgroesse_Fluke = ttk.Label(Frame_Fluke, text="Messgröße")
Label_Messbereich_Fluke = ttk.Label(Frame_Fluke, text="Messbereich")

Combo_Messgroesse_Fluke = ttk.Combobox(
    Frame_Fluke,
    state="readonly",
    values=["Gleichspannung", "Wechselspannung", "Gleichstrom", "Wechselstrom", "Widerstand"],
    width=18
)
Combo_Messgroesse_Fluke.current(0)

Combo_Messbereich_Fluke = ttk.Combobox(
    Frame_Fluke,
    state="readonly",
    values=["1V", "10V", "100V", "1000Ohm", "10A"],
    width=10
)
Combo_Messbereich_Fluke.current(0)

# Fluke Design
Frame_Fluke.pack()
Label_Messgroesse_Fluke.grid(column=0, row=0, sticky="W", padx=5, pady=1)
Label_Messbereich_Fluke.grid(column=1, row=0, padx=5, pady=1)
Combo_Messgroesse_Fluke.grid(column=0, row=1, sticky="W", padx=5, pady=1)
Combo_Messbereich_Fluke.grid(column=1, row=1, padx=5, pady=1)


# Messung
Frame_Messung = ttk.LabelFrame(Frame_Steuerung, text="Messung")
Label_Variable = tk.Label(Frame_Messung, text="Variable")
Label_Startwert = tk.Label(Frame_Messung, text="Startwert")
Label_Schrittweite = tk.Label(Frame_Messung, text="Schrittweite")
Label_Zielwert = tk.Label(Frame_Messung, text="Zielwert")

Combo_Variable = ttk.Combobox(
    Frame_Messung,
    state="readonly",
    values=["Spannung links", "Spannung rechts"],
    width=16
)
Combo_Variable.current(0)

Eingabe_Startwert_Variable = ttk.Entry(Frame_Messung, width=7)
Eingabe_Startwert_Variable.insert(0,"0")
Eingabe_Schrittweite_Variable = ttk.Entry(Frame_Messung, width=7)
Eingabe_Schrittweite_Variable.insert(0,"0.03")
Eingabe_Zielwert_Variable = ttk.Entry(Frame_Messung, width=7)
Eingabe_Zielwert_Variable.insert(0,"1")

Label_Auswahl_Parameter = tk.Label(Frame_Messung, text="Parameter Auswahl")
Label_Eingabe_Parameter = tk.Label(Frame_Messung, text="Eingabe")

Combo_Parameter = ttk.Combobox(
    Frame_Messung,
    state="readonly",
    values=["Spannung links", "Spannung rechts", "Strom links", "Strom rechts"],
    width=16
)
Combo_Parameter.current(1)

Eingabe_Parameter = ttk.Entry(Frame_Messung, width=20)

Button_Start_Messung = ttk.Button(Frame_Messung, text="Start")
Button_Stop_Messung = ttk.Button(Frame_Messung, text="Stop")

# Messung Design
Frame_Messung.pack()
Label_Variable.grid(column=0, row=0, sticky="W", padx=5, pady=1)
Label_Startwert.grid(column=1, row=0, padx=5, pady=1)
Label_Schrittweite.grid(column=2, row=0, padx=5, pady=1)
Label_Zielwert.grid(column=3, row=0, padx=5, pady=1)
Combo_Variable.grid(column=0, row=1, sticky="W", padx=5, pady=1)
Eingabe_Startwert_Variable.grid(column=1, row=1, padx=5, pady=1)
Eingabe_Schrittweite_Variable.grid(column=2, row=1, padx=5, pady=1)
Eingabe_Zielwert_Variable.grid(column=3, row=1, padx=5, pady=1)

Label_Auswahl_Parameter.grid(column=0, row=2, sticky="W", padx=5, pady=1)
Label_Eingabe_Parameter.grid(column=1, row=2, padx=5, pady=1)
Combo_Parameter.grid(column=0, row=3, sticky="W", padx=5, pady=1)
Eingabe_Parameter.grid(column=1, row=3, sticky="W", columnspan=3, padx=5, pady=1)

Button_Start_Messung.grid(column=0, row=4, columnspan=2, padx=10, pady=10)
Button_Stop_Messung.grid(column=2, row=4, columnspan=2, padx=10, pady=10)

plot(Frame_Plot)

master.mainloop()


