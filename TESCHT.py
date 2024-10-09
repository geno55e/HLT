from tkinter import filedialog
import matplotlib.pyplot as plt
import pyvisa
import tkinter as tk
import numpy as np
from tkinter import ttk
from time import sleep
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


def Geraete_lokal_bedienen():
    global geraete_lokal_on
    if geraete_lokal_on:
        # Wechsle zurück zu remote
        Eingabe_Spannung_links_HM8143_Quelle.configure(state='normal')
        Eingabe_Spannung_rechts_HM8143_Quelle.configure(state='normal')
        Eingabe_Strom_links_HM8143_Quelle.configure(state='normal')
        Button_on_off_HM8143_Quelle.configure(state='normal')
        Eingabe_Strom_rechts_HM8143_Quelle.configure(state='normal')
        Combo_Messgroesse_Fluke.configure(state='normal')
        Combo_Messbereich_Fluke.configure(state='normal')
        Combo_Variable.configure(state='normal')
        Eingabe_Startwert_Variable.configure(state='normal')
        Eingabe_Schrittweite_Variable.configure(state='normal')
        Eingabe_Zielwert_Variable.configure(state='normal')
        Combo_Parameter.configure(state='normal')
        Combo_Parameter_Einteilung.configure(state='normal')
        Eingabe_Startwert_Parameter.configure(state='normal')
        Eingabe_Zielwert_Parameter.configure(state='normal')
        Eingabe_Schritte_Parameter.configure(state='normal')
        Button_Messdaten_Speichern.configure(state='normal')
        Button_Start_Messung.configure(state='normal')
        Button_Stop_Messung.configure(state='normal')
        style.configure('My.TButton', foreground='black')
        HM8143_Quelle_remoteOn()
    else:
        # Wechsle zu lokal
        Eingabe_Spannung_links_HM8143_Quelle.configure(state='disabled')
        Eingabe_Spannung_rechts_HM8143_Quelle.configure(state='disabled')
        Eingabe_Strom_links_HM8143_Quelle.configure(state='disabled')
        Button_on_off_HM8143_Quelle.configure(state='disabled')
        Eingabe_Strom_rechts_HM8143_Quelle.configure(state='disabled')
        Combo_Messgroesse_Fluke.configure(state='disabled')
        Combo_Messbereich_Fluke.configure(state='disabled')
        Combo_Variable.configure(state='disabled')
        Eingabe_Startwert_Variable.configure(state='disabled')
        Eingabe_Schrittweite_Variable.configure(state='disabled')
        Eingabe_Zielwert_Variable.configure(state='disabled')
        Combo_Parameter.configure(state='disabled')
        Combo_Parameter_Einteilung.configure(state='disabled')
        Eingabe_Startwert_Parameter.configure(state='disabled')
        Eingabe_Zielwert_Parameter.configure(state='disabled')
        Eingabe_Schritte_Parameter.configure(state='disabled')
        Button_Messdaten_Speichern.configure(state='disabled')
        Button_Start_Messung.configure(state='disabled')
        Button_Stop_Messung.configure(state='disabled')
        style.configure('My.TButton', foreground='green')
        HM8143_Quelle_remoteOff()
        HM8143_Quelle_AusgangOff()
    # Zustand umschalten
    geraete_lokal_on = not geraete_lokal_on


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
    # print('SU1:' + str(spannung))
    my_instrument.write('SU1:' + str(spannung))
    my_instrument.close()


def HM8143_Quelle_SpannungRechts(spannung):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    # print('SU2:' + str(spannung))
    my_instrument.write('SU2:' + str(spannung))
    my_instrument.close()


def HM8143_Quelle_StromBegrenzLinks(strom):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('SI1:' + str(strom))
    my_instrument.close()


def HM8143_Quelle_StromBegrenzRechts(strom):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('SI2:' + str(strom))
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


def HM8143_Quelle_ZeigeStromLinks():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    strom_links = my_instrument.query('MI1')
    my_instrument.close()
    return strom_links.replace("I1:+", "")


def HM8143_Quelle_ZeigeStromRechts():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    strom_rechts = my_instrument.query('MI2')
    my_instrument.close()
    return strom_rechts.replace("I2:+", "")


