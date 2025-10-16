import pyvisa # Protokoll und "Framework" für die Kommunikation mit Laborgeräten
import tkinter as tk    # GUI
from tkinter import ttk # GUI (mehr Einstellungsmöglichkeiten)
from tkinter import messagebox  # GUI (Ausgabe von Meldungen)
from tktooltip import ToolTip   # GUI (Tooltips zur Beschreibung der Funktionen)
from tkinter import filedialog  # Speichern von Dateien
import matplotlib.pyplot as plt # Darstellung von Plots
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) # GUI Integration von matplotlib (Plotfenster) in tkinter (Hauptfenster)
import numpy as np  # Erzeugung von Werten, Vektoren, Matrizen und Rechenoperationen
from time import sleep  # Wartezeit zwischen Messungen
import Validation_functions as Vali # Ausgelagerte Validierungsfunktionen für Überprüfung der Eingaben
from config_loader import Config    # Config zur Einstellung der Standartwerte vor dem Start der Anwendung

# LADE die Config mit den Pre-Sets, wenn Werte fehlen, werden Standartwerte aus config_loader.py verwendet
config = Config()

# HM8143 Spannungsquelle
def HM8143_Quelle_remoteOn():
    """
    Einschalten des Remote-Zustandes von der HAMEG Spannungsquelle. Die Frontbedienelemente werden gesperrt. Eine Bedienung des Netzgeräts kann jetzt
    nur noch mit dem Interface erfolgen.
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_power_source, write_termination='\r', read_termination='\r')
    my_instrument.write('RM1')
    my_instrument.close()


def HM8143_Quelle_remoteOff():
    """
    Ausschalten des Remote-Zustandes von der HAMEG Spannungsquelle. Die Frontbedienelemente sind entsperrt.
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_power_source, write_termination='\r', read_termination='\r')
    my_instrument.write('RM0')
    my_instrument.close()


def HM8143_Quelle_SpannungLinks(spannung):
    """
    Setze Spannung 1 (links) von der HAMEG Spannungsquelle auf den angegebenen Wert (spannung)
    :param spannung: Spannung in [V] die eingestellt werden soll.
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_power_source, write_termination='\r', read_termination='\r')
    # print('SU1:' + str(spannung))
    my_instrument.write('SU1:' + str(spannung))
    my_instrument.close()
    print('Spannung links eingestellt: ' + str(spannung))


def HM8143_Quelle_SpannungRechts(spannung):
    """
    Setze Spannung 2 (rechts) von der HAMEG Spannungsquelle auf den angegebenen Wert (spannung)
    :param spannung: Spannung in [V] die eingestellt werden soll.
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_power_source, write_termination='\r', read_termination='\r')
    # print('SU2:' + str(spannung))
    my_instrument.write('SU2:' + str(spannung))
    my_instrument.close()
    print('Spannung rechts eingestellt: ' + str(spannung))


def HM8143_Quelle_StromBegrenzLinks(strom):
    """
    Setze Strombegrenzung 1 (links) von der HAMEG Spannungsquelle auf den angegebenen Wert (strom)
    :param strom: Strom in [A] die eingestellt werden soll.
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_power_source, write_termination='\r', read_termination='\r')
    my_instrument.write('SI1:' + str(strom))
    my_instrument.close()
    print('Strom (Compliance) links eingestellt: ' + str(strom))


def HM8143_Quelle_StromBegrenzRechts(strom):
    """
    Setze Strombegrenzung 2 (rechts) von der HAMEG Spannungsquelle auf den angegebenen Wert (strom)
    :param strom: Strom in [A] die eingestellt werden soll.
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_power_source, write_termination='\r', read_termination='\r')
    my_instrument.write('SI2:' + str(strom))
    my_instrument.close()
    print('Strom (Compliance) rechts eingestellt: ' + str(strom))


def HM8143_Quelle_AusgangOn():
    """
    Die Ausgangsbuchsen von der HAMEG Spannungsquelle werden eingeschaltet.
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_power_source, write_termination='\r', read_termination='\r')
    my_instrument.write('OP1')
    my_instrument.close()
    Button_on_off_HM8143_Quelle["text"] = "On"


def HM8143_Quelle_AusgangOff():
    """
    Die Ausgangsbuchsen von der HAMEG Spannungsquelle werden ausgeschaltet.
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_power_source, write_termination='\r', read_termination='\r')
    my_instrument.write('OP0')
    my_instrument.close()
    style.configure('quelle.TButton', foreground='black')
    Button_on_off_HM8143_Quelle["text"] = "Off"


def HM8143_Quelle_Toggle_Ausgang():
    if Button_on_off_HM8143_Quelle.cget("text") == 'Off':
        HM8143_Quelle_AusgangOn()
        style.configure('quelle.TButton', foreground='green')
        Button_on_off_HM8143_Quelle["text"] = "On"
    else:
        HM8143_Quelle_AusgangOff()
        style.configure('quelle.TButton', foreground='black')
        Button_on_off_HM8143_Quelle["text"] = "Off"


def HM8143_Quelle_ZeigeStromLinks():
    """
    Gebe die Stromwerte zurück (String 0.000A), entsprechend der bei der letzten Messung gemessenen Istwerten des entnommenen Stromes von Ausgang 1
    (links).
    :return: String 0.000
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_power_source, write_termination='\r', read_termination='\r')
    strom_links = my_instrument.query('MI1')
    my_instrument.close()
    return strom_links[4:-1]


def HM8143_Quelle_ZeigeStromRechts():
    """
    Gebe die Stromwerte zurück (String 0.000A), entsprechend der bei der letzten Messung gemessenen Istwerten des entnommenen Stromes von Ausgang 2
    (rechts).
    :return: String 0.000
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_power_source, write_termination='\r', read_termination='\r')
    strom_rechts = my_instrument.query('MI2')
    my_instrument.close()
    return strom_rechts[4:-1]


def HM8143_Quelle_ZeigeSpannungLinks():
    """
    Gebe den Spannungswert (gemessen) entsprechend der bei der letzten Messung gemessenen Istwerten am Ausgang 1 (links) anstehenden Spannungen
    zurück.
    :return: float 0.00
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_power_source, write_termination='\r', read_termination='\r')
    spannung_links = my_instrument.query('MU1')
    my_instrument.close()
    return float(spannung_links[3:8])


def HM8143_Quelle_ZeigeSpannungRechts():
    """
    Gebe den Spannungswert (gemessen) entsprechend der bei der letzten Messung gemessenen Istwerten am Ausgang 2 (rechts) anstehenden Spannungen
    zurück.
    :return: float 0.00
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_power_source, write_termination='\r', read_termination='\r')
    spannung_rechts = my_instrument.query('MU2')
    my_instrument.close()
    return float(spannung_rechts[3:8])


def HM8143_Quelle_ZeigeSpannungLinksGesetzt():
    """
    Gebe den Soll-Spannungswert (eingestellt) am Ausgang 1 (links) zurück.
    :return: float 0.00
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_power_source, write_termination='\r', read_termination='\r')
    spannung_links = my_instrument.query('RU1')
    my_instrument.close()
    return float(spannung_links[3:8])


def HM8143_Quelle_ZeigeSpannungRechtsGesetzt():
    """
    Gebe den Soll-Spannungswert (eingestellt) am Ausgang 2 (rechts) zurück.
    :return: float 0.00
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_power_source, write_termination='\r', read_termination='\r')
    spannung_rechts = my_instrument.query('RU2')
    my_instrument.close()
    return float(spannung_rechts[3:8])


def HM8143_Quelle_Status():
    """
    Gibt einen String zurück (OP1/0 CV1/CC1 CV2/CC2 RM0/1), der Auskunft über den momentanen Gerätestatus gibt.
    :return: OP1/0 CV1/CC1 CV2/CC2 RM0/1
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_power_source, write_termination='\r', read_termination='\r')
    status = my_instrument.query('STA?')
    my_instrument.close()
    return status


def HM8143_IstAusgangInCC(ausgang):
    """
    Gebe einen True zurück wenn der übergebene Ausgang sich im Konstantstrombetrieb (CC) befindet, sonst false
    :param ausgang: Der Ausgang welcher abgefragt werden soll: links = 1 oder rechts = 2.
    :return: bool
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_power_source, write_termination='\r', read_termination='\r')
    status_powersup = my_instrument.query('STA')

    my_instrument.write('RM0')
    my_instrument.close()
    if ausgang == 1 and status_powersup[4:-8] == "CC1":
        return True
    elif ausgang == 2 and status_powersup[8:-4] == "CC2":
        return True
    else:
        return False


# HM8150 Funktionsgenerator

# Reihenfolge der Befehle um das Gerät einzustellen:
# 1. Signalform (SIN;TRI;...)
# 2. Frequenz (FRQ:xxxx )
# 3. Offsetspannung (OFS:xxx)
# 4. Amplitude setzen (AMP:xxx)
# 5. Ausgang ein/ausschalten (OT1 ; OT0)

def HM8150_Freq_remoteOff():
    """
    Ausschalten des Remote-Zustandes von des HAMEG Funktionsgenerators. Die Frontbedienelemente werden entsperrt. Eine Bedienung des Netzgeräts kann
    jetzt mit dem Interface erfolgen.
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_frequency_generator, write_termination='\r', read_termination='\r')
    my_instrument.write('RM0')
    my_instrument.close()


def HM8150_Freq_Wellenform(wellenform):
    """
    Einstellen der Signalform des Ausgangssignals
    :param wellenform: SIN: Sinus, TRI: Dreieck, PLS: Impuls, RMP: Sägezahn (positiv), RMN Sägezahn (negativ), ARB: Arbitary
    """
    print("Wellenform ausgewählt: " + wellenform)
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_frequency_generator, write_termination='\r', read_termination='\r')
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
            print(wellenform + " nicht bekannt")

    my_instrument.close()


def HM8150_Freq_OffsetOn():
    """
    Einschalten der Offsetspannung
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_frequency_generator, write_termination='\r', read_termination='\r')
    my_instrument.write('OF1')
    my_instrument.close()


