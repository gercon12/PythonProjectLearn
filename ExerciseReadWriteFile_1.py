#poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program
#and find out words with maximum occurance.

with open("C:\\Users\\DELL LATITUDE\\PycharmProjects\\PythonProjectLearn\\poem.txt", "r") as f:
    content = f.read()
print(content)

print(type(content))

import re
from collections import Counter

# Quitar puntuación y dejar solo letras y espacios
texto_limpio = re.sub(r'[^\w\s]', '', content.lower())

palabras = texto_limpio.split()
contador = Counter(palabras)

print(contador.most_common(10))

import matplotlib.pyplot as plt

mas_comunes = contador.most_common(10)  # top 10
palabras, frecuencias = zip(*mas_comunes)

plt.bar(palabras, frecuencias)
plt.xticks(rotation=45)
plt.title("Palabras más frecuentes")
plt.show()

