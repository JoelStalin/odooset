import os

def create_package_structure(package_name):
    # Estructura de carpetas
    directories = [
        package_name,
        f"{package_name}/tests",
        f"{package_name}/docs",
    ]

    # Estructura de archivos
    files = {
        f"{package_name}/__init__.py": "",
        f"{package_name}/main.py": """def main():
    print("¡Hola, mundo!")

if __name__ == "__main__":
    main()
""",
        "setup.py": f"""from setuptools import setup, find_packages

setup(
    name='{package_name}',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={{
        'console_scripts': [
            '{package_name}={package_name}.main:main',
        ],
    }},
)
""",
        "README.md": f"# {package_name}\n\nEste es un paquete de ejemplo de Python.\n",
        "requirements.txt": "",
        ".gitignore": "__pycache__/\n*.pyc\n*.pyo\n*.pyd\n*.egg-info/\ndist/\nbuild/\n",
    }

    # Crear directorios
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Crear archivos
    for file_path, content in files.items():
        with open(file_path, 'w') as file:
            file.write(content.strip())

    print(f"Estructura del paquete de Python '{package_name}' creada correctamente.")

if __name__ == "__main__":
    # Solicitar el nombre del paquete al usuario
    package_name = input("Introduce el nombre del paquete: ")
    create_package_structure(package_name)
