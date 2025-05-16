import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

# ----------------------------
# Función: ecuación de Hill
# ----------------------------
def hill_equation(dose, Emax, EC50, n):
    return Emax * (dose**n) / (EC50**n + dose**n)

# ----------------------------
# Parámetros
# ----------------------------
Emax = 100
EC50_pre = 3.0
EC50_after = 0.3
hill_slope = 1.2
steps = 40
doses = np.logspace(-2, 3, 300)
EC50s = np.linspace(EC50_pre, EC50_after, steps)

# Colores para las curvas
color_before = "#B0C4DE"
color_after = "#1f77b4"

# Carpeta de salida
output_dir = "curva_dosis_respuesta"
os.makedirs(output_dir, exist_ok=True)
filenames = []

# ----------------------------
# Generar los frames
# ----------------------------
for i, EC50 in enumerate(EC50s):
    response_before = hill_equation(doses, Emax, EC50_pre, hill_slope)
    response_current = hill_equation(doses, Emax, EC50, hill_slope)

    # Flecha y texto
    y_arrow = 27
    x_start = EC50_pre
    x_end = EC50
    x_text = np.sqrt(EC50_pre * EC50)

    fig, ax = plt.subplots(figsize=(7, 5))

    # Curvas
    ax.plot(doses, response_before, '-', color=color_before,
            label=f'Antes (EC₅₀ = {EC50_pre:.1f} µM)', lw=1.8, alpha=0.7, zorder=1)
    ax.plot(doses, response_current, '-', color=color_after,
            label=f'Después (EC₅₀ ≈ {EC50:.2f} µM)', lw=2.5, zorder=2)

    if i == len(EC50s) - 1:
        # Flecha fluida usando annotate
        ax.annotate(
            '', xy=(x_end, y_arrow), xytext=(x_start, y_arrow),
            arrowprops=dict(arrowstyle='-|>', color='black', lw=1.2), zorder=3
        )

        # Texto en dos líneas sobre la flecha
        ax.text(x_text, y_arrow + 7, '↓ EC₅₀\n↑ Sensibilidad',
                ha='center', va='bottom', fontsize=11, family='sans-serif', color='black')

    # Ajustes de ejes y estilo
    ax.set_xscale('log')
    ax.set_xlim(0.005, 1000)
    ax.set_ylim(0, 110)
    ax.set_xlabel("Concentración del fármaco (µM)", fontsize=12, family='sans-serif')
    ax.set_ylabel("Viabilidad (%)", fontsize=12, family='sans-serif')
    ax.set_title("Reducción de EC₅₀ tras tratamiento experimental", fontsize=13, family='sans-serif')
    ax.legend(loc='lower right', fontsize=10)
    ax.grid(True, which='major', linestyle='-', linewidth=0.4, alpha=0.3)
    ax.grid(True, which='minor', linestyle=':', linewidth=0.3, alpha=0.2)
    ax.minorticks_on()
    ax.tick_params(which='both', direction='out', length=4, width=1)
    plt.tight_layout()

    # Guardar frame
    frame_path = os.path.join(output_dir, f"frame_{i}.png")
    plt.savefig(frame_path, dpi=200)
    plt.close()
    filenames.append(frame_path)

# ----------------------------
# Crear el GIF
# ----------------------------
gif_path = "[Nombre_Archivo].gif"
with imageio.get_writer(gif_path, mode='I', duration=0.4) as writer:
    for filename in filenames:
        writer.append_data(imageio.imread(filename))

print(f"\n✅ GIF generado: {gif_path}")
