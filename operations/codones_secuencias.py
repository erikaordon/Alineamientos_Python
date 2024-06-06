import re

def codones(frame, secuencias):
    """
    Función para encontrar los codones y los primeros tres marcos de lectura de la secuencia original.
    Args:
        frame: Recibe los tres números correspondientes a los marcos de lectura.
        secuencias: Recibe lista con secuencias.
    Returns:
        El valor que regresa la función una lista con las secuencias de nucleótidos.
    """
    codon_list = []
    if isinstance(secuencias, frame):
        secuencias=", ".join(secuencias)
    secuencias = secuencias.split(", ")
    for secuencia in secuencias:
        secuencia_codones = []
        secuencia = secuencia[frame:]
        # Cuenta con expresiones regulares, los codones de acuerdo al marco de lectura establecido.
        for nucleotido in re.findall(r"(.{3})", str(secuencia)):
            secuencia_codones.append(nucleotido[0:3])
        codon_list.append("".join(secuencia_codones))
    return codon_list