def HM8150_Freq_OffsetOff():
    """
    Ausschalten der Offsetspannung
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_frequency_generator, write_termination='\r', read_termination='\r')
    my_instrument.write('OF0')
    my_instrument.close()


def HM8150_Freq_Toggle_Offset():
    """
    Schaltet die Offsetspannung ein oder aus abhängig von dem aktuellen Zustand.
    """
    if Button_Offset_on_off_HM8150_Freq.cget("text") == 'Off':
        HM8150_Freq_OffsetOn()
        Button_Offset_on_off_HM8150_Freq["text"] = "On"
    else:
        HM8150_Freq_OffsetOff()
        Button_Offset_on_off_HM8150_Freq["text"] = "Off"


def HM8150_Freq_OutputOn():
    """
    Einschalten des Ausgangs vom Frequenzgenerator
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_frequency_generator, write_termination='\r', read_termination='\r')
    my_instrument.write('OT1')
    my_instrument.close()
    Button_Output_on_off_HM8150_Freq["text"] = "On"


def HM8150_Freq_OutputOff():
    """
    Ausschalten des Ausgangssignals vom Frequenzgenerator
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_frequency_generator, write_termination='\r', read_termination='\r')
    my_instrument.write('OT0')
    my_instrument.close()
    style.configure('freq.TButton', foreground='black')
    Button_Output_on_off_HM8150_Freq["text"] = "Off"


def HM8150_Freq_Toggle_Output():
    """
    Schaltet den Ausgang vom Frequenzgenerator ein oder aus abhängig von dem aktuellen Zustand.
    """
    if Button_Output_on_off_HM8150_Freq.cget("text") == 'Off':
        HM8150_Freq_OutputOn()
        style.configure('freq.TButton', foreground='green')
        Button_Output_on_off_HM8150_Freq["text"] = "On"
    else:
        HM8150_Freq_OutputOff()
        style.configure('freq.TButton', foreground='black')
        Button_Output_on_off_HM8150_Freq["text"] = "Off"


def HM8150_Freq_Amplitude(amplitude):
    """
    Setze die Amplitude auf den angegebenen Wert
    :param amplitude: Amplitude 00.00 in [V]
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_frequency_generator, write_termination='\r', read_termination='\r')
    my_instrument.write('AMP:' + str(amplitude))
    my_instrument.write('DAM')
    my_instrument.close()
    print("Amplitude eingestellt: " + str(amplitude))


def HM8150_Freq_Frequenz(frequenz):
    """
    Setze die Frequenz auf den angegebenen Wert
    :param frequenz: Frequenz 0.0000 in [kHz]
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_frequency_generator, write_termination='\r', read_termination='\r')
    my_instrument.write('FRQ:' + str(frequenz))
    my_instrument.write('DFR')
    my_instrument.close()
    print("Frequenz eingestellt: " + str(frequenz))


def HM8150_Freq_Offset(offset):
    """
    Setze Offset auf den angegebenen Wert
    :param offset: Offset in [V]
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_frequency_generator, write_termination='\r', read_termination='\r')
    my_instrument.write('OFS:' + str(offset))
    my_instrument.write('DOF')
    my_instrument.close()
    print("Offset eingestellt: " + str(offset))


# Fluke Multimeter 8846a
def ConvertMessbereichToDecimalString():
    """
    Wandelt den ausgewählten Messbereich in eine Zahl für Verarbeitung vom FLUKE um
    :return: string Messbereich als Zahl ohne Einheit
    """
    match Combo_Messbereich_Fluke.get():
        case "100uA":
            return "0.000001"

        case "1mA":
            return "0.001"

        case "10mA":
            return "0.01"

        case "100mV" | "100mA":
            return "0.1"

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
    """
    Setze die Auswahl des Messbereichs abhängig von der ausgewählen Messgröße
    :param: string Messgröße
    """
    match messgroesse_eingestellt:
        case "DC V" | "AC V":
            print("Spannung")
            Combo_Messbereich_Fluke['values'] = fluke_Messbereich_Spannung
            Combo_Messbereich_Fluke.current(2)
            Fluke_set_Range()
        case "DC I" | "AC I":
            print("Strom")
            Combo_Messbereich_Fluke['values'] = fluke_Messbereich_Strom
            Combo_Messbereich_Fluke.current(2)
            Fluke_set_Range()
        case "Widerstand":
            print("Widerstand")
            Combo_Messbereich_Fluke['values'] = fluke_Messbereich_Widerstand
            Combo_Messbereich_Fluke.current(2)
            Fluke_set_Range()


def Widgets_sperren():
    """
    Sperre alle Eingabe-/Auswahl-Widgets während der Messung
    """
    Eingabe_Spannung_links_HM8143_Quelle.configure(state='disabled')
    Eingabe_Spannung_rechts_HM8143_Quelle.configure(state='disabled')
    Eingabe_Strom_links_HM8143_Quelle.configure(state='disabled')
    Button_on_off_HM8143_Quelle.configure(state='disabled')
    Eingabe_Strom_rechts_HM8143_Quelle.configure(state='disabled')
    Combo_Wellenform_HM8150_Freq.configure(state='disabled')
    Eingabe_Amplitude_HM8150_Freq.configure(state='disabled')
    Eingabe_Frequenz_HM8150_Freq.configure(state='disabled')
    Eingabe_Offset_HM8150_Freq.configure(state='disabled')
    Button_Output_on_off_HM8150_Freq.configure(state='disabled')
    Button_Offset_on_off_HM8150_Freq.configure(state='disabled')
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
    Button_Geraete_lokal.configure(state='disabled')
    Eingabe_Parameter.configure(state='disabled')
    Button_x_Achse_toggle.configure(state='disabled')
    Button_y_Achse_toggle.configure(state='disabled')


def Widgets_entsperren():
    """
    Entsperre alle Eingabe-/Auswahl-Widgets nach der Messung
    """
    Eingabe_Spannung_links_HM8143_Quelle.configure(state='normal')
    Eingabe_Spannung_rechts_HM8143_Quelle.configure(state='normal')
    Eingabe_Strom_links_HM8143_Quelle.configure(state='normal')
    Button_on_off_HM8143_Quelle.configure(state='normal')
    Eingabe_Strom_rechts_HM8143_Quelle.configure(state='normal')
    Combo_Wellenform_HM8150_Freq.configure(state='normal')
    Eingabe_Amplitude_HM8150_Freq.configure(state='normal')
    Eingabe_Frequenz_HM8150_Freq.configure(state='normal')
    Eingabe_Offset_HM8150_Freq.configure(state='normal')
    Button_Output_on_off_HM8150_Freq.configure(state='normal')
    Button_Offset_on_off_HM8150_Freq.configure(state='normal')
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
    Button_Geraete_lokal.configure(state='normal')
    Eingabe_Parameter.configure(state='normal')
    Button_x_Achse_toggle.configure(state='normal')
    Button_y_Achse_toggle.configure(state='normal')


def Aktualisiere_Widgets_Parameter(event=None):
    """
    Bei der Auswahl eines Parameters aktualisiere die Auswahl von der Variable (damit nicht der gleiche Ausgang gleichzeitig als Variable und Parameter ausgewählt werden kann)
    """
    selected_variable = Combo_Variable.get()
    selected_parameter = Combo_Parameter.get()

    # Update options for Combo_Parameter
    updated_parameter_options = [item for item in parameter_options if item != selected_variable]
    Combo_Parameter['values'] = updated_parameter_options
    if selected_parameter not in updated_parameter_options:
        Combo_Parameter.set('')  # Reset if current value is no longer valid

    # Update options for Combo_Variable
    updated_variable_options = [item for item in variable_options if item != selected_parameter]
    Combo_Variable['values'] = updated_variable_options
    if selected_variable not in updated_variable_options:
        Combo_Variable.set('')  # Reset if current value is no longer valid

    match selected_parameter:
        case "Spannung links" | "Spannung rechts" | "Strom links" | "Strom rechts" | "Compliance links" | "Compliance rechts":
            # Combo_Parameter_Einteilung.current(3)
            Combo_Parameter_Einteilung.grid(column=0, row=5, sticky="W", padx=5, pady=1)
            Label_Parameter_Einteilung.grid(column=0, row=4, sticky="W", padx=5, pady=1)
            if Combo_Parameter_Einteilung.get() == "manuell":
                Eingabe_Parameter.grid(column=1, row=5, sticky="W", columnspan=3, padx=5, pady=1)
                Label_Eingabe_Parameter.grid(column=1, row=4, sticky="W", columnspan=3, padx=5, pady=1)

        case "ohne Parameter":
            Label_Startwert_Parameter.grid_forget()
            Label_Zielwert_Parameter.grid_forget()
            Label_Schritte_Parameter.grid_forget()
            Eingabe_Startwert_Parameter.grid_forget()
            Eingabe_Zielwert_Parameter.grid_forget()
            Eingabe_Schritte_Parameter.grid_forget()
            Label_Eingabe_Parameter.grid_forget()
            Eingabe_Parameter.grid_forget()
            Combo_Parameter_Einteilung.grid_forget()
            Label_Parameter_Einteilung.grid_forget()


def Aktualisiere_Widgets_Parameter_Eingabe(parameter_einteilung):
    """
    Aktiviere dynamisch die Widgets für die Einteilung der Parameter.
    linear, wurzelförmig, logarithmisch → aktiviere Start, Ziel, Schritte
    manuell → aktiviere Eingabefeld für Parameter
    """
    match parameter_einteilung:
        case "linear" | "wurzelförmig" | "logarithmisch":
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


def update_variable_options(event=None):
    """
    Bei der Auswahl einer Variable aktualisiere die Auswahl der Parameter (damit nicht der gleiche Ausgang gleichzeitig als Variable und Parameter ausgewählt werden kann)
    """
    selected_variable = Combo_Variable.get()
    selected_parameter = Combo_Parameter.get()

    # Update options for Combo_Parameter
    updated_parameter_options = [item for item in parameter_options if item != selected_variable]
    Combo_Parameter['values'] = updated_parameter_options
    if selected_parameter not in updated_parameter_options:
        Combo_Parameter.set('')  # Reset if current value is no longer valid

    # Update options for Combo_Variable
    updated_variable_options = [item for item in variable_options if item != selected_parameter]
    Combo_Variable['values'] = updated_variable_options
    if selected_variable not in updated_variable_options:
        Combo_Variable.set('')  # Reset if current value is no longer valid


