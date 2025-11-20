import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")



habitos = ["Sueño", "Estudio", "Deporte", "Videojuegos"]
horas = [49, 15, 5, 20]  
colores_habitos = ["skyblue", "lightgreen", "salmon", "orange"]

plt.figure(figsize=(8,5))
plt.bar(habitos, horas, color=colores_habitos)
plt.title("Mis hábitos semanales")
plt.ylabel("Horas por semana")
plt.show()


edades = [19, 22, 23, 25, 20]  
alturas = [1.80, 1.60, 1.95, 1.75, 1.58]  
colores_dispersion = ["red", "blue", "green", "purple", "orange"]

plt.figure(figsize=(8,5))
plt.scatter(edades, alturas, color=colores_dispersion, s=100)  
plt.title("Altura vs Edad de la clase")
plt.xlabel("Edad")
plt.ylabel("Altura (cm)")
plt.show()


redes = ["Instagram", "TikTok", "Twitter", "YouTube"]
usuarios = [15, 18, 5, 12]  
colores_redes = ["pink", "lightblue", "lightgrey", "yellow"]

plt.figure(figsize=(8,5))
plt.bar(redes, usuarios, color=colores_redes)
plt.title("Usuarios de redes sociales en clase")
plt.ylabel("Número de alumnos")
plt.show()
