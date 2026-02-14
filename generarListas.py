import random

MATERIALES = ("PET 🛢️", "CARTON 📦", "VIDRIO 🫙", "METAL 🪩")


def generar_mediciones_por_material(cantidad_por_material=20, minimo=0, maximo=20):
    return {
        material: [random.randint(minimo, maximo) for _ in range(cantidad_por_material)]
        for material in MATERIALES
    }


def calcular_promedios(mediciones):
    promedios_por_material = {
        material: sum(valores) / len(valores) for material, valores in mediciones.items() if valores
    }
    todos_los_valores = [valor for valores in mediciones.values() for valor in valores]
    promedio_global = sum(todos_los_valores) / len(todos_los_valores) if todos_los_valores else 0

    return promedios_por_material, promedio_global


def clasificar_promedio_material(promedio):
    if promedio < 8:
        return "Bajo ↘️ (hay que mejorar cultura/flujo)"
    if promedio <= 15:
        return "Estable ↔️ (estamos en el camino correcto)"
    return "Alto 😎 (excelente, estamos reciclando hasta la paciencia)"


def clasificar_promedio_global(promedio_global):
    if promedio_global < 10:
        return "Alerta ⚠️"
    if promedio_global < 15:
        return "Operación normal ✅"
    return "Jornada sobresaliente 🎉"


def mostrar_reporte_promedio(cantidad_por_material=20, minimo=0, maximo=20):
    mediciones = generar_mediciones_por_material(cantidad_por_material, minimo, maximo)
    promedios_por_material, promedio_global = calcular_promedios(mediciones)

    print(f"Mediciones generadas ▶️: {mediciones}")
    print("\nPromedio y estado por material 📊:")

    for material, promedio in promedios_por_material.items():
        clasificacion = clasificar_promedio_material(promedio)
        print(f"- {material}: {promedio:.2f} kg -> {clasificacion}")

    estado_global = clasificar_promedio_global(promedio_global)
    print(f"\nPromedio global 🌱: {promedio_global:.2f} kg -> {estado_global}")


if __name__ == "__main__":
    mostrar_reporte_promedio()