def HM8143_Quelle_ZeigeSpannungLinks():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    spannung_links = my_instrument.query('MU1')
    my_instrument.close()
    return float(spannung_links[3:8])


def HM8143_Quelle_ZeigeSpannungRechts():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    spannung_rechts = my_instrument.query('MU2')
    my_instrument.close()
    return float(spannung_rechts[3:8])


def HM8143_Quelle_Status():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    status = my_instrument.query('STA?')
    my_instrument.close()
    return status


def ConvertMessbereichToDecimalString():
    match Combo_Messbereich_Fluke.get():
        case "100uA":
            return "0.000001"

        case "1mA":
            return "0.001"

        case "10mA":
            return "0.01"

        case "100mV" | "100mA":
            return "0.1"

        case "400mA":
            return "0.4"

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
    global fluke_Einheit
    match messgroesse_eingestellt:
        case "Gleichspannung" | "Wechselspannung":
            print("Spannung")
            Combo_Messbereich_Fluke['values'] = fluke_Messbereich_Spannung
            Combo_Messbereich_Fluke.current(0)
            fluke_Einheit = "V"
        case "Gleichstrom" | "Wechselstrom":
            print("Strom")
            Combo_Messbereich_Fluke['values'] = fluke_Messbereich_Strom
            Combo_Messbereich_Fluke.current(0)
            fluke_Einheit = "A"
        case "Widerstand":
            print("Widerstand")
            Combo_Messbereich_Fluke['values'] = fluke_Messbereich_Widerstand
            Combo_Messbereich_Fluke.current(0)
            fluke_Einheit = "Ohm"


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
            return "CONF:VOLT:DC "
        case "Wechselspannung":
            return "CONF:VOLT:AC "
        case "Gleichstrom":
            return "CONF:CURR:DC "
        case "Wechselstrom":
            return "CONF:CURR:AC "
        case "Widerstand":
            return "CONF:RES "


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


def Parameter_bestimmen():
    match Combo_Parameter_Einteilung.get():
        case "linear":
            return np.linspace(int(Eingabe_Startwert_Parameter.get()), int(Eingabe_Zielwert_Parameter.get()),
                               num=int(Eingabe_Schritte_Parameter.get()))
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


def Fluke_set_Range():
    # Messgröße Fluke
    # vdc = "CONF:VOLT:DC "
    # vac = "CONF:VOLT:AC "
    # adc = "CONF:CURR:DC "
    # aac = "CONF:CURR:AC "
    # res = "CONF:RES "

    # Integrationszeit Fluke
    # vdc_nplc = ":volt:dc:nplc 1"
    # vac_nplc = ":volt:ac:band 200"
    # adc_nplc = ":curr:dc:nplc 1"
    # aac_nplc = ":curr:ac:band 200"
    # res_nplc = ":res:nplc 1"

    # Trigger
    # trig = ":TRIG:DEL 0"
    trig = ":TRIG:SOUR BUS"
    # trig = ":TRIG:SOUR IMM"

    # Commands Fluke
    # Aufbau: ...Messgröße+Messbereich+Integrationszeit+Trigger

    messgroesse = ConvertMessgroesseToSCPI()
    messbereich = ConvertMessbereichToDecimalString()
    integrationszeit = setIntegrationTime().upper()
    print(messgroesse + messbereich + integrationszeit + trig)

    # zum TESTEN auskommentiert
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL5::INSTR', read_termination='\r\n', query_delay=0.21)
    set_range = '*RST;*CLS;' + messgroesse + str(messbereich) + ';' + integrationszeit + ';' + trig
    print(set_range)
    my_instrument.write(set_range)
    # gemessener_wert = float(my_instrument.query(':INIT;*TRG;FETCH?')) # Wandle nach float und speichere gemessenen Wert
    # print("MESSUNG: " + str(gemessener_wert) + messgroesse)
    # my_instrument.write('*RST;*CLS;syst:local')
    my_instrument.close()


def Fluke_reset():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL5::INSTR', read_termination='\r\n', query_delay=0.21)
    my_instrument.write('*RST;*CLS;syst:local')
    my_instrument.close()


