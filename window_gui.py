import random
from tkinter import filedialog
import matplotlib.pyplot as plt
import pyvisa
import tkinter as tk
import numpy as np
from tkinter import ttk
from plot import plot
from time import sleep
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from MOSFET import simulate_mosfet_current


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
    print('SU1:' + str(spannung))
    my_instrument.write('SU1:'+str(spannung))
    my_instrument.close()


def HM8143_Quelle_SpannungRechts(spannung):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    print('SU2:' + str(spannung))
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


# HM8150 Funktionsgenerator
def HM8150_Freq_Wellenform(wellenform):
    print("Wellenform ausgewählt: " + wellenform)
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL3::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('OP0')

    match wellenform:
        case "Sinus":
            my_instrument.write('SIN')
            print("Sinus")
        case "Rechteck":
            print("Rechteck")
            my_instrument.write('SQR')
        case "Dreieck":
            print("Dreieck")
            my_instrument.write('TRI')
        case "Puls":
            print("Puls")
            my_instrument.write('PLS')
        case "Sägezahn":
            print("Sägezahn")
            my_instrument.write('RMP')
        case _:
            print(wellenform+" nicht bekannt")

    my_instrument.close()


def HM8150_Freq_OffsetOn():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL3::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('OF1')
    my_instrument.close()


def HM8150_Freq_OffsetOff():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL3::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('OF0')
    my_instrument.close()


def HM8150_Freq_Toggle_Offset():
    if Button_Offset_on_off_HM8150_Freq.cget("text") == 'Off':
        HM8150_Freq_OffsetOn()
        Button_Offset_on_off_HM8150_Freq["text"] = "On"
    else:
        HM8150_Freq_OffsetOff()
        Button_Offset_on_off_HM8150_Freq["text"] = "Off"


def HM8150_Freq_OutputOn():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL3::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('OT1')
    my_instrument.close()


def HM8150_Freq_OutputOff():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL3::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('OT0')
    my_instrument.close()


def HM8150_Freq_Toggle_Output():
    if Button_Output_on_off_HM8150_Freq.cget("text") == 'Off':
        HM8150_Freq_OutputOn()
        Button_Output_on_off_HM8150_Freq["text"] = "On"
    else:
        HM8150_Freq_OutputOff()
        Button_Output_on_off_HM8150_Freq["text"] = "Off"


def HM8150_Freq_Amplitude(amplitude):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL3::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('AMP:'+str(amplitude))
    my_instrument.write('DAM')
    my_instrument.close()


def HM8150_Freq_Frequenz(frequenz):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL3::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('FRQ:'+str(frequenz))
    my_instrument.write('DFR')
    my_instrument.close()


def HM8150_Freq_Offset(offset):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL3::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('OFS:'+str(offset))
    my_instrument.write('DOF')
    my_instrument.close()


# Fluke
def ConvertMessbereichToDecimalString():
    match Combo_Messbereich_Fluke.get():
        case "100uA":
            return "0,000001"

        case "1mA":
            return "0,001"

        case "10mA":
            return "0,01"

        case "100mV" | "100mA":
            return "0,1"

        case "400mA":
            return "0,4"

        case "1V" | "1A":
            return "1"

        case "3A":
            return "3"

        case "10V" | "10A" | "10 Ohm":
            return "10"

        case "100V" | "100 Ohm":
            return "100"

        case "1000V" | "1k Ohm":
            return "1000"

        case "10k Ohm":
            return "10000"

        case "100k Ohm":
            return "100000"

        case "1M Ohm":
            return "1000000"

        case "100M Ohm":
            return "100000000"

        case "1G Ohm":
            return "1000000000"

        case _:
            return "0"


def Fluke_bestimme_Messbereich(messgroesse_eingestellt):
    match messgroesse_eingestellt:
        case "Gleichspannung" | "Wechselspannung":
            print("Spannung")
            Combo_Messbereich_Fluke['values'] = fluke_Messbereich_Spannung
            Combo_Messbereich_Fluke.current(0)
        case "Gleichstrom" | "Wechselstrom":
            print("Strom")
            Combo_Messbereich_Fluke['values'] = fluke_Messbereich_Strom
            Combo_Messbereich_Fluke.current(0)
        case "Widerstand":
            print("Widerstand")
            Combo_Messbereich_Fluke['values'] = fluke_Messbereich_Widerstand
            Combo_Messbereich_Fluke.current(0)