def ConvertMessgroesseToSCPI():
    """
    Wandle die Auswahl der Messgröße in den SCPI-Befehl für FLUKE um (siehe Fluke Multimeter 8846a programming manual)
    """
    match Combo_Messgroesse_Fluke.get():
        case "DC V":
            return "CONF:VOLT:DC "
        case "AC V":
            return "CONF:VOLT:AC "
        case "DC I":
            return "CONF:CURR:DC "
        case "AC I":
            return "CONF:CURR:AC "
        case "Widerstand":
            return "CONF:RES "


def setIntegrationTime():
    """
    Bestimme abhängig von der Auswahl der Messgröße die Integrationszeit (aus LabView übernommen, s.a. Fluke Multimeter 8846a programming manual)
    """
    match Combo_Messgroesse_Fluke.get():
        case "DC V":
            return ":volt:dc:nplc 1"
        case "AC V":
            return ":volt:ac:band 200"
        case "DC I":
            return ":curr:dc:nplc 1"
        case "AC I":
            return ":curr:ac:band 200"
        case "Widerstand":
            return ":res:nplc 1"


def MessungStop():
    global messungStop
    print("STOP")
    messungStop = True


def Geraete_lokal_bedienen():
    """
    Sperre alle Widgets falls die lokale Bedienung ausgewählt wird oder entsperre wenn die lokale Bedienung ausgeschaltet wird
    """
    global geraete_lokal_on
    if geraete_lokal_on:
        # Wechsle zurück zu remote
        Eingabe_Spannung_links_HM8143_Quelle.configure(state='normal')
        Eingabe_Spannung_rechts_HM8143_Quelle.configure(state='normal')
        Eingabe_Strom_links_HM8143_Quelle.configure(state='normal')
        Button_on_off_HM8143_Quelle.configure(state='normal')
        Eingabe_Strom_rechts_HM8143_Quelle.configure(state='normal')
        Combo_Wellenform_HM8150_Freq.configure(state='normal')
        Eingabe_Amplitude_HM8150_Freq.configure(state='normal')
        Eingabe_Frequenz_HM8150_Freq.configure(state='normal')
        Eingabe_Offset_HM8150_Freq.configure(state='normal')
        Button_Output_on_off_HM8150_Freq.configure(state='normal')
        Button_Offset_on_off_HM8150_Freq.configure(state='normal')
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
        Eingabe_Parameter.configure(state='normal')
        style.configure('lokal.TButton', foreground='black')
        HM8143_Quelle_remoteOn()
    else:
        # Wechsle zu lokal
        Eingabe_Spannung_links_HM8143_Quelle.configure(state='disabled')
        Eingabe_Spannung_rechts_HM8143_Quelle.configure(state='disabled')
        Eingabe_Strom_links_HM8143_Quelle.configure(state='disabled')
        Button_on_off_HM8143_Quelle.configure(state='disabled')
        Eingabe_Strom_rechts_HM8143_Quelle.configure(state='disabled')
        Combo_Wellenform_HM8150_Freq.configure(state='disabled')
        Eingabe_Amplitude_HM8150_Freq.configure(state='disabled')
        Eingabe_Frequenz_HM8150_Freq.configure(state='disabled')
        Eingabe_Offset_HM8150_Freq.configure(state='disabled')
        Button_Output_on_off_HM8150_Freq.configure(state='disabled')
        Button_Offset_on_off_HM8150_Freq.configure(state='disabled')
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
        Eingabe_Parameter.configure(state='disabled')
        style.configure('lokal.TButton', foreground='green')
        HM8143_Quelle_AusgangOff()
        HM8150_Freq_OutputOff()
        HM8143_Quelle_remoteOff()

    # Zustand umschalten
    geraete_lokal_on = not geraete_lokal_on


def Parameter_bestimmen():
    """
    - **`linear`**:
     - Erstellt eine gleichmäßig verteilte Sequenz von Werten zwischen dem Start- und Zielwert mit `numpy.linspace`.

    - **`wurzelförmig`**:
     - Wendet eine wurzelförmige Beziehung an:
       - Die Start- und Zielwerte werden quadriert.
       - Eine Sequenz wird basierend auf den quadrierten Werten erstellt.
       - Anschließend werden die quadrierten Werte zurück in die Ursprungsdimension transformiert (Wurzel) und auf zwei Dezimalstellen gerundet.

    - **`logarithmisch`**:
     - Wendet eine logarithmische Beziehung an:
       - Die Start- und Zielwerte werden exponentiert.
       - Eine Sequenz wird basierend auf den logarithmischen Werten erstellt.
       - Anschließend erfolgt eine logarithmische Transformation der Werte, die ebenfalls auf zwei Dezimalstellen gerundet werden.

    - **`manuell`**:
     - Die Eingabe wird aus einem Textfeld gelesen und auf Basis eines Trennzeichens `;` in eine Liste umgewandelt.

    3. **Fehlende Parameter**:
       - Für den Fall, dass die Option `ohne Parameter` gewählt ist, gibt die Funktion `[1]` als Standardwert zurück.
    """
    match Combo_Parameter.get():
        case "Spannung links" | "Spannung rechts" | "Strom links" | "Strom rechts" | "Compliance links" | "Compliance rechts":
            match Combo_Parameter_Einteilung.get():
                case "linear":
                    return np.linspace(float(Eingabe_Startwert_Parameter.get()), float(Eingabe_Zielwert_Parameter.get()),
                                       num=int(Eingabe_Schritte_Parameter.get()))
                case "wurzelförmig":
                    i_min = np.square(float(Eingabe_Startwert_Parameter.get()))
                    i_max = np.square(float(Eingabe_Zielwert_Parameter.get()))
                    step = int(Eingabe_Schritte_Parameter.get())
                    i_vec = np.linspace(i_min, i_max, num=int(step))
                    para = np.sqrt(i_vec)
                    para = np.round(para, decimals=2)
                    return para
                case "logarithmisch":
                    i_min = np.exp(float(Eingabe_Startwert_Parameter.get()))
                    i_max = np.exp(float(Eingabe_Zielwert_Parameter.get()))
                    step = int(Eingabe_Schritte_Parameter.get())
                    i_vec = np.linspace(i_min, i_max, num=int(step))
                    para = np.log(i_vec)
                    para = np.round(para, decimals=2)
                    return para
                case "manuell":
                    return Eingabe_Parameter.get().split(";")
        case "ohne Parameter":
            return [1]


def make_headers_unique(heads):
    """Funktion, um doppelte Werte in headers eindeutig zu machen."""
    seen = {}  # Wörterbuch für bereits gesehene Werte
    unique_headers = []

    for header in heads:
        if header not in seen:
            seen[header] = 1  # Erster Auftritt des Headers
            unique_headers.append(header)
        else:
            seen[header] += 1  # Zähler für doppelte Header erhöhen
            unique_headers.append(f"{header}_{seen[header]}")  # Header eindeutig machen

    return unique_headers


def Create_table(headers_para, var):
    """
    Initialisiert die Anzeige (Tabelle) der Messwerte.
    :param headers_para: Überschriften der Spalten
    :param var: Berechneten/bestimmten Variablen (erste Spalte)
    """
    global Tabelle
    global h_scrollbar

    Tabelle.pack_forget()  # Tabelle vom Fenster löschen (wenn man mehrere Messungen nacheinander durchführt)
    h_scrollbar.pack_forget()

    for i in Tabelle.get_children():  # Daten in Tabelle löschen damit bei erneuter Messung Tabelle leer ist
        Tabelle.delete(i)

    # Konfigurieren der ersten Spalte "#0" und setzen der Überschrift auf "Variable"
    Tabelle.column("#0", anchor=tk.CENTER, width=150, stretch=tk.NO)  # Zentrierte Ausrichtung
    Tabelle.heading("#0", text="Variable", anchor=tk.CENTER)  # Überschrift ebenfalls zentriert

    # Konfigurieren der restlichen Spalten aus der headers-Liste
    Tabelle['columns'] = headers_para
    for header in headers_para:
        Tabelle.column(header, anchor=tk.CENTER, width=100)  # Zentrierte Ausrichtung für zusätzliche Spalten
        Tabelle.heading(header, text=header, anchor=tk.CENTER)  # Überschrift

    # Platzhalter-Daten (in diesem Fall Zufallsdaten für zusätzliche Spalten)
    for i, variable in enumerate(var):
        Tabelle.insert(parent='', index='end', iid=i, text=f"{variable:.2f}", values=())  # Leere values-Liste

    # Tabelle und Scrollbar anzeigen
    Tabelle.pack(fill='both', expand=True, padx=10, pady=10)
    h_scrollbar.pack(side='bottom', fill='x')
    Tabelle.configure(xscrollcommand=h_scrollbar.set)


def Wert_in_Tabelle_einfuegen(row_id, column, value):
    """
    Füge einen Messwert in die Tabelle ein.
    :param row_id: Zeilennummer wo der Messwert eingefügt werden soll
    :param column: Spalte wo der Messwert eingefügt werden soll
    :param value: Messwert der eingefügt werden soll
    """
    global Tabelle
    # Hier wird der Wert in eine spezifische Zelle gesetzt
    Tabelle.set(row_id, column=column, value=value)


def Save_Messdaten_to_File():
    """
    Öffnet ein Dialog zum Speichern der Messdaten. Format und Datentypen können über die config eingestellt werden
    """
    global messdaten
    global headers
    if messdaten.size > 0 and headers.size > 0:
        headers_string = ";".join(headers)
        messdaten_transponiert = np.transpose(messdaten)
        # Dialog zum Speichern des Exports öffnen
        file_path = filedialog.asksaveasfilename(defaultextension="."+config.format_export, filetypes=[(config.format_export+" files", "*."+config.format_export), ("All files", "*.*")])
        if file_path:
            # Datei öffnen und Matrix speichern
            np.savetxt(file_path, messdaten_transponiert, fmt=config.datentyp, delimiter=config.trennzeichen, header=headers_string, comments='')
            print(f"Numpy-Matrix wurde in {file_path} gespeichert.")


