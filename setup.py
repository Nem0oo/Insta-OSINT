from setuptools import setup, find_packages

setup(
    name="Insta-OSINT",
    version="1.0.0",
    packages=['osint'],
    install_requires=[
        'requests',  # Ajoute toutes les dépendances nécessaires ici
        'pathlib',   # pathlib est inclus dans Python >= 3.4, donc pas nécessaire si tu utilises cette version ou supérieure
    ],
    entry_points={
        "console_scripts": [
            "insta-osint = osint.main:main",
        ],
    },
)