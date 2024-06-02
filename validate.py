import os
import subprocess
import sys

def check_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def main():
    print("Validating project...")

    # Check if Python is installed
    if not check_command("python --version"):
        print("Python could not be found. Please install Python.")
        sys.exit(1)

    # Check if pip is installed
    if not check_command("pip --version"):
        print("pip could not be found. Please install pip.")
        sys.exit(1)

    # Check if virtual environment is set up
    if not os.path.isdir("venv"):
        print("Virtual environment not found. Setting up...")
        subprocess.run("python -m venv venv", shell=True)

    # Activate virtual environment
    if os.name == 'nt':
        activate_script = os.path.join("venv", "Scripts", "activate.bat")
    else:
        activate_script = os.path.join("venv", "bin", "activate")
    
    # Install requirements
    subprocess.run(f"{activate_script} && pip install -r requirements.txt", shell=True, check=True)

    # Initialize database
    subprocess.run(f"{activate_script} && python scripts/initialize_db.py", shell=True, check=True)

    # Run tests
    subprocess.run(f"{activate_script} && python -m unittest discover -s tests", shell=True, check=True)

    print("Validation complete.")

if __name__ == "__main__":
    main()