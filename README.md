# Fortify Light

## Description

Fortify Light is a lightweight project to fetch and store Fortify Software Security Center (SSC) data incrementally. It includes scripts to initialize a SQLite database, fetch data from SSC, extract metrics, and save them in a database.

## Project Structure
fortify-light/

├── scripts/ 
│   ├── fetch_data.py 
│   ├── initialize_db.py 
│   ├── main.py 
│   ├── extract_metrics.py 
│   ├── save_metrics.py
│   ├── copy_metrics.py
│   ├── config.py
│   ├── generate_token.py
│   ├── encrypt.py
│   ├── process_csv.py
├── tests/
│   ├── test_fetch_data.py
│   ├── test_initialize_db.py
│   ├── test_extract_metrics.py
│   ├── test_save_metrics.py
│   ├── test_copy_metrics.py
│   ├── test_process_csv.py
├── data/
│   └── vulnerabilities.csv
├── .env
├── requirements.txt
├── validate.sh
├── validate.py
└── README.md

## Requirements

- Python 3.x
- Fortify SSC
- Environment variables: `SSC_URL`, `SSC_AUTH_TOKEN`, `SSC_ENC_USERNAME`, `SSC_ENC_PASSWORD`

## Installation

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/yourusername/fortify-light.git
    cd fortify-light
    ```

2. Créez un environnement virtuel et activez-le :
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```

3. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Exécutez le script de configuration pour définir les variables d'environnement et générer un token :
    ```sh
    python scripts/config.py
    ```

2. Sauvegardez la clé de chiffrement pour une utilisation ultérieure :
    ```sh
    python scripts/encrypt.py
    ```

## Usage

1. Définissez les variables d'environnement :
    ```sh
    export SSC_URL="https://your-ssc-url"
    export SSC_AUTH_TOKEN="your-encrypted-auth-token"
    export SSC_ENC_USERNAME="your-encrypted-username"
    export SSC_ENC_PASSWORD="your-encrypted-password"
    ```

2. Exécutez le script principal :
    ```sh
    python scripts/main.py
    ```

## Testing

1. Ouvrez Git Bash dans Visual Studio Code.
2. Exécutez le script de validation :
    ```sh
    ./validate.sh
    ```

## Fonctionnalités

- `fetch_data.py` : Contient des fonctions pour récupérer les projets, versions et issues de Fortify SSC.
- `initialize_db.py` : Initialise la base de données SQLite.
- `extract_metrics.py` : Extrait les métriques à partir d'un fichier CSV.
- `save_metrics.py` : Enregistre les métriques extraites dans la base de données.
- `copy_metrics.py` : Copie les métriques de la semaine précédente si aucun changement n'est trouvé.
- `main.py` : Script principal pour orchestrer le processus.
- `config.py` : Script pour configurer les variables d'environnement.
- `generate_token.py` : Script pour générer un token d'authentification.
- `encrypt.py` : Script pour chiffrer et déchiffrer les données.
- `process_csv.py` : Script pour traiter les issues et générer des fichiers CSV.

## License

Ce projet est sous licence MIT.

## Note windows et test unitaire :
Pour utiliser validate.sh sous Windows avec Visual Studio Code, il y a quelques étapes supplémentaires à suivre pour s’assurer que les scripts bash peuvent être exécutés correctement. Voici les étapes détaillées :

	1.	Installer Git Bash : Git Bash permet d’exécuter des scripts bash sous Windows.
	•	Téléchargez et installez Git pour Windows.
	•	Pendant l’installation, choisissez d’utiliser Git Bash.
	2.	Configurer Visual Studio Code :
	•	Ouvrez Visual Studio Code.
	•	Installez l’extension “Bash Debug” pour l’exécution et le débogage des scripts bash.
	•	Configurez Git Bash comme terminal par défaut :
	•	Ouvrez les paramètres de VS Code (Ctrl + ,).
	•	Recherchez terminal integrated shell.
	•	Dans Terminal > Integrated > Shell: Windows, choisissez le chemin de Git Bash (souvent C:\Program Files\Git\bin\bash.exe).
	3.	Exécuter validate.sh dans Git Bash :
	•	Ouvrez votre projet dans Visual Studio Code.
	•	Ouvrez un terminal intégré (Ctrl + ).
	•	Assurez-vous que le terminal intégré est configuré pour utiliser Git Bash.
	•	Exécutez le script de validation :
