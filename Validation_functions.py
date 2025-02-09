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


def validate_var_start_ziel_schrittweite(start, schrittweite, ziel, variable):
    try:
        start = float(start)
        ziel = float(ziel)
        schrittweite = float(schrittweite)

        if schrittweite > (ziel - start):
            return False, "Es muss gelten: (Zielwert - Startwert) > Schrittweite"

        if variable in ["Spannung links", "Spannung rechts"]:
            if not (0 <= start <= 30 and 0 <= ziel <= 30 and 0 <= schrittweite <= 30 and ziel > start):
                return False, "Werte dürfen nur zwischen 0 und 30 liegen."
        elif variable in ["Compliance links", "Compliance rechts"]:
            if not (0 <= start <= 2 and 0 <= ziel <= 2 and 0 <= schrittweite <= 2 and ziel > start):
                return False, "Werte dürfen nur zwischen 0 und 2 liegen."
        elif variable == "Frequenz":
            if not (0.01 <= start <= 1250000000 and 0.01 <= ziel <= 1250000000 and 0.01 <= schrittweite <= 1250000000 and ziel > start):
                return False, "Werte dürfen nur zwischen 0.01 und 1.25e9 liegen."

    except ValueError:
        return False, "Bitte gültige Zahlen eingeben."

    return True, None

def validate_para_start_ziel_schritte(start, schrittweite, ziel, parameter):
    try:
        start = float(start)
        ziel = float(ziel)
        schrittweite = float(schrittweite)

        if start > ziel:
            return False, "Es muss gelten: Zielwert > Startwert"

        if parameter in ["Spannung links", "Spannung rechts"]:
            if not (0 <= start <= 30 and 0 <= ziel <= 30 and 0 <= schrittweite <= 30 and ziel > start):
                return False, "Werte dürfen nur zwischen 0 und 30 liegen."
        elif parameter in ["Strom links", "Strom rechts"]:
            if not (0 <= start <= 2 and 0 <= ziel <= 2 and 0 <= schrittweite <= 2 and ziel > start):
                return False, "Werte dürfen nur zwischen 0 und 2 liegen."
    except ValueError:
        return False, "Bitte gültige Zahlen eingeben."

    return True, None


def validate_para_manuell(input_string: str) -> bool:
    pattern = r"^\d+(\.\d+)?(;(\d+(\.\d+)?))*$"
    return bool(re.fullmatch(pattern, input_string))
