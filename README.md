# Gif-your-dose-response
Genera una animación de curva dosis-respuesta con la ecuación de Hill, mostrando la reducción progresiva de EC₅₀ tras un tratamiento. Útil para visualización de sensibilidad farmacológica.


# Animación de Curva Dosis–Respuesta con EC₅₀ Decreciente

Este repositorio contiene un script en Python que genera una **animación en formato GIF** basada en la **ecuación de Hill**, mostrando cómo una curva dosis–respuesta cambia cuando **disminuye progresivamente el valor de EC₅₀**, simulando un aumento en la sensibilidad a un fármaco tras tratamiento.

---

## 🧪 ¿Qué hace este script?

- Calcula curvas dosis–respuesta con diferentes valores de EC₅₀.
- Genera un gráfico para cada curva, comparando la condición inicial con la actual.
- Añade una flecha y texto explicativo en el último frame.
- Une todos los gráficos en un GIF animado llamado `[Nombre archivo].gif`.

---

## 📈 Ejemplo visual

<img src="[Nombre archivo].gif" width="600"/>

---

## 🧰 Requisitos

Instala las dependencias necesarias con:

```bash
pip install numpy matplotlib imageio
```

---

## ▶️ Cómo ejecutarlo

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de estar en la carpeta donde está el archivo `.py`.
3. Ejecuta el script con:

```bash
python3 curva_ec50_animacion.py
```

4. El GIF generado aparecerá en la misma carpeta (`stefano_ec50.gif`).

---

## 📁 Archivos incluidos

- `curva_ec50_animacion.py`: Script principal.
- `requirements.txt`: Lista de dependencias.
- `README.md`: Este archivo.

---

## 📚 Sobre la ecuación de Hill

La ecuación de Hill es un modelo farmacodinámico usado para describir la relación entre la concentración de un fármaco y su efecto:

```
E(dose) = Emax * (dose^n) / (EC50^n + dose^n)
```

- `Emax`: respuesta máxima (100%)
- `EC₅₀`: concentración que produce el 50% de la respuesta
- `n`: coeficiente de Hill (pendiente)

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Libre para uso, modificación y distribución.
