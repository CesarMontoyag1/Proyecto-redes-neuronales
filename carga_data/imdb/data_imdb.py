import os
import shutil
import kagglehub

# Descargar dataset IMDB

print("Descargando dataset IMDB...")

path = kagglehub.dataset_download(
    "rehanliaqat17/imbd-dataset"
)

print(f"\nDataset descargado en:\n{path}")

# Buscar CSV

csv_files = [
    f for f in os.listdir(path)
    if f.endswith(".csv")
]

if not csv_files:
    raise FileNotFoundError(
        "No se encontró ningún CSV."
    )

csv_original = os.path.join(
    path,
    csv_files[0]
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
    "imdb"
)

os.makedirs(target_dir, exist_ok=True)

# Ruta final

target_csv = os.path.join(
    target_dir,
    "IMDB_Dataset.csv"
)

# Copiar archivo

shutil.copy(csv_original, target_csv)

print(f"\nArchivo copiado a:\n{target_csv}")

# Verificación

if os.path.exists(target_csv):
    print("\n IMDB_Dataset.csv existe correctamente.")
else:
    print("\n Error copiando el archivo.")