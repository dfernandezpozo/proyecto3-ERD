import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


alumnos = ["Laura", "Marc", "Sergio", "Clara", "Júlia", "Pau", "Marta", "Pepe"]


notas_asignatura1 = np.random.randint(0, 11, 8)
notas_asignatura2 = np.random.randint(0, 11, 8)


df = pd.DataFrame({
    "Alumno": alumnos,
    "Asignatura 1": notas_asignatura1,
    "Asignatura 2": notas_asignatura2
})


plt.figure(figsize=(10, 6))

plt.bar(df["Alumno"], df["Asignatura 1"], label="Asignatura 1")
plt.bar(df["Alumno"], df["Asignatura 2"],
        bottom=df["Asignatura 1"], label="Asignatura 2")

plt.title("Notas de 2 asignaturas de 8 alumnos", fontsize=16, fontweight='bold')
plt.xlabel("Alumnos", fontsize=12)
plt.ylabel("Nota", fontsize=12)
plt.legend()
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Segundo gráfico

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
temp_min = [12, 14, 13, 11, 15, 13, 12]
temp_max = [22, 24, 23, 21, 25, 24, 23]

plt.figure(figsize=(10,5))
plt.plot(dias, temp_max, marker='o', color='tomato', label='Máximas')
plt.plot(dias, temp_min, marker='o', color='skyblue', label='Mínimas')
plt.title('Temperaturas mínimas y máximas de la semana', fontsize=14)
plt.xlabel('Días', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Tercer gráfico

alturas = [150, 160, 165, 170, 155, 180, 175, 162, 168, 158]
pesos = [50, 60, 65, 70, 55, 80, 75, 62, 68, 58]

plt.figure(figsize=(8,6))
plt.scatter(alturas, pesos, color='mediumseagreen', s=100, alpha=0.7)

plt.title('Relación entre altura y peso de los alumnos', fontsize=14)
plt.xlabel('Altura (cm)', fontsize=12)
plt.ylabel('Peso (kg)', fontsize=12)
plt.grid(alpha=0.3)

plt.show()

# Cuarto gráfico

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
ingresos = [2500, 2600, 2550, 2700, 2650, 2750, 2800, 2900, 2850, 2750, 2650, 2700]
gastos = [2000, 2100, 2050, 2200, 2150, 2250, 2300, 2400, 2350, 2250, 2150, 2200]

x = np.arange(len(meses))
ancho = 0.35

plt.figure(figsize=(12,6))
plt.bar(x - ancho/2, ingresos, width=ancho, color='dodgerblue', label='Ingresos')
plt.bar(x + ancho/2, gastos, width=ancho, color='tomato', label='Gastos')

plt.xticks(x, meses)
plt.title('Ingresos y gastos mensuales de una familia', fontsize=14)
plt.xlabel('Meses', fontsize=12)
plt.ylabel('Euros (€)', fontsize=12)
plt.legend()
plt.grid(axis='y', alpha=0.3)

plt.show()



