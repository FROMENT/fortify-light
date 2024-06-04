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
- Environment variables: `SSC_URL`, `SSC_AUTH_TOKEN`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/fortify-light.git
    cd fortify-light
    ```

2. Create a virtual environment and activate it:
sh
python3 -m venv venv 
source venv/bin/activate 

3.	Install the dependencies:
pip install -r requirements.txt

Usage

	1.	Set up the environment variables:

    export SSC_URL="https://your-ssc-url"
    export SSC_AUTH_TOKEN="your-auth-token"

	2.	Run the main script:

    python scripts/main.py

 ## Functionality

- `fetch_data.py`: Contains functions to fetch projects, versions, and issues from Fortify SSC.
- `initialize_db.py`: Initializes the SQLite database.
- `extract_metrics.py`: Extracts metrics from a CSV file.
- `save_metrics.py`: Saves extracted metrics to the database.
- `copy_metrics.py`: Copies metrics from the previous week if no changes are found.
- `main.py`: Main script to orchestrate the process.

## Tests

The `tests` directory contains unit tests for the various scripts. To run the tests, use:
    ```sh python -m unittest discover -s tests



Note windows et test unitaire :
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
