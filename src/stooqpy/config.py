""" Instaluje pliki konfiguracyjne w Dokumentach użytkownika."""

import os
import shutil
from platformdirs import user_documents_dir
import importlib.resources as pkg_resources
from . import templates

# Tworzy nazwę podfolderu, który zostanie utworzony w 'Dokumentach'
CONFIG_SUBDIR = "stooqpy"

# Znajduje ścieżkę do systemowego folderu 'Dokumenty'/'Documents'
try:
    docs_dir = user_documents_dir()

    # Tworzy pełną ścieżkę do folderu konfiguracyjnego użytkownika
    CONFIG_DIR = os.path.join(docs_dir, CONFIG_SUBDIR)
except Exception as ex:
    # Raportuje ewentualne fiasko poszukiwań
    print(f'Wystąpił błąd: {ex}')
    raise Exception

# Definiuje ścieżkę docelową dla pliku konfiguracyjnego
USER_CONFIG_PATH = os.path.join(CONFIG_DIR, 'settings.py')
USER_SETUP_PATH = os.path.join(CONFIG_DIR, 'setup.yaml')


def initialize_config():
    """
    Tworzy pliki konfiguracyjne na podstawie szablonów,
    jeśli jeszcze nie istnieją.
    """
    os.makedirs(CONFIG_DIR, exist_ok=True)

    if not os.path.exists(USER_CONFIG_PATH):
        print(f"Tworzenie pliku konfiguracyjnego w: {USER_CONFIG_PATH}")
        with pkg_resources.path(templates, 'settings.py') as template_path:
            shutil.copy2(template_path, USER_CONFIG_PATH)

    if not os.path.exists(USER_SETUP_PATH):
        print(f"Tworzenie pliku konfiguracyjnego w: {USER_SETUP_PATH}")
        with pkg_resources.path(templates, 'setup.yaml') as template_path:
            shutil.copy2(template_path, USER_SETUP_PATH)


if __name__ == '__main__':
    print(CONFIG_DIR)
    print(USER_CONFIG_PATH)
    print(USER_SETUP_PATH)
