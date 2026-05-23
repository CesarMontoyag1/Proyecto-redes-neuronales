import os
import shutil
import kagglehub

# Descargar dataset Amazon

print("Descargando dataset Amazon...")

path = kagglehub.dataset_download(
    "snap/amazon-fine-food-reviews"
)

print(f"\nDataset descargado en:\n{path}")

# Archivo CSV original

csv_original = os.path.join(
    path,
    "Reviews.csv"
)

# Obtener raíz del proyecto

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

# Carpeta destino

target_dir = os.path.join(
    project_root,
    "data",
    "amazon"
)

os.makedirs(target_dir, exist_ok=True)

# Ruta final

target_csv = os.path.join(
    target_dir,
    "Reviews.csv"
)

# Copiar archivo

shutil.copy(csv_original, target_csv)

print(f"\nArchivo copiado a:\n{target_csv}")

# Verificación

if os.path.exists(target_csv):
    print("\n Reviews.csv existe correctamente.")
else:
    print("\n Error copiando el archivo.")