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
├── tests/
│   ├── test_fetch_data.py
│   ├── test_initialize_db.py
│   ├── test_extract_metrics.py
│   ├── test_save_metrics.py
│   ├── test_copy_metrics.py
├── data/
│   └── vulnerabilities.csv
├── requirements.txt
├── validate.sh
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
sh python3 -m venv venv source venv/bin/activate 

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

### Instructions for Uploading to GitHub

1. Initialize a new Git repository:
    ```sh
    git init
    ```

2. Add all files to the repository:
    ```sh
    git add .
    ```

3. Commit the changes:
    ```sh
    git commit -m "Initial commit"
    ```

4. Add the remote repository (replace `<username>` and `<repository>` with your GitHub username and repository name):
    ```sh
    git remote add origin https://github.com/<username>/fortify-light.git
    ```

5. Push the changes to GitHub:
    ```sh
    git push -u origin master
    ```

This completes the creation of a comprehensive Git project structure for "fortify-light". You can now manage the project using Git and share it on GitHub.