def Aktualisiere_Widgets_Parameter(parameter_einteilung):
    match parameter_einteilung:
        case "linear" | "quadratisch" | "exponentiell":
            Label_Eingabe_Parameter.grid_forget()
            Eingabe_Parameter.grid_forget()
            Label_Startwert_Parameter.grid(column=1, row=4, padx=5, pady=1)
            Label_Zielwert_Parameter.grid(column=2, row=4, padx=5, pady=1)
            Label_Schritte_Parameter.grid(column=3, row=4, padx=5, pady=1)
            Eingabe_Startwert_Parameter.grid(column=1, row=5, padx=5, pady=1)
            Eingabe_Zielwert_Parameter.grid(column=2, row=5, padx=5, pady=1)
            Eingabe_Schritte_Parameter.grid(column=3, row=5, padx=5, pady=1)
        case "manuell":
            Label_Startwert_Parameter.grid_forget()
            Label_Zielwert_Parameter.grid_forget()
            Label_Schritte_Parameter.grid_forget()
            Eingabe_Startwert_Parameter.grid_forget()
            Eingabe_Zielwert_Parameter.grid_forget()
            Eingabe_Schritte_Parameter.grid_forget()
            Label_Eingabe_Parameter.grid(column=1, row=4, sticky="W", columnspan=3, padx=5, pady=1)
            Eingabe_Parameter.grid(column=1, row=5, sticky="W", columnspan=3, padx=5, pady=1)
        case "ohne Parameter":
            Label_Startwert_Parameter.grid_forget()
            Label_Zielwert_Parameter.grid_forget()
            Label_Schritte_Parameter.grid_forget()
            Eingabe_Startwert_Parameter.grid_forget()
            Eingabe_Zielwert_Parameter.grid_forget()
            Eingabe_Schritte_Parameter.grid_forget()
            Label_Eingabe_Parameter.grid_forget()
            Eingabe_Parameter.grid_forget()


def ConvertMessgroesseToSCPI():
    match Combo_Messgroesse_Fluke.get():
        case "Gleichspannung":
            return ":CONF:VOLT:DC "
        case "Wechselspannung":
            return ":CONF:VOLT:AC "
        case "Gleichstrom":
            return ":CONF:CURR:DC "
        case "Wechselstrom":
            return ":CONF:CURR:AC "
        case "Widerstand":
            return ":CONF:RES "


def setIntegrationTime():
    match Combo_Messgroesse_Fluke.get():
        case "Gleichspannung":
            return ":volt:dc:nplc 1"
        case "Wechselspannung":
            return ":volt:ac:band 200"
        case "Gleichstrom":
            return ":curr:dc:nplc 1"
        case "Wechselstrom":
            return ":curr:ac:band 200"
        case "Widerstand":
            return ":res:nplc 1"


def MessungStop():
    global messungStop
    print("STOP")
    messungStop = True


def Fluke_Messe_Wert(v, p):

    # Messgröße Fluke
    # vdc = ":CONF:VOLT:DC "
    # vac = ":CONF:VOLT:AC "
    # adc = ":CONF:CURR:DC "
    # aac = ":CONF:CURR:AC "
    # res = ":CONF:RES "

    # Integrationszeit Fluke
    # vdc_nplc = ":volt:dc:nplc 1"
    # vac_nplc = ":volt:ac:band 200"
    # adc_nplc = ":curr:dc:nplc 1"
    # aac_nplc = ":curr:ac:band 200"
    # res_nplc = ":res:nplc 1"

    # Trigger
    # trig = ";:TRIG:DEL 0"
    # trig = ";:TRIG:SOUR BUS"

    # Commands Fluke
    # Aufbau: ...Messgröße+Messbereich+Integrationszeit+Trigger

    # messgroesse = ConvertMessgroesseToSCPI()
    # messbereich = ConvertMessbereichToDecimalString()
    # integrationszeit = setIntegrationTime().upper()

    # print(messgroesse+messbereich+trig+integrationszeit)

    # zum TESTEN auskommentiert
    # rm = pyvisa.ResourceManager()
    # my_instrument = rm.open_resource('ASRL5::INSTR', read_termination='\r\n', query_delay=0.21)
    # my_instrument.write('*RST;*CLS;CONF:VOLT:DC '+str(messbereich)+';:VOLT:DC:NPLC 1;:TRIG:SOUR BUS')
    # gemessener_wert = float(my_instrument.query(':INIT;*TRG;FETCH?')) # Wandle nach float und speichere gemessenen Wert
    # my_instrument.write('*RST;*CLS;syst:local')
    # my_instrument.close()

    gemessener_wert = simulate_mosfet_current(v_gate=p, v_drain=v, resistance_value=100)

    return gemessener_wert