def Fluke_Messe_Wert_live():
    # zum TESTEN auskommentiert
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL5::INSTR', read_termination='\r\n', query_delay=0.3)
    gemessener_wert = float(my_instrument.query(':INIT;*TRG;FETCH?'))  # Wandle nach float und speichere gemessenen Wert
    my_instrument.close()

    return gemessener_wert


def Messung():
    Fluke_set_Range()
    HM8143_Quelle_remoteOn()
    HM8143_Quelle_AusgangOff()

    start = float(Eingabe_Startwert_Variable.get())
    schritt = float(Eingabe_Schrittweite_Variable.get())
    ziel = float(Eingabe_Zielwert_Variable.get())
    start_schritt_ziel = np.linspace(start, ziel, num=int((ziel - start) / schritt))

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

    para = Parameter_bestimmen()

    messwerte_insgesamt = int((ziel - start) / schritt) * len(para)
    progressbar['maximum'] = messwerte_insgesamt  # Lege das Maximum von der Progressbar fest
    match Combo_Parameter.get():
        case "Spannung links" | "Spannung rechts":
            if len(para) == 1:
                headers = [Combo_Messgroesse_Fluke.get()]
            else:
                headers = [Combo_Messgroesse_Fluke.get() + ", Parameter " + str(i) + "V" for i in para]
        case "Strom links" | "Strom rechts":
            if len(para) == 1:
                headers = [Combo_Messgroesse_Fluke.get()]
            else:
                headers = [Combo_Messgroesse_Fluke.get() + ", Parameter " + str(i) + "A" for i in para]

    messdaten = np.transpose(start_schritt_ziel)

    p_i = 0
    progress = 0
    sleep(0.1)
    while (p_i < len(para)) and (not messungStop):  # gehe Parameter durch
        var_x = []
        mess_y = []
        x_i = 0
        if Combo_Parameter_Einteilung.get() != "ohne Parameter":
            match Combo_Parameter.get():
                case "Spannung links":
                    HM8143_Quelle_SpannungLinks(para[p_i])
                    HM8143_Quelle_StromBegrenzLinks(Eingabe_Strom_links_HM8143_Quelle.get())
                    HM8143_Quelle_AusgangOn()
                case "Spannung rechts":
                    HM8143_Quelle_SpannungRechts(para[p_i])
                    HM8143_Quelle_StromBegrenzRechts(Eingabe_Strom_rechts_HM8143_Quelle.get())
                    HM8143_Quelle_AusgangOn()
                case "Strom rechts":
                    # HM8143_Quelle_StromBegrenzRechtsCC(para[p_i])
                    HM8143_Quelle_AusgangOn()
                case "Strom links":
                    # HM8143_Quelle_StromBegrenzLinksCC(para[p_i])
                    HM8143_Quelle_AusgangOn()
        while x_i < len(start_schritt_ziel) and (not messungStop):  # gehe Variablen durch für aktuellen Parameter
            match Combo_Variable.get():
                case "Spannung links":
                    HM8143_Quelle_SpannungLinks(start_schritt_ziel[x_i,])
                    HM8143_Quelle_StromBegrenzLinks(Eingabe_Strom_links_HM8143_Quelle.get())
                    HM8143_Quelle_AusgangOn()
                case "Spannung rechts":
                    HM8143_Quelle_SpannungRechts(start_schritt_ziel[x_i,])
                    HM8143_Quelle_StromBegrenzRechts(Eingabe_Strom_rechts_HM8143_Quelle.get())
                    HM8143_Quelle_AusgangOn()

            sleep(0.3)

            # Speichere Daten und aktualisiere Plot
            ax.clear()
            ax.grid()
            for p_fertig in range(p_i):  # Ab den zweiten Parameter, gib die Kurven davor sofort aus
                ax.plot(start_schritt_ziel, messdaten[p_fertig + 1, :], '--.')
                canvas.draw()
            var_x.append(start_schritt_ziel[x_i,])

            wert_gemessen = Fluke_Messe_Wert_live()  # FLUKE MESSE WERT
            print(str(progress+1)+"/"+str(messwerte_insgesamt) + "      VAR: " + str(x_i) + "     FLUKE: " + str(wert_gemessen))
            print("Spannung: " + str(HM8143_Quelle_ZeigeSpannungLinks()) + "  Spannung: " + str(HM8143_Quelle_ZeigeSpannungRechts()))
            print("   Strom: " + str(HM8143_Quelle_ZeigeStromLinks()) + "       Strom:" + str(HM8143_Quelle_ZeigeStromRechts()))
            mess_y.append(wert_gemessen)
            ax.plot(var_x, mess_y, '--.')
            ax.set_xlabel(Combo_Variable.get())
            ax.set_ylabel('Fluke ' + Combo_Messgroesse_Fluke.get())
            canvas.draw()
            master.update()
            x_i += 1
            progress += 1
            progressbar['value'] = progress  # Progress um eins erweitern

        if not messungStop:
            messdaten = np.vstack((messdaten, mess_y))  # Füge den durchlauf zu den Messdaten hinzu
            p_i += 1

    ax.legend(headers)
    canvas.draw()
    headers = np.append(['Variable'], headers)  # Füge Bezeichner Variable an Kopf an
    HM8143_Quelle_AusgangOff()


