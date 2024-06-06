from Bio.Seq import Seq

def complemento(secuencias):
    """
    Función para encontrar el complementario de la secuencia original de nucleotidos.
    Args:
        secuencias: Recibe lista con secuencias.
    Returns:
        El valor que regresa la función una lista con el complementario de las secuencias de nucleótidos.
    """
    complement_list=[]
    # Prepara las secuenciancias para procesarlas 
    if isinstance(secuencias, list):
        secuencias=", ".join(secuencias)
    secuencias = secuencias.split(", ")
    for secuencia in secuencias:
        seq_obj=Seq(secuencia)
        # Obtiene la secuencia complementaria a la secuencia que se está analizando. 
        complement_seq=str(seq_obj.complement())
        complement_seq=("".join(complement_seq))
        complement_list.append(complement_seq)
    return complement_list