# 📝 ejercicio2.py
# 🎓 Promedio de notas
# Puntaje: 12 puntos

# Instrucciones:
# 1. Solicita cuántas notas ingresará el usuario.
# 2. Usa un ciclo para pedir las notas una por una y guárdalas en una lista.
# 3. Calcula el promedio con dos decimales.
# 4. Muestra si el promedio es suficiente para aprobar (4.0 o más) o no.
# 5. Todas las notas deben estar entre 1.0 y 7.0.

# 👇 Aquí comienza tu código
n = int(input("ingresa tus notas "))
notas = []

for i in range(n):
    nota = float(input("Ingrese nota: "))
    notas.append(nota)

promedio = sum(notas) / n
print("Promedio:", round(promedio, 2))

if promedio >= 4.0:
    print("¡Aprobaste!")
else:
    print("No aprobaste.jijiji")
