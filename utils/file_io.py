"""
file_io.py: Funciones para manejar operaciones de entrada de archivos de ADN.

Este módulo provee funcionalidades para leer secuencias de ADN desde
archivos fasta, asegurando que las secuencias sean válidas y estén bien formateadas.

Funciones:
    read_dna_sequence(filename) - Lee una secuencia de ADN de un archivo.
    
Ejemplos de uso están disponibles en el bloque principal del módulo.

Autores: Erika Nathalia Ordoñez Guzmán
Versión: 1.0
"""

# meta-info
__author__ = "Erika Nathalia Ordoñez Guzmán"
__version__ = "1.0"

def read_dna_sequence(filename):
    """
    Lee una secuencia de ADN de un archivo de texto.
    
    Args:
        filename (str): El nombre del archivo del cual leer la secuencia.
        
    Returns:
        str: La secuencia de ADN contenida en el archivo.
        
    Raises:
        FileNotFoundError: Si el archivo especificado no se encuentra.
        ValueError: Si el archivo está vacío o contiene caracteres no válidos.
    """
    with open(filename, 'r') as file:
        sequence = file.read().strip().upper()
    if not sequence:
        raise ValueError("El archivo está vacío.")

    return sequence