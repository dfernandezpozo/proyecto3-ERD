import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("pokemon.csv")  

stats = ['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']
df['Total'] = df[stats].sum(axis=1)
sns.set_style("whitegrid")

# Gráfico 1
plt.figure(figsize=(8,6))
gen_counts = df['generation'].value_counts().sort_index()
sns.barplot(x=gen_counts.index, y=gen_counts.values, palette="viridis")
plt.title("Número de Pokémon por Generación")
plt.xlabel("Generación")
plt.ylabel("Cantidad de Pokémon")
plt.tight_layout()
plt.savefig("pokemons_por_generacion.png")
plt.show()

# Gráfico 2
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='Total', y='speed', hue='is_legendary', 
                palette={0: "blue", 1: "red"})
plt.title("Relación entre Total de estadísticas y Velocidad")
plt.xlabel("Estadísticas totales (Total)")
plt.ylabel("Velocidad (Speed)")
plt.legend(title="Legendario", labels=['No', 'Sí'])
plt.tight_layout()
plt.savefig("total_vs_speed_legendary.png")
plt.show()

# Gráfico 3
legend_counts = df['is_legendary'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(legend_counts, labels=['No Legendario', 'Legendario'], 
        autopct="%1.1f%%", colors=["skyblue", "salmon"])
plt.title("Proporción de Pokémon Legendarios vs No Legendarios")
plt.tight_layout()
plt.savefig("proporcion_legendary.png")
plt.show()

# Esto lo he buscado para que se muestre bien por pantalla para hacer el informe.
num_pokemons = len(df)
num_legend = legend_counts.get(1, 0)
perc_legend = num_legend / num_pokemons * 100

print("=== Informe Pokémon ===")
print(f"Número total de Pokémon: {num_pokemons}")
print(f"Número de legendarios: {num_legend} ({perc_legend:.2f} %)")
print()
print("Conteo por generación:")
print(gen_counts)
print()
print("Estadísticas totales (Total):")
print(df['Total'].describe())
print()
print("Conclusiones preliminares:")
print("- La mayoría de Pokémon no son legendarios; los legendarios representan solo una pequeña parte.")
print("- Existe variabilidad en las estadísticas totales entre generaciones, algunas generaciones tienen Pokémon con stats muy altos.")
print("- Los legendarios suelen tener estadísticas totales más altas y velocidad relativamente alta, aunque no todos los Pokémon fuertes son rápidos.")
