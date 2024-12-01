from cx_Freeze import setup, Executable

# Options pour cx_Freeze
build_exe_options = {
    "packages": ["pygame", "os","shutil","sys"],  # Liste des packages nécessaires
    "include_files": [
        "resources/circuit.png",  # Inclure vos fichiers de ressources
        "resources/closed.png",
    ],
}

# Définir l'exécutable
exe = Executable(
    script="main.py",  # Remplacez par le nom de votre script
    base="Win32GUI",  # Utiliser Win32GUI pour une application GUI (si nécessaire)
)

# Configuration de cx_Freeze
setup(
    name="MonApplication",
    version="1.0",
    description="Description de votre application",
    options={"build_exe": build_exe_options},
    executables=[exe],
)