def regulate_current(target_current, start_voltage=0.0, tolerance=0.001, max_voltage=10, min_voltage=0.0, step_size=0.2):
    """
    Regelt die Spannung, um den Zielstrom (target_current) innerhalb der Toleranz zu erreichen.

    :param target_current: Der gewünschte Strom in A.
    :param start_voltage: Die Anfangsspannung für die Regelung.
    :param tolerance: Die zulässige Abweichung vom Zielstrom (±0.001 A).
    :param max_voltage: Maximale Spannung, die eingestellt werden kann.
    :param min_voltage: Minimale Spannung, die eingestellt werden kann.
    :param step_size: Schrittweite, um die Spannung anzupassen.
    """
    def get_current():
        # Liest den aktuellen Strom und gibt ihn als float zurück
        current_str = HM8143_Quelle_ZeigeStromLinks()
        return float(current_str.replace("A", ""))

    HM8143_Quelle_remoteOn()
    HM8143_Quelle_StromBegrenzLinks(target_current+0.001)   # Setze die Strombegrenzung auf den gewünschten Wert (zur Absicherung), 0.001 Offset drauf wegen statischer Abweichung
    HM8143_Quelle_AusgangOn()
    sleep(0.8)

    # status = HM8143_Quelle_Status()[4:7]    # Lese Status Ausgang links aus (CC1, CV1 oder ---)
    current_voltage = HM8143_Quelle_ZeigeSpannungLinks()

    # Starte die Regelung der Spannung
    # if status == "CC1":     # Prüfe ob Ausgang links in Strombegrenzung ist
    #     current_voltage = float(HM8143_Quelle_ZeigeSpannungLinks())

    HM8143_Quelle_SpannungLinks(current_voltage)    # Setze linke Quelle auf die Start-Spannung

    while True:
        current = get_current()
        error = round((target_current - current),3)

        # Wenn der Strom innerhalb der Toleranz ist, beenden, sonst Spannung anpassen basierend auf dem Fehler (P-Regler)
        if abs(error) <= tolerance:
            current_voltage += step_size    # Beim Erreichen des Stroms noch ein Step machen um in die Strombegrenzung zu kommen
            HM8143_Quelle_SpannungLinks(current_voltage)
            print("Strom stabil bei "+HM8143_Quelle_ZeigeStromLinks()+" mit Spannung "+ str(HM8143_Quelle_ZeigeSpannungLinks()))
            break
        else:
            # Strom zu niedrig → Spannung erhöhen
            current_voltage += step_size

        # Stellt sicher, dass der Wert von current_voltage immer im Bereich von min_voltage bis max_voltage liegt (optional)
        current_voltage = max(min_voltage, min(current_voltage, max_voltage))

        # Spannung einstellen
        HM8143_Quelle_SpannungLinks(current_voltage)
        sleep(0.3)

        # Optionale Ausgabe zur Überwachung
        print("Aktuelle Spannung: " + str(HM8143_Quelle_ZeigeSpannungLinks()) + ", Aktueller Strom: " + HM8143_Quelle_ZeigeStromLinks())

    # HM8143_Quelle_AusgangOff()
    HM8143_Quelle_remoteOff()


