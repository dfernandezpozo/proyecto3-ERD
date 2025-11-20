import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('notas.csv')
df['Media'] = df[['Matemáticas', 'Catalán', 'Inglés']].mean(axis=1)

plt.figure(figsize=(10,6))
plt.bar(df['Nombre'], df['Media'], color='mediumslateblue', alpha=0.7)
plt.title('Nota media de cada alumno', fontsize=14)
plt.xlabel('Alumno', fontsize=12)
plt.ylabel('Nota media', fontsize=12)
plt.ylim(0, 10)  
plt.grid(axis='y', alpha=0.3)

plt.show()

# Segundo Gráfico

respuestas = ["M'agrada Python", "Prefereixo JavaScript", "M'és indiferent"]
valores = [45, 30, 25]  
colors = ['#ff9999','#66b3ff','#99ff99'] 

plt.figure(figsize=(8,8))
plt.pie(valores, labels=respuestas, autopct='%1.1f%%', startangle=90, colors=colors, shadow=False)
plt.title('Resultados de la encuesta de preferencia de lenguaje', fontsize=14)
plt.tight_layout()

plt.show()

# Tercer gráfico

semanas = ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4', 'Semana 5']
producto_A = [150, 200, 180, 220, 210]
producto_B = [100, 120, 130, 140, 150]
producto_C = [80, 90, 100, 95, 110]

plt.figure(figsize=(10,6))
plt.plot(semanas, producto_A, marker='o', color='dodgerblue', label='Producto A')
plt.plot(semanas, producto_B, marker='s', color='tomato', label='Producto B')
plt.plot(semanas, producto_C, marker='^', color='mediumseagreen', label='Producto C')
plt.title('Ventas semanales de tres productos', fontsize=14)
plt.xlabel('Semanas', fontsize=12)
plt.ylabel('Unidades vendidas', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)

plt.show()

# Cuarto gráfico

notas = {
    'Matemáticas': [8, 6, 9, 7, 10, 5, 8, 6, 7, 9],
    'Catalán': [7, 5, 8, 6, 9, 6, 8, 7, 6, 8],
    'Inglés': [9, 7, 10, 8, 9, 5, 7, 6, 8, 9]
}

plt.figure(figsize=(8,6))
sns.boxplot(data=notas)
plt.title('Distribución de notas de los alumnos', fontsize=14)
plt.ylabel('Notas')

plt.show()