def Parameter_bestimmen():
    match Combo_Parameter_Einteilung.get():
        case "linear":
            return np.linspace(int(Eingabe_Startwert_Parameter.get()), int(Eingabe_Zielwert_Parameter.get()), num=int(Eingabe_Schritte_Parameter.get()))
        case "quadratisch":
            i_min = np.square(int(Eingabe_Startwert_Parameter.get()))
            i_max = np.square(int(Eingabe_Zielwert_Parameter.get()))
            step = Eingabe_Schritte_Parameter.get()
            i_vec = np.linspace(i_min, i_max, num=int(step))
            para = np.sqrt(i_vec)
            para = np.round(para, decimals=2)
            return para
        case "exponentiell":
            i_min = np.exp(int(Eingabe_Startwert_Parameter.get()))
            i_max = np.exp(int(Eingabe_Zielwert_Parameter.get()))
            step = Eingabe_Schritte_Parameter.get()
            i_vec = np.linspace(i_min, i_max, num=int(step))
            para = np.log(i_vec)
            para = np.round(para, decimals=2)
            return para
        case "manuell":
            return Eingabe_Parameter.get().split(";")
        case "ohne Parameter":
            return [1]
    
    
def Create_table(headers, var):
    global Tabelle

    # Konfigurieren der ersten Spalte "#0" und setzen der Überschrift auf "Variable"
    Tabelle.column("#0", anchor=tk.CENTER, width=150, stretch=tk.NO)  # Zentrierte Ausrichtung
    Tabelle.heading("#0", text="Variable", anchor=tk.CENTER)  # Überschrift ebenfalls zentriert

    # Konfigurieren der zusätzlichen Spalten aus der headers-Liste
    Tabelle['columns'] = headers
    for header in headers:
        Tabelle.column(header, anchor=tk.CENTER, width=100)  # Zentrierte Ausrichtung für zusätzliche Spalten
        Tabelle.heading(header, text=header, anchor=tk.CENTER)  # Überschrift

    # Beispiel-Daten (in diesem Fall Zufallsdaten für zusätzliche Spalten)
    for i, variable in enumerate(var):
        Tabelle.insert(parent='', index='end', iid=i, text=f"{variable:.2f}", values=())  # Leere values-Liste

    # Tabelle anzeigen
    Tabelle.pack()
    

def Wert_in_Tabelle_einfuegen(row_id, column, value):
    global Tabelle
    # Hier wird der Wert in eine spezifische Zelle gesetzt
    Tabelle.set(row_id, column=column, value=value)


def Save_Messdaten_to_File():
    global messdaten
    global headers
    messdaten_transp = np.transpose(messdaten)
    # Datei speichern Dialog öffnen
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        # Datei öffnen und Matrix speichern
        np.savetxt(file_path, messdaten_transp, fmt='%s', delimiter=' ', header=str(headers), comments='')
        print(f"Numpy-Matrix wurde in {file_path} gespeichert.")


