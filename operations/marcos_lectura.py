from Bio.Seq import Seq
from operations.codones_secuencias import codones
from operations.ploteo import ploteo_comparacion
from operations.secuencias_complemento import complemento

def coincidencias(secuencias_nucleotidos_1, secuencias_nucleotidos_2):
  """
  Función para mandar las secuencias de nucleótidos a la función ára graficar.
    Args:
        secuencias_nucleotidos_1: Recibe lista con secuencias.
        secuencias_nucleotidos_2: Recibe lista con secuencias.
    Returns:
        El valor que regresa la función son las secuencias traducidas a aminoácidos de todos los marcos de lectura.
        """
  if len(secuencias_nucleotidos_1) == len(secuencias_nucleotidos_2):
    # Calcula los codones de los 3 marcos de lectura de las secuencias originales llamando a su función.
    for frame in range(3):
      frame_seq = codones(frame,[secuencias_nucleotidos_1,secuencias_nucleotidos_2])
      seq1 = Seq(frame_seq[0])
      seq2 = Seq(frame_seq[1])
      ploteo_comparacion(seq1.translate(),seq2.translate(),frame)
      # Calcula los codones de los 3 marcos de lectura de las secuencias complementarias llamando a su función.
    for frame in range(3):
      frame_seq = complemento([secuencias_nucleotidos_1,secuencias_nucleotidos_2])
      seq1 = Seq(frame_seq[0])
      seq2 = Seq(frame_seq[1])
      ploteo_comparacion(seq1.translate(),seq2.translate(),frame)