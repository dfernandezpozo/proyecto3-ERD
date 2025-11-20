import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Datos del primer gráfico
datos = {"animales": ["alimoche moteado", "ocelote", "gorila", "wombat", "Alfonso"],
         "cantEjemplares": [30, 2000, 40, 90, 1]}

df = pd.DataFrame(datos)


plt.figure(figsize=(8,5))
bars = plt.bar(df['animales'], df['cantEjemplares'], color=['#FF9999','#66B2FF','#99FF99','#FFCC99','#C2C2F0'])
plt.title("Animales y cantidad de ejemplares", fontsize=16, fontweight='bold')
plt.xlabel("Animales", fontsize=12)
plt.ylabel("C.Ejemplares", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

# Datos del segundo gráfico
dias = ["D1","D2","D3","D4","D5","D6","D7","D8","D9","D10"]
precio = [22, 13, 15, 77, 2, 8, 15, 99, 21, 14]


plt.figure(figsize=(10,5))
plt.plot(dias, precio, marker='o', linestyle='-', color='green', linewidth=2, markersize=8, label="precios")
plt.title("Evolución de precios en 10 días", fontsize=16, fontweight='bold')
plt.xlabel("Días", fontsize=12)
plt.ylabel("Precios", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=12)

for i, p in enumerate(precio):
    plt.text(i, p + 2, str(p), ha='center', fontsize=10)

plt.show()

# Tercer gráfico

datos = {
    "Categoría": ["Hores de son", "Clases", "Oci", "Esport"],
    "Porcentaje": [20, 5, 50, 25]
}

df = pd.DataFrame(datos)

plt.pie(df["Porcentaje"], labels=df["Categoría"], autopct="%1.1f%%", startangle=90)
plt.title("Distribuciò horari setmanal")
plt.show()

# Cuarto gráfico


data = np.random.uniform(0, 20, 100)
plt.figure(figsize=(10, 5))
counts, bins, patches = plt.hist(data, bins=15, edgecolor='black')


colors = plt.cm.rainbow(np.linspace(0, 1, len(patches)))
for patch, color in zip(patches, colors):
    patch.set_facecolor(color)


plt.title("Histograma de 100 nombres aleatoris entre 0 i 20", fontsize=16, fontweight='bold')
plt.xlabel("Valor", fontsize=12)
plt.ylabel("Freqüència", fontsize=12)
plt.legend(["Distribució de valors"], fontsize=12)
plt.grid(True, linestyle='--', alpha=0.4)
plt.show()