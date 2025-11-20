import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

minutos = [30, 45, 20, 25, 40, 50, 35, 30, 25, 45, 40, 20, 30, 35, 50, 40, 25, 30, 45, 50,
           35, 30, 25, 40, 45, 50, 30, 35, 40, 25]

dias = np.arange(1, 31)

plt.figure(figsize=(12,5))

plt.subplot(1, 2, 1)
sns.histplot(minutos, bins=8, kde=True, color='skyblue')
plt.title('Distribución de minutos de ejercicio', fontsize=14)
plt.xlabel('Minutos')
plt.ylabel('Frecuencia')

plt.subplot(1, 2, 2)
plt.plot(dias, minutos, marker='o', color='tomato')
plt.title('Evolución de minutos de ejercicio durante 30 días', fontsize=14)
plt.xlabel('Días')
plt.ylabel('Minutos')
plt.grid(alpha=0.3)
plt.tight_layout()

plt.show()

# Proyecto 2

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
ingresos = np.array([2500, 2600, 2550, 2700, 2650, 2750, 2800, 2900, 2850, 2750, 2650, 2700])
gastos = np.array([2000, 2100, 2050, 2200, 2150, 2250, 2300, 2400, 2350, 2250, 2150, 2200])
ahorro = np.cumsum(ingresos - gastos)

x = np.arange(len(meses))

plt.figure(figsize=(12,5))


plt.subplot(1, 2, 1)
plt.bar(x, ingresos, color='dodgerblue', label='Ingresos')
plt.bar(x, gastos, color='tomato', label='Gastos')
plt.xticks(x, meses)
plt.ylabel('Euros (€)')
plt.title('Ingresos y gastos mensuales')
plt.legend()
plt.grid(axis='y', alpha=0.3)


plt.subplot(1, 2, 2)
plt.plot(meses, ahorro, marker='o', color='mediumseagreen', linewidth=2)
plt.title('Ahorro acumulado mensual')
plt.xlabel('Meses')
plt.ylabel('Euros (€)')
plt.grid(alpha=0.3)
plt.tight_layout()

plt.show()

# Proyecto 3

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
temp_min = [2, 3, 5, 8, 12, 15, 17, 16, 13, 9, 5, 3]
temp_max = [8, 10, 13, 17, 21, 25, 28, 27, 23, 18, 12, 9]
temp_media = [(min_t + max_t)/2 for min_t, max_t in zip(temp_min, temp_max)]

x = np.arange(len(meses))

plt.figure(figsize=(12,5))


plt.subplot(1, 2, 1)
plt.plot(meses, temp_max, marker='o', color='tomato', label='Máximas')
plt.plot(meses, temp_min, marker='o', color='skyblue', label='Mínimas')
plt.title('Temperaturas mínimas y máximas')
plt.xlabel('Meses')
plt.ylabel('°C')
plt.legend()
plt.grid(alpha=0.3)


plt.subplot(1, 2, 2)
plt.bar(meses, temp_media, color='mediumseagreen')
plt.title('Temperatura media mensual')
plt.xlabel('Meses')
plt.ylabel('°C')
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