# Hauptfunktion
def Messung():
    # HM8143_Quelle_remoteOn()
    # HM8143_Quelle_AusgangOff()
    start = float(Eingabe_Startwert_Variable.get())
    schritt = float(Eingabe_Schrittweite_Variable.get())
    ziel = float(Eingabe_Zielwert_Variable.get())
    start_schritt_ziel = np.linspace(start, ziel, num=int((ziel - start) / schritt))

    # match Combo_Variable_Einteilung.get():
    #     case "linear":
    #         start_schritt_ziel = np.linspace(start, ziel, num=int((ziel - start) / schritt))
    #     case "logarithmisch":
    #         start_schritt_ziel = np.logspace(start, ziel, num=int((ziel - start) / schritt))
    #     case _:
    #         start_schritt_ziel = np.linspace(start, ziel, num=int((ziel - start) / schritt))

    global var_x
    global mess_y
    global x_i
    global messungStop
    global messdaten
    global headers

    messungStop = False
    var_x = []
    mess_y = []
    x_i = 0
    # para = ([1, 2, 4])
    # para = Eingabe_Parameter.get().split(";")
    para = Parameter_bestimmen()
    
    match Combo_Parameter.get():
        case "Spannung links" | "Spannung rechts":
            headers = [str(i) + "V (Parameter)" for i in para]
        case "Strom links" | "Strom rechts":
            headers = [str(i) + "V (Parameter)" for i in para]
        case _:
            headers = [str(i) + " (Parameter)" for i in para]

    Create_table(headers, list(start_schritt_ziel))

    messdaten = np.transpose(start_schritt_ziel)
    p_i = 0

    while p_i < len(para):  # gehe Parameter durch
        var_x = []
        mess_y = []
        x_i = 0
        while x_i < len(start_schritt_ziel):    # gehe Variablen durch für aktuellen Parameter
            # match Combo_Variable.get():
            #     case "Spannung links":
            #         HM8143_Quelle_SpannungLinks(start_schritt_ziel[x_i,])
            #         HM8143_Quelle_AusgangOn()
            #     case "Spannung rechts":
            #         HM8143_Quelle_SpannungRechts(start_schritt_ziel[x_i,])
            #         HM8143_Quelle_AusgangOn()
            ax.clear()
            ax.grid()
            for p_fertig in range(p_i):     # Ab den zweiten Parameter, gib die Kurven davor sofort aus
                ax.plot(start_schritt_ziel, messdaten[p_fertig+1, :], '--.')
                canvas.draw()
            var_x.append(start_schritt_ziel[x_i,])
            wert_gemessen = Fluke_Messe_Wert(start_schritt_ziel[x_i,], int(para[p_i]))
            mess_y.append(wert_gemessen)
            Wert_in_Tabelle_einfuegen(row_id=x_i, column=headers[p_i], value=Fluke_Messe_Wert(start_schritt_ziel[x_i,], int(para[p_i])))  # Tabelle
            ax.plot(var_x, mess_y, '--.')
            ax.set_xlabel(Combo_Variable.get())
            ax.set_ylabel('Fluke ' + Combo_Messgroesse_Fluke.get())
            canvas.draw()
            master.update()
            sleep(0.01)
            x_i += 1
        messdaten = np.vstack((messdaten, mess_y))  # Füge den durchlauf zu den Messdaten hinzu
        p_i += 1
    ax.legend(headers)
    canvas.draw()
    headers = np.append(['Variable'], headers)


headers = 0
messdaten = 0
x_i = 0
var_x = []
mess_y = []
messungStop = False

window_height = 700
window_width = 1065

fluke_Messbereich_Spannung = ["100mV", "1V", "10V", "100V", "1000V"]
fluke_Messbereich_Strom = ["100uA", "1mA", "10mA", "100mA", "400mA", "1A", "3A", "10A"]
fluke_Messbereich_Widerstand = ["10 Ohm", "100 Ohm", "1k Ohm", "10k Ohm", "100k Ohm", "1M Ohm", "100M Ohm", "1G Ohm"]

# ###############################################################################################################################################

# Instanziiere das Hauptfenster'
master = tk.Tk()
master.geometry("2065x560")
master.title("HalbleiterLeitTechnik")


Frame_Steuerung = ttk.Frame(master)
Frame_Plot = ttk.Frame(master)

Frame_Steuerung.place(x=0, y=0, relwidth=0.35, relheight=1)
Frame_Plot.place(relx=0.35, y=0, relwidth=0.65, relheight=1)

Tabelle = ttk.Treeview(Frame_Plot)

# Lokal
Frame_Lokal = ttk.Frame(Frame_Steuerung)
Button_Geraete_lokal = ttk.Button(Frame_Lokal, text="Geräte lokal bedienen")

