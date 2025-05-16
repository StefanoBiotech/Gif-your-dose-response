import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

# ----------------------------
# Función de Hill
# ----------------------------
def hill_equation(dose, Emax, EC50, n):
    return Emax * (dose ** n) / (EC50 ** n + dose ** n)

# ----------------------------
# Parámetros base
# ----------------------------
Emax = 100
EC50_start = 0.3  # menor EC50 (más sensible)
EC50_end = 3.0    # mayor EC50 (menos sensible)
hill_slope = 1.2
steps = 40
EC50s = np.linspace(EC50_start, EC50_end, steps)
doses = np.logspace(-3, 1, 300)

# Ticks personalizados para el eje X
custom_ticks = [0.001, 0.01, 0.1, 1, 10]
custom_labels = ['0.001', '0.01', '0.1', '1', '10']

# Colores
color_before = "#B0C4DE"
color_after = "#1f77b4"

# ----------------------------
# Crear carpeta y generar frames
# ----------------------------
output_dir = "curva_dosis_respuesta_derecha"
os.makedirs(output_dir, exist_ok=True)
filenames = []

for i, EC50 in enumerate(EC50s):
    response_before = hill_equation(doses, Emax, EC50s[0], hill_slope)
    response_current = hill_equation(doses, Emax, EC50, hill_slope)

    fig, ax = plt.subplots(figsize=(7, 5))

    # Curvas
    ax.plot(doses, response_before, '-', color=color_before,
            label=f'Antes (EC₅₀ = {EC50s[0]:.1f} µM)', lw=1.8, alpha=0.7, zorder=1)
    ax.plot(doses, response_current, '-', color=color_after,
            label=f'Después (EC₅₀ ≈ {EC50:.2f} µM)', lw=2.5, zorder=2)

    # Flecha + texto solo al final
    if i == len(EC50s) - 1:
        y_arrow = 27
        x_start = EC50s[0]
        x_end = EC50s[-1]
        x_text = np.sqrt(x_start * x_end)

        ax.annotate('', xy=(x_end, y_arrow), xytext=(x_start, y_arrow),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.2), zorder=3)

        ax.text(x_text, y_arrow + 7, '↑ EC₅₀\n↓ Sensibilidad',
                ha='center', va='bottom', fontsize=11, family='sans-serif', color='black')

    # Estética y ejes
    ax.set_xscale('log')
    ax.set_xlim(0.0008, 12)
    ax.set_ylim(0, 110)
    ax.set_xticks(custom_ticks)
    ax.set_xticklabels(custom_labels)
    ax.set_xlabel("Concentración del fármaco (µM)", fontsize=12)
    ax.set_ylabel("Viabilidad (%)", fontsize=12)
    ax.set_title("Aumento de EC₅₀ tras tratamiento experimental", fontsize=13)
    ax.legend(loc='lower right', fontsize=10)
    ax.grid(True, which='major', linestyle='-', linewidth=0.4, alpha=0.3)
    ax.grid(True, which='minor', linestyle=':', linewidth=0.3, alpha=0.2)
    ax.minorticks_on()
    ax.tick_params(which='both', direction='out', length=4, width=1)
    plt.tight_layout()

    frame_path = os.path.join(output_dir, f"frame_{i}.png")
    plt.savefig(frame_path, dpi=200)
    plt.close()
    filenames.append(frame_path)

# ----------------------------
# Crear el GIF
# ----------------------------
gif_path = "Nombre_Archivo.gif"
with imageio.get_writer(gif_path, mode='I', duration=0.4) as writer:
    for filename in filenames:
        writer.append_data(imageio.imread(filename))

print(f"\n✅ GIF generado: {gif_path}")