headers = 0
messdaten = 0
x_i = 0
var_x = []
mess_y = []
messungStop = False
geraete_lokal_on = False
fluke_Einheit = "X"

window_height = 700
window_width = 1065

fluke_Messbereich_Spannung = ["100mV", "1V", "10V", "100V", "1000V"]
fluke_Messbereich_Strom = ["100uA", "1mA", "10mA", "100mA", "400mA", "1A", "3A", "10A"]
fluke_Messbereich_Widerstand = ["10 Ohm", "100 Ohm", "1k Ohm", "10k Ohm", "100k Ohm", "1M Ohm", "100M Ohm", "1G Ohm"]

# ###############################################################################################################################################


# Instanziiere das Hauptfenster'
master = tk.Tk()
master.geometry("1500x900")
master.title("HalbleiterLeitTechnik")

Frame_Steuerung = ttk.Frame(master)
Frame_Plot = ttk.Frame(master, relief='groove')

Frame_Steuerung.place(x=0, y=0, relwidth=0.23, relheight=1)
Frame_Plot.place(relx=0.23, y=0, relwidth=0.77, relheight=1)


style = ttk.Style()
# style.configure('My.TButton', background='lightblue', foreground='black')

# Lokal
Frame_Lokal = ttk.Frame(Frame_Steuerung)
Button_Geraete_lokal = ttk.Button(Frame_Lokal, text="Geräte lokal bedienen", style='My.TButton', command=Geraete_lokal_bedienen)

# Lokal Design
Frame_Lokal.pack(fill='x')
Button_Geraete_lokal.pack(padx=10, pady=10)


# HM8143 Power
Frame_HM8143_Quelle = ttk.LabelFrame(Frame_Steuerung, text="Spannungsquelle HM8143")

Label_Spannung_links_HM8143_Quelle = ttk.Label(Frame_HM8143_Quelle, text="Spannung links")
Label_Spannung_rechts_HM8143_Quelle = ttk.Label(Frame_HM8143_Quelle, text="Spannung rechts")

Eingabe_Spannung_links_HM8143_Quelle = ttk.Entry(Frame_HM8143_Quelle, width=7)
Eingabe_Spannung_links_HM8143_Quelle.insert(0, "0.5")
Eingabe_Spannung_links_HM8143_Quelle.bind("<Return>", (lambda event: HM8143_Quelle_SpannungLinks(Eingabe_Spannung_links_HM8143_Quelle.get())))
Eingabe_Spannung_rechts_HM8143_Quelle = ttk.Entry(Frame_HM8143_Quelle, width=7)
Eingabe_Spannung_rechts_HM8143_Quelle.insert(0, "0.5")
Eingabe_Spannung_rechts_HM8143_Quelle.bind("<Return>", (lambda event: HM8143_Quelle_SpannungRechts(Eingabe_Spannung_rechts_HM8143_Quelle.get())))

Label_Strom_links_HM8143_Quelle = ttk.Label(Frame_HM8143_Quelle, text="Strom links")
Label_Strom_rechts_HM8143_Quelle = ttk.Label(Frame_HM8143_Quelle, text="Strom rechts")

Eingabe_Strom_links_HM8143_Quelle = ttk.Entry(Frame_HM8143_Quelle, width=7)
Eingabe_Strom_links_HM8143_Quelle.insert(0, "0.095")
Eingabe_Strom_links_HM8143_Quelle.bind("<Return>", (lambda event: HM8143_Quelle_StromBegrenzLinks(Eingabe_Strom_links_HM8143_Quelle.get())))
Button_on_off_HM8143_Quelle = ttk.Button(Frame_HM8143_Quelle, text="Off", command=HM8143_Quelle_Toggle_Ausgang)
Eingabe_Strom_rechts_HM8143_Quelle = ttk.Entry(Frame_HM8143_Quelle, width=7)
Eingabe_Strom_rechts_HM8143_Quelle.insert(0, "0.095")
Eingabe_Strom_rechts_HM8143_Quelle.bind("<Return>", (lambda event: HM8143_Quelle_StromBegrenzRechts(Eingabe_Strom_rechts_HM8143_Quelle.get())))

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
Eingabe_Strom_rechts_HM8143_Quelle.grid(column=2, row=3, sticky="E", padx=5, pady=1)

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

