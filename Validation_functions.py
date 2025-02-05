import re


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


def validate_var_para_start_ziel_schritt(value):
    """
    Validiert die Eingabefelder Start, Ziel, Schritte, Schrittweite. Nur positive Dezimalzahlen erlaubt.
    """
    try:
        if value == "":  # Leere Eingabe erlauben
            return True
        return float(value) >= 0  # Nur positive Zahlen erlaubt
    except ValueError:
        return False  # Falls kein gültiger float-Wert


def validate_para_manuell(value):
    """
    Validiert, ob die Eingabe eine Liste von Dezimalzahlen (inkl. 0), getrennt durch ';', ist.

    value: Neuer Wert im Entry-Widget (%P).
    """
    if value == "":  # Leere Eingabe zulassen
        return True

    # Erlaubt Zahlen mit optionalem Dezimalpunkt, getrennt durch ';'
    pattern = r"^\s*\d+(\.\d+)?(\s*;\s*\d+(\.\d+)?)*\s*$"

    # Prüfen, ob die Eingabe gültig ist
    return bool(re.fullmatch(pattern, value))
