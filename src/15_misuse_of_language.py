def VerarbeitungDatenZuBerechnen(datos):
    # Datenverarbeitung beginnt...
    numeroDeElementos = len(datos)
    ergebnis = 0
    for indice, valeur in enumerate(datos):
        # 加算する各要素
        ergebnis += valeur * indice
    # Результат обработки
    risultatoFinale = ergebnis / numeroDeElementos if numeroDeElementos > 0 else None
    return risultatoFinale
