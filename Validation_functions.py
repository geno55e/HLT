import tkinter as tk


def validation_entry_voltage(value):
    """
    Funktion zur Eingabeprüfung der Spannung.
    Akzeptiert nur Dezimalzahlen zwischen 0 und 30.
    """
    try:
        # Leere Eingabe (Löschen zulassen)
        if value == "":
            return True
        # Prüfen, ob die Eingabe eine gültige Dezimalzahl ist
        if float(value) >= 0 and float(value) <= 30:
            return True
        return False
    except ValueError:
        # Falls die Eingabe kein gültiger Float ist
        return False

def validation_entry_current(value):
    """
    Funktion zur Eingabeprüfung des Stromes.
    Akzeptiert nur Dezimalzahlen zwischen 0 und 2.
    """
    try:
        # Leere Eingabe (Löschen zulassen)
        if value == "":
            return True
        # Prüfen, ob die Eingabe eine gültige Dezimalzahl ist
        if float(value) >= 0 and float(value) <= 2:
            return True
        return False
    except ValueError:
        # Falls die Eingabe kein gültiger Float ist
        return False
