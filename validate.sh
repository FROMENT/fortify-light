#!/bin/bash

echo "Validating project..."

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Please install Python3."
    exit
fi

# Check if pip is installed
if ! command -v pip &> /dev/null
then
    echo "pip could not be found. Please install pip."
    exit
fi

# Check if virtual environment is set up
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Setting up..."
    python3 -m venv venv
fi

source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Initialize database
python3 scripts/initialize_db.py

# Run tests
python3 -m unittest discover -s tests

echo "Validation complete."