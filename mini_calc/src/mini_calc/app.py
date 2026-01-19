# ===================================================================
# Mini-Rechner Anwendung mit Tkinter
# ===================================================================
# Diese Anwendung erstellt einen einfachen grafischen Taschenrechner,
# der die vier Grundrechenarten (Addition, Subtraktion, Multiplikation
# und Division) unterstützt.
# ===================================================================

# Import des tkinter-Moduls für die grafische Benutzeroberfläche (GUI)
import tkinter as tk


def calculate(op):
    """
    Führt eine mathematische Berechnung basierend auf dem übergebenen Operator aus.
    
    Diese Funktion liest die Werte aus den beiden Eingabefeldern,
    konvertiert sie in Fließkommazahlen und führt die entsprechende
    Rechenoperation aus.
    
    Parameter:
    ----------
    op : str
        Der mathematische Operator ('+', '-', '*' oder '/')
    
    Fehlerbehandlung:
    -----------------
    - ValueError: Wird ausgelöst, wenn die Eingabe keine gültige Zahl ist
    - Division durch Null: Wird gesondert behandelt und gibt eine Fehlermeldung aus
    """
    try:
        # Einlesen und Konvertieren der ersten Zahl aus dem Eingabefeld entry_a
        a = float(entry_a.get())
        
        # Einlesen und Konvertieren der zweiten Zahl aus dem Eingabefeld entry_b
        b = float(entry_b.get())
        
        # Überprüfung des Operators und Durchführung der entsprechenden Berechnung
        if op == '+':
            # Addition: a + b
            result.set(a + b)
        elif op == '-':
            # Subtraktion: a - b
            result.set(a - b)
        elif op == '*':
            # Multiplikation: a * b
            result.set(a * b)
        elif op == '/':
            # Division: a / b
            # Sonderprüfung: Division durch Null wird verhindert
            # Wenn b ungleich 0 ist, wird die Division durchgeführt
            # Ansonsten wird eine Fehlermeldung angezeigt
            result.set(a / b if b != 0 else "Fehler: ÷0")
    except ValueError:
        # Fehlerbehandlung für ungültige Eingaben (z.B. Text statt Zahlen)
        result.set("Ungültige Eingabe")


# ===================================================================
# Hauptfenster erstellen und konfigurieren
# ===================================================================

# Erstellen des Hauptfensters (Root-Widget) der Tkinter-Anwendung
root = tk.Tk()

# Setzen des Fenstertitels, der in der Titelleiste angezeigt wird
root.title("Mini-Rechner")

# ===================================================================
# Eingabefelder erstellen
# ===================================================================

# Erstellen des ersten Eingabefeldes für die erste Zahl
entry_a = tk.Entry(root)

# Erstellen des zweiten Eingabefeldes für die zweite Zahl
entry_b = tk.Entry(root)

# Positionierung des ersten Eingabefeldes im Grid-Layout
# row=0: erste Zeile, column=0: erste Spalte
# padx und pady fügen Abstände (Padding) um das Widget herum hinzu
entry_a.grid(row=0, column=0, padx=5, pady=5)

# Positionierung des zweiten Eingabefeldes im Grid-Layout
# row=0: erste Zeile (gleiche Zeile wie entry_a), column=1: zweite Spalte
entry_b.grid(row=0, column=1, padx=5, pady=5)

# ===================================================================
# Ergebnis-Label erstellen
# ===================================================================

# Erstellen einer StringVar-Variable zur dynamischen Anzeige des Ergebnisses
# StringVar ist eine Tkinter-Variable, die automatisch das Label aktualisiert
result = tk.StringVar()

# Erstellen eines Labels zur Anzeige des Berechnungsergebnisses
# textvariable=result: Das Label zeigt den Inhalt der result-Variable an
# grid(row=1, ...): Zweite Zeile (unter den Eingabefeldern)
# columnspan=2: Das Label erstreckt sich über beide Spalten
tk.Label(root, textvariable=result).grid(row=1, column=0, columnspan=2)

# ===================================================================
# Operator-Buttons erstellen
# ===================================================================

# Schleife zur Erstellung der vier Operator-Buttons
# enumerate(['+', '-', '*', '/']) gibt uns sowohl den Index (i) als auch den Operator (op)
for i, op in enumerate(['+', '-', '*', '/']):
    # Erstellen eines Buttons für jeden Operator
    # text=op: Der Button zeigt den Operator als Text an
    # command=lambda o=op: calculate(o): 
    #   - Lambda-Funktion zum Aufruf von calculate() mit dem aktuellen Operator
    #   - o=op ist notwendig, um den aktuellen Wert von op zu "binden"
    #     (andernfalls würden alle Buttons nur den letzten Operator verwenden)
    # grid(row=2, column=i): Dritte Zeile, Spalte entsprechend dem Index (0-3)
    tk.Button(root, text=op, command=lambda o=op: calculate(o)).grid(row=2, column=i)

# ===================================================================
# Hauptprogrammschleife starten
# ===================================================================

# Startet die Tkinter Event-Loop (Hauptschleife)
# Diese Schleife wartet auf Benutzerinteraktionen (Klicks, Tastatureingaben etc.)
# und hält das Fenster geöffnet, bis es vom Benutzer geschlossen wird
root.mainloop()