# Lokal Design
Frame_Lokal.pack(fill='x')
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
Eingabe_Strom_links_HM8143_Quelle.insert(0, "0.095")
Eingabe_Strom_links_HM8143_Quelle.bind("<Return>", (lambda event: HM8143_Quelle_StromLinks(Eingabe_Strom_links_HM8143_Quelle.get())))
Button_on_off_HM8143_Quelle = ttk.Button(Frame_HM8143_Quelle, text="Off", command=HM8143_Quelle_Toggle_Ausgang)
Eingabe_Strom_rechts_HM8143_Quelle = ttk.Entry(Frame_HM8143_Quelle, width=7)
Eingabe_Strom_rechts_HM8143_Quelle.insert(0, "0.095")
Eingabe_Strom_rechts_HM8143_Quelle.bind("<Return>", (lambda event: HM8143_Quelle_StromRechts(Eingabe_Strom_rechts_HM8143_Quelle.get())))

# HM8143 Design
Frame_HM8143_Quelle.pack(fill='x')

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

Combo_Wellenform_HM8150_Freq.bind("<<ComboboxSelected>>", (lambda event: HM8150_Freq_Wellenform(Combo_Wellenform_HM8150_Freq.get())))

Eingabe_Amplitude_HM8150_Freq = ttk.Entry(Frame_HM8150_Freq, width=7)
Eingabe_Amplitude_HM8150_Freq.insert(0, "0.5")
Eingabe_Amplitude_HM8150_Freq.bind("<Return>", (lambda event: HM8150_Freq_Amplitude(Eingabe_Amplitude_HM8150_Freq.get())))
Eingabe_Frequenz_HM8150_Freq = ttk.Entry(Frame_HM8150_Freq, width=7)
Eingabe_Frequenz_HM8150_Freq.insert(0, "1000")
Eingabe_Frequenz_HM8150_Freq.bind("<Return>", (lambda event: HM8150_Freq_Frequenz(Eingabe_Frequenz_HM8150_Freq.get())))
Eingabe_Offset_HM8150_Freq = ttk.Entry(Frame_HM8150_Freq, width=7)
Eingabe_Offset_HM8150_Freq.insert(0, "0")
Eingabe_Offset_HM8150_Freq.bind("<Return>", (lambda event: HM8150_Freq_Offset(Eingabe_Offset_HM8150_Freq.get())))

Label_Output_Button_HM8150_Freq = ttk.Label(Frame_HM8150_Freq, text="Output")
Label_Offset_Button_HM8150_Freq = ttk.Label(Frame_HM8150_Freq, text="Offset")
Button_Output_on_off_HM8150_Freq = ttk.Button(Frame_HM8150_Freq, text="Off", command=HM8150_Freq_Toggle_Output)
Button_Offset_on_off_HM8150_Freq = ttk.Button(Frame_HM8150_Freq, text="Off", command=HM8150_Freq_Toggle_Offset)

# HM8150 Design
Frame_HM8150_Freq.pack(fill='x')

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

Combo_Messgroesse_Fluke.bind("<<ComboboxSelected>>", (lambda event: Fluke_bestimme_Messbereich(Combo_Messgroesse_Fluke.get())))

Combo_Messbereich_Fluke = ttk.Combobox(
    Frame_Fluke,
    state="readonly",
    values=fluke_Messbereich_Spannung,
    width=10
)
Combo_Messbereich_Fluke.current(0)

# Fluke Design
Frame_Fluke.pack(fill='x')
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
Eingabe_Startwert_Variable.insert(0, "0")
Eingabe_Schrittweite_Variable = ttk.Entry(Frame_Messung, width=7)
Eingabe_Schrittweite_Variable.insert(0, "0.2")
Eingabe_Zielwert_Variable = ttk.Entry(Frame_Messung, width=7)
Eingabe_Zielwert_Variable.insert(0, "2")

Label_Auswahl_Parameter = tk.Label(Frame_Messung, text="Parameter Auswahl")
Label_Eingabe_Parameter = tk.Label(Frame_Messung, text="Eingabe (mit ; getrennt)")

Combo_Parameter = ttk.Combobox(
    Frame_Messung,
    state="readonly",
    values=["Spannung links", "Spannung rechts", "Strom links", "Strom rechts"],
    width=16
)
Combo_Parameter.current(1)