def Fluke_reset():
    """
    # This clears all error prior to initiating readings (siehe Fluke Multimeter 8846a programming manual).
    Verhindert leider nicht den sporadisch auftretenden Kommunikationsfehler.
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_multimeter, read_termination='\r\n', query_delay=0.21)
    my_instrument.write('*RST;*CLS;syst:local')
    my_instrument.close()


def Fluke_set_Range():
    """
    Aktiviert anhand von Messwert und Messbereich den dazugehörigen Messmodus vom Fluke
    """
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
    trig = ":TRIG:SOUR BUS" # Aus LabView übernommen
    # trig = ":TRIG:SOUR IMM"

    # Commands Fluke
    # Aufbau: ...Messgröße+Messbereich+Integrationszeit+Trigger

    messgroesse = ConvertMessgroesseToSCPI()
    messbereich = ConvertMessbereichToDecimalString()
    integrationszeit = setIntegrationTime().upper()
    print(messgroesse + messbereich + integrationszeit + trig)

    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_multimeter, read_termination='\r\n', query_delay=0.21)
    set_range = '*RST;*CLS;' + messgroesse + str(messbereich) + ';' + integrationszeit + ';' + trig
    print(set_range)
    my_instrument.write(set_range)
    # gemessener_wert = float(my_instrument.query(':INIT;*TRG;FETCH?')) # Wandle nach float und speichere gemessenen Wert
    # print("MESSUNG: " + str(gemessener_wert) + messgroesse)
    my_instrument.close()


def Fluke_Messe_Wert_live():
    """
    Messe Wert mit dem Fluke Multimeter und gebe den gemessenen Wert (Antwort vom Fluke) zurück.
    :return: float mit gemessenen Wert
    """
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource(config.address_multimeter, read_termination='\r\n', query_delay=0.3)
    gemessener_wert = float(my_instrument.query(':INIT;*TRG;FETCH?'))  # Wandle nach float und speichere gemessenen Wert
    my_instrument.close()

    return gemessener_wert


# Hauptfunktionen
def regulate_current_links(target_current: float, var_i, step_size=0.05, max_iterations=50, tolerance=0.001, max_voltage=30,
                     min_voltage=0.0, ):
    """
    Regelt die linke Spannung, um den Zielstrom (target_current) innerhalb der Toleranz und nach max_iterations zu erreichen.

    :param target_current: Der gewünschte Strom in A.
    :param var_i: Aktueller Var-Schritt (nur beim ersten Var wird Strombegrenzung gesetzt)
    :param step_size: Schrittweite, um die Spannung anzupassen.
    :param max_iterations: Maximale Anzahl an Regelversuchen.
    :param tolerance: Die zulässige Abweichung vom Zielstrom (±0.001 A).
    :param max_voltage: Maximale Spannung, die eingestellt werden kann.
    :param min_voltage: Minimale Spannung, die eingestellt werden kann.

    """

    def get_current():
        # Liest den aktuellen Strom und gibt ihn als float zurück
        current_strom = HM8143_Quelle_ZeigeStromLinks()
        return float(current_strom)

    if var_i == 0:
        HM8143_Quelle_StromBegrenzLinks(
            target_current + 0.001)  # Setze die Strombegrenzung auf den gewünschten Wert (zur Absicherung), 0.001 Offset wegen statischer Abweichung Anzeige ↔ Messung
        HM8143_Quelle_AusgangOn()
        step_size = 1
        sleep(0.3)

    # status = HM8143_Quelle_Status()[4:7]    # Lese Status Ausgang links aus (CC1, CV1 oder ---)
    current_voltage = HM8143_Quelle_ZeigeSpannungLinks()

    current = get_current()
    error = round((target_current - current), 3)
    if not HM8143_IstAusgangInCC(ausgang=1) and abs(
            error) <= tolerance:  # Wenn Strom bereits innerhalb der Toleranz ist → nichts machen (um Schwankungen zu verhindern sonst bei jeden MEsspunkt neue Einstellung)
        return None

    # Starte die Regelung der Spannung
    # if status == "CC1":     # Prüfe ob Ausgang links in Strombegrenzung ist
    #     current_voltage = float(HM8143_Quelle_ZeigeSpannungLinks())
    print("1Aktuelle Spannung: " + str(HM8143_Quelle_ZeigeSpannungLinks()) + "(SET " + str(
        HM8143_Quelle_ZeigeSpannungLinksGesetzt()) + "), Aktueller Strom: " + HM8143_Quelle_ZeigeStromLinks())
    HM8143_Quelle_SpannungLinks(current_voltage)  # Setze linke Quelle auf die Start-Spannung
    iterations = 0
    sleep(0.3)
    print("2Aktuelle Spannung: " + str(HM8143_Quelle_ZeigeSpannungLinks()) + "(SET " + str(
        HM8143_Quelle_ZeigeSpannungLinksGesetzt()) + "), Aktueller Strom: " + HM8143_Quelle_ZeigeStromLinks())
    while True:
        current = get_current()
        error = round((target_current - current), 3)

        # Wenn der Strom innerhalb der Toleranz ist, beenden, sonst Spannung anpassen basierend auf dem Fehler (P-Regler)
        if abs(error) <= tolerance or iterations == max_iterations:
            if HM8143_IstAusgangInCC(ausgang=1):
                print("CC 0.02 runter")
                current_voltage -= 0.01
                HM8143_Quelle_SpannungLinks(current_voltage)

            print(f"Strom {current} ~= Target {target_current}")
            # current_voltage += step_size # Beim Erreichen des Stroms noch ein Step machen um in die Strombegrenzung zu kommen
            # HM8143_Quelle_SpannungLinks(current_voltage)
            # print("Strom stabil bei "+HM8143_Quelle_ZeigeStromLinks()+" mit Spannung "+ str(HM8143_Quelle_ZeigeSpannungLinks()))
            break
        # else:
        #     # Strom zu niedrig → Spannung erhöhen
        #     current_voltage += step_size

        elif current < target_current:
            # print(f"Strom zu niedrig: {current} < Target {target_current} | Abweichung: {error} → erhöhe um {step_size}")
            # Strom zu niedrig → Spannung erhöhen
            current_voltage += step_size
            iterations += 1

        elif current > target_current or HM8143_IstAusgangInCC(ausgang=1):
            # print(f"Strom zu hoch: {current} > Target {target_current} | Abweichung: {error} -> verringere um {step_size}")
            # Strom zu hoch → Spannung erhöhen
            current_voltage -= step_size
            iterations += 1

        # Stellt sicher, dass der Wert von current_voltage immer im Bereich von min_voltage bis max_voltage liegt (optional)
        current_voltage = max(min_voltage, min(current_voltage, max_voltage))

        # Spannung einstellen
        HM8143_Quelle_SpannungLinks(current_voltage)
        sleep(0.3)

        # Optionale Ausgabe zur Überwachung
        print("(" + str(iterations) + "/"+ str(max_iterations) + ") Aktuelle Spannung: " + str(HM8143_Quelle_ZeigeSpannungLinks()) + "(SET " + str(
            HM8143_Quelle_ZeigeSpannungLinksGesetzt()) + "), Aktueller Strom: " + HM8143_Quelle_ZeigeStromLinks())


def regulate_current_rechts(target_current: float, var_i, step_size=0.05, max_iterations=50, tolerance=0.001, max_voltage=30,
                     min_voltage=0.0, ):
    """
    Regelt die linke Spannung, um den Zielstrom (target_current) innerhalb der Toleranz und nach max_iterations zu erreichen.

    :param target_current: Der gewünschte Strom in A.
    :param var_i: Aktueller Var-Schritt (nur beim ersten Var wird Strombegrenzung gesetzt)
    :param step_size: Schrittweite, um die Spannung anzupassen.
    :param max_iterations: Maximale Anzahl an Regelversuchen.
    :param tolerance: Die zulässige Abweichung vom Zielstrom (±0.001 A).
    :param max_voltage: Maximale Spannung, die eingestellt werden kann.
    :param min_voltage: Minimale Spannung, die eingestellt werden kann.

    """

    def get_current():
        # Liest den aktuellen Strom und gibt ihn als float zurück
        current_strom = HM8143_Quelle_ZeigeStromRechts()
        return float(current_strom)

    if var_i == 0:
        HM8143_Quelle_StromBegrenzRechts(
            target_current + 0.001)  # Setze die Strombegrenzung auf den gewünschten Wert (zur Absicherung), 0.001 Offset wegen statischer Abweichung Anzeige ↔ Messung
        HM8143_Quelle_AusgangOn()
        step_size = 1
        sleep(0.3)

    # status = HM8143_Quelle_Status()[4:7]    # Lese Status Ausgang rechts aus (CC1, CV1 oder ---)
    current_voltage = HM8143_Quelle_ZeigeSpannungRechts()

    current = get_current()
    error = round((target_current - current), 3)
    if not HM8143_IstAusgangInCC(ausgang=2) and abs(
            error) <= tolerance:  # Wenn Strom bereits innerhalb der Toleranz ist → nichts machen (um Schwankungen zu verhindern sonst bei jeden MEsspunkt neue Einstellung)
        return None

    # Starte die Regelung der Spannung
    # if status == "CC1":     # Prüfe ob Ausgang rechts in Strombegrenzung ist
    #     current_voltage = float(HM8143_Quelle_ZeigeSpannungRechts())
    print("1Aktuelle Spannung: " + str(HM8143_Quelle_ZeigeSpannungRechts()) + "(SET " + str(
        HM8143_Quelle_ZeigeSpannungRechtsGesetzt()) + "), Aktueller Strom: " + HM8143_Quelle_ZeigeStromRechts())
    HM8143_Quelle_SpannungRechts(current_voltage)  # Setze linke Quelle auf die Start-Spannung
    iterations = 0
    sleep(0.3)
    print("2Aktuelle Spannung: " + str(HM8143_Quelle_ZeigeSpannungRechts()) + "(SET " + str(
        HM8143_Quelle_ZeigeSpannungRechtsGesetzt()) + "), Aktueller Strom: " + HM8143_Quelle_ZeigeStromRechts())
    while True:
        current = get_current()
        error = round((target_current - current), 3)

        # Wenn der Strom innerhalb der Toleranz ist, beenden, sonst Spannung anpassen basierend auf dem Fehler (P-Regler)
        if abs(error) <= tolerance or iterations == max_iterations:
            if HM8143_IstAusgangInCC(ausgang=2):
                print("CC 0.02 runter")
                current_voltage -= 0.01
                HM8143_Quelle_SpannungRechts(current_voltage)

            print(f"Strom {current} ~= Target {target_current}")
            # current_voltage += step_size # Beim Erreichen des Stroms noch ein Step machen um in die Strombegrenzung zu kommen
            # HM8143_Quelle_SpannungRechts(current_voltage)
            # print("Strom stabil bei "+HM8143_Quelle_ZeigeStromRechts()+" mit Spannung "+ str(HM8143_Quelle_ZeigeSpannungRechts()))
            break
        # else:
        #     # Strom zu niedrig → Spannung erhöhen
        #     current_voltage += step_size

        elif current < target_current:
            # print(f"Strom zu niedrig: {current} < Target {target_current} | Abweichung: {error} -> erhöhe um {step_size}")
            # Strom zu niedrig → Spannung erhöhen
            current_voltage += step_size
            iterations += 1

        elif current > target_current or HM8143_IstAusgangInCC(ausgang=2):
            # print(f"Strom zu hoch: {current} > Target {target_current} | Abweichung: {error} -> verringere um {step_size}")
            # Strom zu hoch → Spannung erhöhen
            current_voltage -= step_size
            iterations += 1

        # Stellt sicher, dass der Wert von current_voltage immer im Bereich von min_voltage bis max_voltage liegt (optional)
        current_voltage = max(min_voltage, min(current_voltage, max_voltage))

        # Spannung einstellen
        HM8143_Quelle_SpannungRechts(current_voltage)
        sleep(0.3)

        # Optionale Ausgabe zur Überwachung
        print("(" + str(iterations) + "/"+ str(max_iterations) + ") Aktuelle Spannung: " + str(HM8143_Quelle_ZeigeSpannungRechts()) + "(SET " + str(
            HM8143_Quelle_ZeigeSpannungRechtsGesetzt()) + "), Aktueller Strom: " + HM8143_Quelle_ZeigeStromRechts())


def message_hinweis_strommessung(messgroesse_eingestellt, messbereich_eingestellt):
    """
    Die Funktion überprüft, ob eine Strommessung durchgeführt wird. Wenn beim Fluke als Messgröße "DC I"/"AC I" und/oder ein Messbereich >= 100mA
    ausgewählt wurde, wird eine Meldung ausgegeben, bei OK → True und bei Abbrechen → False
    :param messgroesse_eingestellt: ausgewählte Messgröße
    :param messbereich_eingestellt: ausgewählter Messbereich
    :return: Bool von der Interaktion mit dem AskOkCancel-Fenster
    """
    if messgroesse_eingestellt in ("DC I", "AC I") and messbereich_eingestellt in ("100mA", "1A", "3A", "10A"):
        return messagebox.askokcancel("Strommessung", "ACHTUNG, bei Strommessung die Verkabelung überprüfen, Kurzschlussgefahr! Ab "
                                                      "100mA auf richtigen Anschluss beim Fluke achten!")
    if messbereich_eingestellt in ("100mA", "1A", "3A", "10A"):
        return messagebox.askokcancel("Strommessung", "ACHTUNG, ab 100mA auf richtigen Anschluss beim Fluke achten!")
    if messgroesse_eingestellt in ("DC I", "AC I"):
        return messagebox.askokcancel("Strommessung", "ACHTUNG, bei Strommessung die Verkabelung überprüfen, Kurzschlussgefahr!")


def toggle_x_scale():
    """
    Wechselt die Skala der x-Achse zwischen linear und logarithmisch.
    """
    current_scale = ax.get_xscale()
    if current_scale == 'linear':
        ax.set_xscale('log')
        Button_x_Achse_toggle['text'] = "X-log"
    else:
        ax.set_xscale('linear')
        Button_x_Achse_toggle['text'] = "X-linear"
    canvas.draw()


def toggle_y_scale():
    """
    Wechselt die Skala der y-Achse zwischen linear und logarithmisch.
    """
    current_scale = ax.get_yscale()
    if current_scale == 'linear':
        ax.set_yscale('log')
        Button_y_Achse_toggle['text'] = "Y-log"
    else:
        ax.set_yscale('linear')
        Button_y_Achse_toggle['text'] = "Y-linear"
    canvas.draw()


def Messung():
    """
    Hauptfunktion, die beim Start der Messung ausgeführt wird:
    """
    Fluke_set_Range()
    HM8143_Quelle_remoteOn()
    HM8143_Quelle_AusgangOff()
    Widgets_sperren()

    Button_x_Achse_toggle['text'] = "X-linear"
    Button_y_Achse_toggle['text'] = "Y-linear"


    # Prüfe Eingabe der Werte für die Variable abhängig von dem ausgewählten Ausgang
    variable_check = Vali.validate_var_start_ziel_schrittweite(start=Eingabe_Startwert_Variable.get(), ziel=Eingabe_Zielwert_Variable.get(),
                                                          schrittweite=Eingabe_Schrittweite_Variable.get(), variable=Combo_Variable.get())

    if not variable_check[0]:
        messagebox.showerror("Variable ungültig", variable_check[1])
        Widgets_entsperren()
        return

    # Prüfe die eingegebenen Parameter, wenn die Auswahl nicht "ohne Parameter" ist, manuell wird separat geprüft
    if Combo_Parameter.get() != "ohne Parameter":
        if Combo_Parameter_Einteilung.get() in ("linear", "wurzelförmig", "logarithmisch"):
            parameter_check = Vali.validate_para_start_ziel_schritte(start=Eingabe_Startwert_Parameter.get(),
                                                                     ziel=Eingabe_Zielwert_Parameter.get(),
                                                                     schritte=Eingabe_Schritte_Parameter.get(),
                                                                     parameter=Combo_Parameter.get())
            if not parameter_check[0]:
                messagebox.showerror("Parameter ungültig", parameter_check[1])
                Widgets_entsperren()
                return

        if Combo_Parameter_Einteilung.get() == "manuell":
            parameter_check = Vali.validate_para_manuell(Eingabe_Parameter.get())

            if not parameter_check:
                messagebox.showerror("Parameter ungültig", "Eingabe ungültig, es dürfen nur Zahlen getrennt"
                                                           "durch ; eingegeben werden")
                Widgets_entsperren()
                return


    # Prüfe ob Strommessung durchgeführt wird, beim Abbrechen wird Messung gestoppt
    if not message_hinweis_strommessung(Combo_Messgroesse_Fluke.get(), Combo_Messbereich_Fluke.get()):
        Widgets_entsperren()
        return

    # Wandle die Eingaben in float um und erzeuge die Variablen anhand der Werte
    start = float(Eingabe_Startwert_Variable.get())
    schritt = float(Eingabe_Schrittweite_Variable.get())
    ziel = float(Eingabe_Zielwert_Variable.get())
    start_schritt_ziel = np.linspace(start, ziel, num=int((ziel - start) / schritt))
    start_schritt_ziel = np.round(start_schritt_ziel, decimals=2)

    global var_x    # Vor jeder Messung wird die nächste Variable zu der Liste hinzugefügt, damit der Plot live aufgebaut werden kann (x-Achse)
    global mess_y   # Nach jeder Messung wird der gemessene Wert zu der Liste hinzugefügt, damit der Plot live aufgebaut werden kann (y-Achse)
    global x_i  # Index in der Variablen-Liste für die while-Schleifen
    global messungStop  # Zur Prüfung des Stop-Buttons
    global messdaten    # Speicher für die komplette Messung inkl. Variable
    global headers  # Überschriften für die Tabelle, Plot und Export der Daten

    var_x = []
    mess_y = []
    x_i = 0
    messungStop = False

    para = Parameter_bestimmen()    # Erzeuge die Parameter anhand der ausgewählten Parametereinteilung

    # Initialisierung Progressbar
    messwerte_insgesamt = int((ziel - start) / schritt) * len(para)
    progressbar['maximum'] = messwerte_insgesamt  # Lege das Maximum von der Progressbar fest

    # Bestimme den Tabellenkopf
    match Combo_Parameter.get():
        case "Spannung links" | "Spannung rechts":
            if len(para) == 1:
                headers = [Combo_Messgroesse_Fluke.get()]
            else:
                headers = make_headers_unique([Combo_Messgroesse_Fluke.get() + "_param_" + str(i) + "V" for i in para])
        case "Strom links" | "Strom rechts" | "Compliance links" | "Compliance rechts":
            if len(para) == 1:
                headers = [Combo_Messgroesse_Fluke.get()]
            else:
                headers = make_headers_unique([Combo_Messgroesse_Fluke.get() + "_param_" + str(i) + "A" for i in para])
        case "ohne Parameter":
                headers = [Combo_Messgroesse_Fluke.get()]

    # Tabelle wird erstellt
    Create_table(headers, list(start_schritt_ziel))

    # Transponiere Variable und füge das als erste Spalte an die Messdaten
    messdaten = np.transpose(start_schritt_ziel)

    p_i = 0 # Index für den aktuellen Parameter in der Parameterliste für die Schleife
    progress = 0

    # Äußere Schleife für jeden Parameter-Wert (wenn ohne Parameter = 1 → ein Durchlauf)
    while (p_i < len(para)) and (not messungStop):  # gehe Parameter durch
        var_x = []
        mess_y = []
        x_i = 0
        para_now = para[p_i]

        # Setze die Werte aus der GUI und den Parameter abhängig von der Auswahl des Parameters
        if Combo_Parameter.get() != "ohne Parameter":
            match Combo_Parameter.get():
                case "Spannung links":
                    HM8143_Quelle_SpannungLinks(para_now)
                    HM8143_Quelle_StromBegrenzLinks(Eingabe_Strom_links_HM8143_Quelle.get())
                    HM8143_Quelle_AusgangOn()
                case "Spannung rechts":
                    HM8143_Quelle_SpannungRechts(para_now)
                    HM8143_Quelle_StromBegrenzRechts(Eingabe_Strom_rechts_HM8143_Quelle.get())
                    HM8143_Quelle_AusgangOn()
                case "Strom rechts":
                    HM8143_Quelle_SpannungLinks(0.01)  # Zur Sicherheit da bei Stromregulierung Ausgang eingeschaltet wird
                    HM8143_Quelle_SpannungRechts(0.01)  # Zur Sicherheit da bei Stromregulierung Ausgang eingeschaltet wird
                    regulate_current_rechts(target_current=float(para_now), var_i=x_i)
                    # HM8143_Quelle_StromBegrenzLinksCC(para_now)
                    HM8143_Quelle_AusgangOn()
                case "Strom links":
                    HM8143_Quelle_SpannungLinks(0.01)  # Zur Sicherheit da bei Stromregulierung Ausgang eingeschaltet wird
                    HM8143_Quelle_SpannungRechts(0.01)  # Zur Sicherheit da bei Stromregulierung Ausgang eingeschaltet wird
                    regulate_current_links(target_current=float(para_now), var_i=x_i)
                    # HM8143_Quelle_StromBegrenzLinksCC(para_now)
                    HM8143_Quelle_AusgangOn()
                case "Compliance links":
                    HM8143_Quelle_SpannungLinks(Eingabe_Spannung_links_HM8143_Quelle.get())
                    HM8143_Quelle_StromBegrenzLinks(float(para_now))
                    HM8143_Quelle_AusgangOn()
                case "Compliance rechts":
                    HM8143_Quelle_SpannungRechts(Eingabe_Spannung_rechts_HM8143_Quelle.get())
                    HM8143_Quelle_StromBegrenzRechts(float(para_now))
                    HM8143_Quelle_AusgangOn()

        sleep(1)  # Wartezeit nach Setzen von Parametern

        # Setze die Variable anhand der Auswahl
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
                case "Frequenz":
                    HM8150_Freq_Frequenz(start_schritt_ziel[x_i,])
                    HM8150_Freq_OutputOn()
                case "Compliance links":
                    HM8143_Quelle_SpannungLinks(Eingabe_Spannung_links_HM8143_Quelle.get())
                    HM8143_Quelle_StromBegrenzLinks(start_schritt_ziel[x_i,])
                    HM8143_Quelle_AusgangOn()
                case "Compliance rechts":
                    HM8143_Quelle_SpannungRechts(Eingabe_Spannung_rechts_HM8143_Quelle.get())
                    HM8143_Quelle_StromBegrenzRechts(start_schritt_ziel[x_i,])
                    HM8143_Quelle_AusgangOn()

            # Stromsteuerung während der Messreihe (Strom wird nach jeder Variablen nachgeregelt) + Fehlerbehandlung
            if Combo_Parameter.get() != "ohne Parameter":
                match Combo_Parameter.get():
                    case "Strom links":
                        try:
                            regulate_current_links(target_current=float(para_now), var_i=x_i)
                        except Exception as e:
                            messungStop = True
                            messagebox.showerror("HM8143 Spannungsquelle Kommunikationsfehler",
                                                 "Fehler bei der Kommunikation mit "
                                                 "HM8143 Spannungsquelle (Gerät ist ausgeschaltet oder nicht erreichbar)")
                            break  # Verlässt die Mess-Schleife
                        # HM8143_Quelle_StromBegrenzLinksCC(para_now)
                        # HM8143_Quelle_AusgangOn()
                    case "Strom rechts":
                        try:
                            regulate_current_rechts(target_current=float(para_now), var_i=x_i)
                        except Exception as e:
                            messungStop = True
                            messagebox.showerror("HM8143 Spannungsquelle Kommunikationsfehler",
                                                 "Fehler bei der Kommunikation mit "
                                                 "HM8143 Spannungsquelle (Gerät ist ausgeschaltet oder nicht erreichbar)")
                            break  # Verlässt die Mess-Schleife

                        # HM8143_Quelle_StromBegrenzLinksCC(para_now)
                        # HM8143_Quelle_AusgangOn()

            # Wartezeit zwischen Messungen einstellbar
            messdelay = config.delay_messung/float(Combo_Messdelay.get()[1:])
            sleep(messdelay)

            # Speichere Daten und aktualisiere Plot
            ax.clear()
            ax.grid()

            # Ab den zweiten Parameter, gib die Plots von allen Parametern, die vorher durchlaufen wurden, aus
            for p_fertig in range(p_i):
                ax.plot(start_schritt_ziel, messdaten[p_fertig + 1, :], '--.', linewidth=0.4, markersize=1)
                canvas.draw()
            var_x.append(start_schritt_ziel[x_i,])

            # Fluke Messung mit Fehlerbehandlung, falls die Kommunikation mit dem Fluke unterbrochen wird
            try:
                wert_gemessen = Fluke_Messe_Wert_live() # FLUKE MESSE WERT
            except Exception as e:
                messungStop = True
                messagebox.showerror("FLUKE Kommunikationsfehler", "Fehler bei der Kommunikation mit "
                                                                   "Fluke Multimeter 8846A")
                Fluke_reset()   # Zum Testen, damit nach einer Exception der Fehlerspeicher vom Fluke gelöscht wird
                break  # Verlässt die Mess-Schleife

            # DEBUG Ausgabe auf Konsole
            try:
                print("------------------------------------------------------------------------------------")
                print("(" + str(progress + 1) + "/" + str(messwerte_insgesamt) + ") VAR:" +
                      str(start_schritt_ziel[x_i,]) + " FLUKE:" +
                      str(wert_gemessen) + " U1:" +
                      str(HM8143_Quelle_ZeigeSpannungLinks()) + "V(SET " +
                      str(HM8143_Quelle_ZeigeSpannungLinksGesetzt()) + ") I1:" +
                      str(HM8143_Quelle_ZeigeStromLinks()) + "A U2:" +
                      str(HM8143_Quelle_ZeigeSpannungRechts()) + "V(SET " +
                      str(HM8143_Quelle_ZeigeSpannungRechtsGesetzt()) + ") I2:" +
                      str(HM8143_Quelle_ZeigeStromRechts()) + "A")
            except Exception as e:
                messungStop = True
                messagebox.showerror("HM8143 Spannungsquelle Kommunikationsfehler", "Fehler bei der Kommunikation mit "
                                                                   "HM8143 Spannungsquelle (Gerät ist ausgeschaltet oder nicht erreichbar)")
                break  # Verlässt die Mess-Schleife

            # Füge Messwert an den aktuellen Messliste an
            mess_y.append(wert_gemessen)

            # Füge Messwert in Tabelle ein
            Wert_in_Tabelle_einfuegen(row_id=x_i, column=headers[p_i], value=wert_gemessen)  # Tabelle Live
            # Plotte alle bis zu dem Messzeitpunkt gemessenen Werte über der Variable
            ax.plot(var_x, mess_y, marker=".", markersize=3, linewidth=1)
            ax.set_xlabel(Combo_Variable.get())
            ax.set_ylabel('Fluke ' + Combo_Messgroesse_Fluke.get())
            # Aktualisiere Plot (nötig da eingebunden in Tkinter)
            canvas.draw()
            master.update()
            # Erhöhe die Durchlaufvariable und aktualisiere den Fortschrittsbalken
            x_i += 1
            progress += 1
            progressbar['value'] = progress  # Progress um eins erweitern

        # Wenn Messung nicht gestoppt wurde, soll die Parameter-Durchlaufvariable erhöht werden
        if not messungStop:
            messdaten = np.vstack((messdaten, mess_y))  # Füge den durchlauf zu den Messdaten hinzu
            p_i += 1


        # Wenn Messung gestoppt wird und mess_y weniger Werte als Zeilen in messdaten hat, werden die fehlenden Werte mit -1 aufgefüllt
        if messungStop and (len(mess_y) < len(start_schritt_ziel)):
            # Fehlende Länge berechnen
            missing_length = len(start_schritt_ziel) - len(mess_y)

            # Auffüllen mit -1
            mess_y.extend([-1] * missing_length)
            # Füge die aufgefüllte Messreihe an die Messdaten an
            messdaten = np.vstack((messdaten, mess_y))

    # Routine nach der letzten Messung
    ax.legend(headers)  # Füge Legende aus den Tabellenköpfen ein
    canvas.draw()   # Aktualisiere Plot
    headers = np.append(['Variable'], headers)  # Füge Bezeichner Variable an Kopf an
    HM8143_Quelle_AusgangOff()
    HM8150_Freq_OutputOff()
    Widgets_entsperren()


# ---------------------------------------------------------------------------------------------------------------------------------------------------
headers = np.array([])  # Überschriften für die Tabelle, Plot und Export der Daten
messdaten = np.array([])    # Speicher für die komplette Messung inkl. Variable
x_i = 0 # Index in der Variablen-Liste für die while-Schleifen
var_x = []  # Vor jeder Messung wird die nächste Variable zu der Liste hinzugefügt, damit der Plot live aufgebaut werden kann (x-Achse)
mess_y = [] # Nach jeder Messung wird der gemessene Wert zu der Liste hinzugefügt, damit der Plot live aufgebaut werden kann (y-Achse)
messungStop = False # Zur Prüfung des Stop-Buttons
geraete_lokal_on = False # Zur Prüfung des Geräte-lokal-bedienen-Buttons

# Vordefinierte Werte für die Breite und Höhe des Hauptfensters
window_height = config.window_height
window_width = config.window_width

fluke_Messbereich_Spannung = ["100mV", "1V", "10V", "100V", "1000V"]
fluke_Messbereich_Strom = ["100uA", "1mA", "10mA", "100mA", "1A", "3A", "10A"]
fluke_Messbereich_Widerstand = ["10 Ohm", "100 Ohm", "1k Ohm", "10k Ohm", "100k Ohm", "1M Ohm", "100M Ohm", "1G Ohm"]
variable_options = ["Spannung links", "Spannung rechts", "Compliance links", "Compliance rechts", "Frequenz"]

# Prüfe, ob die Pseudostromquelle in der Parameterauswahl angezeigt werden soll
if config.pseudostromquelle_active:
    parameter_options = ["Spannung links", "Spannung rechts", "Strom links", "Strom rechts", "Compliance links", "Compliance rechts", "ohne Parameter"]
    default_parameter = 6
    strom_tooltip = ("Hier wird der Parameter ausgewählt (bleibt während einer Messreihe konstant).\n"
                     "- die Variablen werden für jeden Parameter wiederholt durchlaufen.\n- der Wert in dem entsprechenden "
                     "Bedienelement wird ignoriert.\nACHTUNG: Wenn hier Ströme unter 10mA eingestellt werden, könnte es "
                     "zu einer unpräzisen Regelung kommen. (Pseudostromquelle)")

else:
    parameter_options = ["Spannung links", "Spannung rechts", "Compliance links", "Compliance rechts", "ohne Parameter"]
    default_parameter = 4
    strom_tooltip = ("Hier wird der Parameter ausgewählt (bleibt während einer Messreihe konstant).\n"
                     "- die Variablen werden für jeden Parameter wiederholt durchlaufen.\n- der Wert in dem entsprechenden "
                     "Bedienelement wird ignoriert.")

# #####################################################################################################################


# Instanziiere das Hauptfenster'
master = tk.Tk()    # Erzeuge das Hauptfenster
# master.geometry("1500x560")
master.geometry(str(window_width) + "x" + str(window_height))   # Parametrisiere das Hauptfenster
master.title("HalbleiterLeitTechnik")

# Funktionen für die direkte Validierung der Eingaben innerhalb der Spezifikationen von der HAMEG Spannungsquelle
vcmd_voltage = master.register(Vali.validation_entry_voltage)
vcmd_current = master.register(Vali.validation_entry_current)

# Erzeuge die Subframes im Hauptfenster
Frame_Steuerung = ttk.Frame(master)
Frame_Plot = ttk.Frame(master)
Frame_Tabelle = ttk.Frame(master)

# Platziere die Subframes
Frame_Steuerung.place(x=0, y=0, relwidth=0.23, relheight=1)
Frame_Plot.place(relx=0.23, y=0, relwidth=0.45, relheight=1)
Frame_Tabelle.place(relx=0.68, y=0, relwidth=0.32, relheight=1)

Tabelle = ttk.Treeview(Frame_Tabelle, selectmode='browse')
h_scrollbar = ttk.Scrollbar(Frame_Tabelle, orient=tk.HORIZONTAL, command=Tabelle.xview)

# Für die dynamische Einfärbung der Buttons (on/off)
style = ttk.Style()

# Lokal
Frame_Lokal = ttk.Frame(Frame_Steuerung)
Button_Geraete_lokal = ttk.Button(Frame_Lokal, text="Geräte lokal bedienen", style='lokal.TButton', command=Geraete_lokal_bedienen)
ToolTip(Button_Geraete_lokal, text="Schaltet zwischen remote (Bedienelemente an den Gerätet sind gesperrt) und lokal um")

# Lokal Design
Frame_Lokal.pack(fill='x')
Button_Geraete_lokal.pack(padx=10, pady=10)

# HM8143 Power
Frame_HM8143_Quelle = ttk.LabelFrame(Frame_Steuerung, text="Spannungsquelle HM8143")

Label_Spannung_links_HM8143_Quelle = ttk.Label(Frame_HM8143_Quelle, text="Spannung links")
Label_Spannung_rechts_HM8143_Quelle = ttk.Label(Frame_HM8143_Quelle, text="Spannung rechts")

Eingabe_Spannung_links_HM8143_Quelle = ttk.Entry(Frame_HM8143_Quelle, width=7, validate="key", validatecommand=(vcmd_voltage, "%P"))
Eingabe_Spannung_links_HM8143_Quelle.insert(0, "0.5")
ToolTip(Eingabe_Spannung_links_HM8143_Quelle, text="Setzt die Ausgangsspannung des linken Ausgangs: 0 - 30 [V]")
Eingabe_Spannung_links_HM8143_Quelle.bind("<FocusOut>", (lambda event: HM8143_Quelle_SpannungLinks(Eingabe_Spannung_links_HM8143_Quelle.get())))
Eingabe_Spannung_rechts_HM8143_Quelle = ttk.Entry(Frame_HM8143_Quelle, width=7, validate="key", validatecommand=(vcmd_voltage, "%P"))
ToolTip(Eingabe_Spannung_rechts_HM8143_Quelle, text="Setzt die Ausgangsspannung des rechten Ausgangs: 0 - 30 [V]")
Eingabe_Spannung_rechts_HM8143_Quelle.insert(0, "0.5")
Eingabe_Spannung_rechts_HM8143_Quelle.bind("<FocusOut>", (lambda event: HM8143_Quelle_SpannungRechts(Eingabe_Spannung_rechts_HM8143_Quelle.get())))

Label_Strom_links_HM8143_Quelle = ttk.Label(Frame_HM8143_Quelle, text="Strom links")
Label_Strom_rechts_HM8143_Quelle = ttk.Label(Frame_HM8143_Quelle, text="Strom rechts")

Eingabe_Strom_links_HM8143_Quelle = ttk.Entry(Frame_HM8143_Quelle, width=7, validate="key", validatecommand=(vcmd_current, "%P"))
Eingabe_Strom_links_HM8143_Quelle.insert(0, "0.015")
ToolTip(Eingabe_Strom_links_HM8143_Quelle, text="Setzt die Strombegrenzung des linken Ausgangs: 0 - 2 [A] \n "
                                               "ACHTUNG: Bei mehr als 0.095A muss auf den richtigen Anschluss beim Fluke geachtet werden!")
Eingabe_Strom_links_HM8143_Quelle.bind("<FocusOut>", (lambda event: HM8143_Quelle_StromBegrenzLinks(Eingabe_Strom_links_HM8143_Quelle.get())))
Button_on_off_HM8143_Quelle = ttk.Button(Frame_HM8143_Quelle, text="Off", style='quelle.TButton', command=HM8143_Quelle_Toggle_Ausgang)
ToolTip(Button_on_off_HM8143_Quelle, text="Schaltet die Ausgänge des Netzgerätes an und aus")
Eingabe_Strom_rechts_HM8143_Quelle = ttk.Entry(Frame_HM8143_Quelle, width=7, validate="key", validatecommand=(vcmd_current, "%P"))
Eingabe_Strom_rechts_HM8143_Quelle.insert(0, "1.0")
ToolTip(Eingabe_Strom_rechts_HM8143_Quelle, text="Setzt die Strombegrenzung des rechten Ausgangs: 0 - 2 [A] \n "
                                                "ACHTUNG: Bei mehr als 0.095A muss auf den richtigen Anschluss beim Fluke geachtet werden!")
Eingabe_Strom_rechts_HM8143_Quelle.bind("<FocusOut>", (lambda event: HM8143_Quelle_StromBegrenzRechts(Eingabe_Strom_rechts_HM8143_Quelle.get())))

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
ToolTip(Combo_Wellenform_HM8150_Freq, text="Setzt die Wellenform des Funktionsgenerators. "
                                          "Es kann zwischen Sinus, Rechteck, Dreieck, Puls, und Sägezahn ausgewählt werden.")

Combo_Wellenform_HM8150_Freq.bind("<<ComboboxSelected>>", (lambda event: HM8150_Freq_Wellenform(Combo_Wellenform_HM8150_Freq.get())))

Eingabe_Amplitude_HM8150_Freq = ttk.Entry(Frame_HM8150_Freq, width=7)
Eingabe_Amplitude_HM8150_Freq.insert(0, "0.5")
ToolTip(Eingabe_Amplitude_HM8150_Freq, text="Legt die Amplitude des ausgegebenen Signals fest. \nACHTUNG: Der hier eingegebene Wert ist die "
                                           "Spitze-Spitze-Spannung UPP des Ausgangssignals! Die tatsächliche Amplitude ist nur halb so hoch. Wenn das"
                                           " eingestellte Signal auf den Modulationseingang des Hameg Netzteils gelegt wird, "
                                           "dürfen maximal 10 V für UPP eingestellt werden. Sonst kann es zur Beschädigung der Geräte kommen.")

Eingabe_Amplitude_HM8150_Freq.bind("<FocusOut>", (lambda event: HM8150_Freq_Amplitude(Eingabe_Amplitude_HM8150_Freq.get())))
Eingabe_Frequenz_HM8150_Freq = ttk.Entry(Frame_HM8150_Freq, width=7)
Eingabe_Frequenz_HM8150_Freq.insert(0, "1000")
ToolTip(Eingabe_Frequenz_HM8150_Freq, text="Legt die Frequenz des Ausgangssignals fest. Diese sollte bei Wechselstrommessung "
                                          "im Bereich zwischen 200 Hz und 10 kHz liegen. Bei Wechselspannungsmessungen "
                                          "kann die Frequenz zwischen 200 Hz und 8 kHz liegen. (Messbereichsgrenzen des Fluke) \n"
                                          "ACHTUNG: Wenn das eingestellte Signal auf den Modulationseingang des Hameg "
                                          "Netzteils gelegt wird, dürfen maximal 50 kHz eingestellt werden. Sonst kann es zur "
                                          "Beschädigung der Geräte kommen.")

Eingabe_Frequenz_HM8150_Freq.bind("<FocusOut>", (lambda event: HM8150_Freq_Frequenz(Eingabe_Frequenz_HM8150_Freq.get())))
Eingabe_Offset_HM8150_Freq = ttk.Entry(Frame_HM8150_Freq, width=7)
Eingabe_Offset_HM8150_Freq.insert(0, "0")
ToolTip(Eingabe_Offset_HM8150_Freq, text="Hier kann der Wert des Gleichspannungsanteils eingetragen werden, welcher zum "
                                        "Signal hinzuaddiert wird.")
Eingabe_Offset_HM8150_Freq.bind("<FocusOut>", (lambda event: HM8150_Freq_Offset(Eingabe_Offset_HM8150_Freq.get())))

Label_Output_Button_HM8150_Freq = ttk.Label(Frame_HM8150_Freq, text="Output")
Label_Offset_Button_HM8150_Freq = ttk.Label(Frame_HM8150_Freq, text="Offset")
Button_Output_on_off_HM8150_Freq = ttk.Button(Frame_HM8150_Freq, text="Off", style='freq.TButton', command=HM8150_Freq_Toggle_Output)
ToolTip(Button_Output_on_off_HM8150_Freq, text="Schaltet den Ausgang den Funktionsgenerators an bzw. aus")
Button_Offset_on_off_HM8150_Freq = ttk.Button(Frame_HM8150_Freq, text="Off", command=HM8150_Freq_Toggle_Offset)
ToolTip(Button_Offset_on_off_HM8150_Freq, text="Schaltet den Gleichspannungsanteil an bzw. aus")


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
    values=["DC V", "AC V", "DC I", "AC I", "Widerstand"],
    width=18
)
Combo_Messgroesse_Fluke.current(2)
ToolTip(Combo_Messgroesse_Fluke, text="Hier kann zwischen einer Gleichspanungs-, Wechselspannungs, Gleichsstrom-, "
                                    "Wechselstrom und einer Widerstandsmessung gewählt werden.\n"
                                    "ACHTUNG: Bei einer Strommessung muss auf den richtigen Anschluss des Fluke "
                                    "geachtet werden!")

Combo_Messgroesse_Fluke.bind("<<ComboboxSelected>>", (lambda event: Fluke_bestimme_Messbereich(Combo_Messgroesse_Fluke.get())))

Combo_Messbereich_Fluke = ttk.Combobox(
    Frame_Fluke,
    state="readonly",
    values=fluke_Messbereich_Strom,
    width=10
)

Combo_Messbereich_Fluke.current(2)
ToolTip(Combo_Messbereich_Fluke, text="Hier wird der Messbereich des Multimeters bestimmt. Die Auswahlmöglichkeiten "
                                    "sind hier von der Messgröße abhängig.\n"
                                    "ACHTUNG: Bei einer Strommessung mit einem Messbereich über 100mA muss der "
                                    "entsprechende Anschluss am Fluke gewählt werden!")

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
    values=variable_options,
    width=17
)
Combo_Variable.current(0)
ToolTip(Combo_Variable, text="Hier wird der für die Messung zu variierende Variable bestimmt. Der Wert in dem entsprechenden "
                     "Bedienelement wird ignoriert.")

Combo_Variable.bind("<<ComboboxSelected>>", update_variable_options)

Eingabe_Startwert_Variable = ttk.Entry(Frame_Messung, width=6)
Eingabe_Startwert_Variable.insert(0, "0")
ToolTip(Eingabe_Startwert_Variable, text="Bei diesem Wert wird der erste Messpunkt der Kennlinie aufgenommen.")
Eingabe_Schrittweite_Variable = ttk.Entry(Frame_Messung, width=6)
Eingabe_Schrittweite_Variable.insert(0, "0.2")
ToolTip(Eingabe_Schrittweite_Variable, text="Hier wird der Abstand zwischen zwei Messpunkten (Variable) eingegeben.")
Eingabe_Zielwert_Variable = ttk.Entry(Frame_Messung, width=6)
Eingabe_Zielwert_Variable.insert(0, "2")
ToolTip(Eingabe_Zielwert_Variable, text="Hier wird der Maximalwert der Variable angegeben.\nACHTUNG: Der Zielwert muss größer als der Startwert sein.")

Label_Auswahl_Parameter = tk.Label(Frame_Messung, text="Parameter")
Label_Eingabe_Parameter = tk.Label(Frame_Messung, text="Parameter mit ; getrennt (z.B. 1;1.5;2)")


Combo_Parameter = ttk.Combobox(
    Frame_Messung,
    state="readonly",
    values=parameter_options,
    width=17
)
Combo_Parameter.current(default_parameter)
ToolTip(Combo_Parameter, text=strom_tooltip)

Combo_Parameter.bind("<<ComboboxSelected>>", Aktualisiere_Widgets_Parameter)

Label_Parameter_Einteilung = tk.Label(Frame_Messung, text="Parameter Einteilung")

Label_Startwert_Parameter = tk.Label(Frame_Messung, text="Startwert")
Label_Zielwert_Parameter = tk.Label(Frame_Messung, text="Zielwert")
Label_Schritte_Parameter = tk.Label(Frame_Messung, text="Schritte")

Eingabe_Startwert_Parameter = ttk.Entry(Frame_Messung, width=6)
Eingabe_Startwert_Parameter.insert(0, "1")
ToolTip(Eingabe_Startwert_Parameter, text="Startwert bei linear, wurzelförmiger und logarithmischer Einteilung")
Eingabe_Zielwert_Parameter = ttk.Entry(Frame_Messung, width=6)
Eingabe_Zielwert_Parameter.insert(0, "8")
ToolTip(Eingabe_Zielwert_Parameter, text="Zielwert bei linear, wurzelförmiger und logarithmischer Einteilung")
Eingabe_Schritte_Parameter = ttk.Entry(Frame_Messung, width=6)
Eingabe_Schritte_Parameter.insert(0, "1")
ToolTip(Eingabe_Schritte_Parameter, text="Anzahl der Werte bei linear, wurzelförmiger und logarithmischer Einteilung")

Combo_Parameter_Einteilung = ttk.Combobox(
    Frame_Messung,
    state="readonly",
    values=["linear", "wurzelförmig", "logarithmisch", "manuell"],
    width=15
)
Combo_Parameter_Einteilung.current(3)
ToolTip(Combo_Parameter_Einteilung, text="Hier wird die Aufteilung der Parameter bestimmt.\n\n"
                                        "linear: Erzeugt die eingestellte Anzahl (Schritte) der Parameter zwischen "
                                        "den Start- und Zielwert.\n\nwurzelförmig: Quadriert den Start- und Zielwert, "
                                        "generiert die festgelegte Anzahl von Parametern (Schritten) zwischen den "
                                        "quadrierten Werten und nimmt anschließend die Wurzel der erzeugten Werte.\n\n"
                                        "logarithmisch: Exponenziert den Start- und Zielwert, generiert die festgelegte "
                                        "Anzahl von Parametern (Schritten) zwischen den Exponentialwerten und berechnet "
                                        "den Logarithmus der Werte.\n\n"
                                        "manuell: Die gewünschten Parameter können manuell eingegeben werden.", delay=1, show_duration=1)

Combo_Parameter_Einteilung.bind("<<ComboboxSelected>>", (lambda event: Aktualisiere_Widgets_Parameter_Eingabe(Combo_Parameter_Einteilung.get())))

Eingabe_Parameter = ttk.Entry(Frame_Messung, width=32)
ToolTip(Eingabe_Parameter, text="Hier können Parameter manuell mit einem Semikolon ; getrennt eingegeben werden z.B 1;1.5;2")

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

Combo_Messdelay = ttk.Combobox(
    Frame_Messung,
    state="readonly",
    values=["x0.5", "x1", "x2", "x5", "x9"],
    width=5
)
Combo_Messdelay.current(3)
Combo_Messdelay.grid(column=0, row=6, padx=5, pady=3)
ToolTip(Combo_Messdelay, text="Messgeschwindigkeit (Wartezeit zwischen den Messungen): \n"
                             "x0.5 = 1,2s, x1 = 600ms, x2 = 300ms, x5 = 100ms, x9")

Button_Start_Messung.grid(column=1, row=6, padx=5, pady=3)
ToolTip(Button_Start_Messung, text="Hier wird die Messung gestartet. Die Ausgänge des Netzgerätes und des Frequenzgenerators werden automatisch "
                                  "angeschaltet, die eingestellte Variable jeweils für jeden Parameter variiert und an jedem Messpunkt ein Messwert "
                                  "aufgenommen.")
Button_Messdaten_Speichern.grid(column=2, row=6, padx=5, pady=3)
ToolTip(Button_Messdaten_Speichern, text="Speichert die Messwerte unter dem ausgewählten Pfad als ."+config.format_export)
Button_Stop_Messung.grid(column=3, row=6, padx=5, pady=3)
ToolTip(Button_Stop_Messung, text="Sollte sich bereits im Laufe der Messung herausstellen, dass die Daten fehlerhaft sind oder sonstige Komplikationen"
                                 " auftreten, kann die Messung hier vorzeitig abgebrochen werden.")


#   ################### INITIALISIERUNG GUI & HARDWARE   #######################
fig, ax = plt.subplots()
ax.grid()
ax.set_xscale('linear')  # Standardmäßig lineare Skalierung
ax.set_yscale('linear')  # Standardmäßig lineare Skalierung

canvas = FigureCanvasTkAgg(fig, master=Frame_Plot)  # Erzeuge Canvas für den Plot
canvas.get_tk_widget().pack(fill='both', expand=True)

Button_y_Achse_toggle = ttk.Button(Frame_Plot, text="Y-linear", command=toggle_y_scale)
Button_y_Achse_toggle.pack(side=tk.RIGHT, padx=3)

Button_x_Achse_toggle = ttk.Button(Frame_Plot, text="X-linear", command=toggle_x_scale)
Button_x_Achse_toggle.pack(side=tk.RIGHT, padx=3)

progressbar = ttk.Progressbar(Frame_Steuerung)
progressbar.pack(fill='x', expand=True)
toolbar = NavigationToolbar2Tk(canvas, Frame_Plot)

# Initialisiere Quelle HM8143 (setzte die default Werte aus den Entries)
HM8143_Quelle_SpannungLinks(Eingabe_Spannung_links_HM8143_Quelle.get())
HM8143_Quelle_SpannungRechts(Eingabe_Spannung_rechts_HM8143_Quelle.get())
HM8143_Quelle_StromBegrenzLinks(Eingabe_Strom_links_HM8143_Quelle.get())
HM8143_Quelle_StromBegrenzRechts(Eingabe_Strom_rechts_HM8143_Quelle.get())

# Initialisiere Frequenzgenerator HM8150 ohne Offset (setzte die default Werte aus der Combo und den Entries)
HM8150_Freq_Wellenform(Combo_Wellenform_HM8150_Freq.get())
HM8150_Freq_Amplitude(Eingabe_Amplitude_HM8150_Freq.get())
HM8150_Freq_Frequenz(Eingabe_Frequenz_HM8150_Freq.get())

# Initialisiere Fluke (setzte die default Werte aus der Combo und den Entries)
Fluke_set_Range()


def closing_cbk():
    """
    Zum ordentlichen Beenden des Programms, wenn man das Hauptfenster schließt
    """
    HM8143_Quelle_AusgangOff()
    HM8143_Quelle_remoteOff()
    HM8150_Freq_OutputOff()
    HM8150_Freq_remoteOff()
    Fluke_reset()

    # Shutdown procedure
    master.quit()
    master.destroy()


Aktualisiere_Widgets_Parameter()    # Damit die Widgets beim Start aktualisiert werden, sonst werden die Felder für Parametereinteilung usw. angezeigt

master.protocol("WM_DELETE_WINDOW", closing_cbk)

master.mainloop()