Combo_Messbereich_Fluke.current(2)

Combo_Messbereich_Fluke.bind("<<ComboboxSelected>>", (lambda event: Fluke_set_Range()))
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
    values=["Spannung links", "Spannung rechts", "Offset", "Frequenz"],
    width=15
)
Combo_Variable.current(1)

Eingabe_Startwert_Variable = ttk.Entry(Frame_Messung, width=6)
Eingabe_Startwert_Variable.insert(0, "0")
Eingabe_Schrittweite_Variable = ttk.Entry(Frame_Messung, width=6)
Eingabe_Schrittweite_Variable.insert(0, "0.2")
Eingabe_Zielwert_Variable = ttk.Entry(Frame_Messung, width=6)
Eingabe_Zielwert_Variable.insert(0, "2")

Label_Auswahl_Parameter = tk.Label(Frame_Messung, text="Parameter Auswahl")
Label_Eingabe_Parameter = tk.Label(Frame_Messung, text="Eingabe (mit ; getrennt)")

Combo_Parameter = ttk.Combobox(
    Frame_Messung,
    state="readonly",
    values=["Spannung links", "Spannung rechts", "Strom links", "Strom rechts"],
    width=15
)
Combo_Parameter.current(0)

Label_Parameter_Einteilung = tk.Label(Frame_Messung, text="Parameter Einteilung")

Combo_Parameter_Einteilung = ttk.Combobox(
    Frame_Messung,
    state="readonly",
    values=["linear", "quadratisch", "exponentiell", "manuell", "ohne Parameter"],
    width=15
)
Combo_Parameter_Einteilung.current(1)

Combo_Parameter_Einteilung.bind("<<ComboboxSelected>>", (lambda event: Aktualisiere_Widgets_Parameter(Combo_Parameter_Einteilung.get())))

Label_Startwert_Parameter = tk.Label(Frame_Messung, text="Startwert")
Label_Zielwert_Parameter = tk.Label(Frame_Messung, text="Zielwert")
Label_Schritte_Parameter = tk.Label(Frame_Messung, text="Schritte")

Eingabe_Startwert_Parameter = ttk.Entry(Frame_Messung, width=6)
Eingabe_Startwert_Parameter.insert(0, "1")
Eingabe_Zielwert_Parameter = ttk.Entry(Frame_Messung, width=6)
Eingabe_Zielwert_Parameter.insert(0, "8")
Eingabe_Schritte_Parameter = ttk.Entry(Frame_Messung, width=6)
Eingabe_Schritte_Parameter.insert(0, "1")

Eingabe_Parameter = ttk.Entry(Frame_Messung, width=20)

Button_Start_Messung = ttk.Button(Frame_Messung, text="Start", command=Messung, width=6)
Button_Messdaten_Speichern = ttk.Button(Frame_Messung, text="Speichern", command=Save_Messdaten_to_File, width=9)
Button_Stop_Messung = ttk.Button(Frame_Messung, text="Stop", command=MessungStop, width=6)

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

Button_Start_Messung.grid(column=0, row=6, padx=5, pady=3)
Button_Messdaten_Speichern.grid(column=1, row=6, padx=5, pady=3)
Button_Stop_Messung.grid(column=2, row=6, padx=5, pady=3)

fig, ax = plt.subplots()
ax.grid()
canvas = FigureCanvasTkAgg(fig, master=Frame_Plot)
canvas.get_tk_widget().pack(fill='both', expand=True)
toolbar = NavigationToolbar2Tk(canvas, Frame_Plot)


progressbar = ttk.Progressbar(Frame_Steuerung)
progressbar.pack(fill='x', expand=True)

# Fluke_set_Range()


# Zum ordentlichen Beenden des Programms, wenn man das Hauptfenster schließt
def closing_cbk():
    HM8143_Quelle_AusgangOff()
    HM8143_Quelle_remoteOff()
    Fluke_reset()
    # Shutdown procedure
    master.quit()
    master.destroy()


master.protocol("WM_DELETE_WINDOW", closing_cbk)

master.mainloop()