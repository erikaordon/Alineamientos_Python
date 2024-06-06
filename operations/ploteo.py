import matplotlib.pyplot as plt
import numpy as np

def ploteo_comparacion(seq1,seq2,frame):
  """
  Función para plotear en un heapmap las secuencias obtenidas.
      Args:
          seq1: Recibe lista con secuencias.
          seq2: Recibe lista con secuencias.
          frame: Recibe el marco de lectura con el que se va a trabajar.
      Returns:
          El valor que regresa la función es un heapmap que grafica las secuencias de nucleótidos, una en el eje de las x y otro en el de las y.
  """

  matriz = np.zeros((len(seq1),len(seq2)))

# Busca la diagonal de la matriz para encontrar las coincidencias entre nucleótidos. 
  for n in range(len(seq1)):
    if seq1[n] == seq2[n]:
      matriz[n][n] = 1

  plt.imshow(matriz)
  plt.xticks([])
  plt.yticks([])
  plt.xlabel("secuencia_1")
  plt.ylabel("secuencia_2")
  plt.title(f'Marco de lectura {frame}')
  plt.show()