Label_Parameter_Einteilung = tk.Label(Frame_Messung, text="Parameter Einteilung")

Combo_Parameter_Einteilung = ttk.Combobox(
    Frame_Messung,
    state="readonly",
    values=["linear", "quadratisch", "exponentiell", "manuell", "ohne Parameter"],
    width=16
)
Combo_Parameter_Einteilung.current(1)

Combo_Parameter_Einteilung.bind("<<ComboboxSelected>>", (lambda event: Aktualisiere_Widgets_Parameter(Combo_Parameter_Einteilung.get())))

Label_Startwert_Parameter = tk.Label(Frame_Messung, text="Startwert")
Label_Zielwert_Parameter = tk.Label(Frame_Messung, text="Zielwert")
Label_Schritte_Parameter = tk.Label(Frame_Messung, text="Schritte")

Eingabe_Startwert_Parameter = ttk.Entry(Frame_Messung, width=7)
Eingabe_Startwert_Parameter.insert(0, "1")
Eingabe_Zielwert_Parameter = ttk.Entry(Frame_Messung, width=7)
Eingabe_Zielwert_Parameter.insert(0, "8")
Eingabe_Schritte_Parameter = ttk.Entry(Frame_Messung, width=7)
Eingabe_Schritte_Parameter.insert(0, "1")

Eingabe_Parameter = ttk.Entry(Frame_Messung, width=20)

Button_Start_Messung = ttk.Button(Frame_Messung, text="Start", command=Messung)
Button_Stop_Messung = ttk.Button(Frame_Messung, text="Stop", command=MessungStop)
Button_Messdaten_Speichern = ttk.Button(Frame_Messung, text="Speichern", command=Save_Messdaten_to_File)

# Messung Design
Frame_Messung.pack(fill='x')

Label_Variable.grid(column=0, row=0, sticky="W", padx=5, pady=1)
Label_Startwert.grid(column=1, row=0, padx=5, pady=1)
Label_Schrittweite.grid(column=2, row=0, padx=5, pady=1)
Label_Zielwert.grid(column=3, row=0, padx=5, pady=1)

Combo_Variable.grid(column=0, row=1, sticky="W", padx=5, pady=1)
Eingabe_Startwert_Variable.grid(column=1, row=1, padx=5, pady=1)
Eingabe_Schrittweite_Variable.grid(column=2, row=1, padx=5, pady=1)
Eingabe_Zielwert_Variable.grid(column=3, row=1, padx=5, pady=1)

Label_Auswahl_Parameter.grid(column=0, row=2, sticky="W", padx=5, pady=1)

Combo_Parameter.grid(column=0, row=3, sticky="W", padx=5, pady=1)

Label_Parameter_Einteilung.grid(column=0, row=4, sticky="W", padx=5, pady=1)
Label_Startwert_Parameter.grid(column=1, row=4, padx=5, pady=1)
Label_Zielwert_Parameter.grid(column=2, row=4, padx=5, pady=1)
Label_Schritte_Parameter.grid(column=3, row=4, padx=5, pady=1)

Combo_Parameter_Einteilung.grid(column=0, row=5, sticky="W", padx=5, pady=1)
Eingabe_Startwert_Parameter.grid(column=1, row=5, padx=5, pady=1)
Eingabe_Zielwert_Parameter.grid(column=2, row=5, padx=5, pady=1)
Eingabe_Schritte_Parameter.grid(column=3, row=5, padx=5, pady=1)

Button_Start_Messung.grid(column=0, row=6, padx=10, pady=10)
Button_Messdaten_Speichern.grid(column=1, row=6, padx=10, pady=10)
Button_Stop_Messung.grid(column=2, row=6, padx=10, pady=10)


fig, ax = plt.subplots()
ax.grid()
canvas = FigureCanvasTkAgg(fig, master=Frame_Plot)
canvas.get_tk_widget().pack(side="left")

progressbar = ttk.Progressbar(Frame_Steuerung)
progressbar.pack(fill='both', expand = True)


# Zum ordentlichen Beenden des Programms, wenn man fenster schließt
def closing_cbk():
    # Shutdown procedure
    master.quit()
    master.destroy()


master.protocol("WM_DELETE_WINDOW", closing_cbk)

master.mainloop()
