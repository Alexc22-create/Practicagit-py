import os
import subprocess
import time
import webbrowser
import requests
import winreg

git_dir = '/home/alex/Documentos/Utez/4to/prog-red/practica'

if not os.path.exists(git_dir):
    os.makedirs(git_dir)
    print(f"Directorio {git_dir} creado.")

repos= [name for name in os.listdir('git_dir') if os.path.isdir(os.path.join(git_dir,name)) and os.path.exists(os.path.join(git_dir, name, '.git'))]

if repos:
    print("Repositorios Git encontrados:")
    for idx, repo in enumerate(repos):
        print(f"{idx + 1}. {repo}")
else:
    print("No se encontraron repositorios Git en el directorio especificado.")