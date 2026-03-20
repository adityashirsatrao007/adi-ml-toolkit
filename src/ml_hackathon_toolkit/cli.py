import os
import sys
import subprocess
import platform

def install_gh_cli():
    print("Installing GitHub CLI...")
    system = platform.system().lower()
    if system == "windows":
        subprocess.run(["winget", "install", "--id", "GitHub.cli"], shell=True)
    elif system == "darwin":
        subprocess.run(["brew", "install", "gh"])
    elif system == "linux":
        print("Please follow instructions at https://github.com/cli/cli/blob/trunk/docs/install_linux.md")
    else:
        print("Unsupported OS for automated gh cli installation.")

def install_vercel():
    print("Installing Vercel CLI...")
    try:
        subprocess.run(["npm", "install", "-g", "vercel"], check=True, shell=True)
    except Exception as e:
        print(f"Failed to install Vercel CLI (is Node.js/npm installed?). Error: {e}")

def install_aws_cli():
    print("Installing AWS CLI...")
    subprocess.run([sys.executable, "-m", "pip", "install", "awscli"])

def install_azure_cli():
    print("Installing Azure CLI...")
    subprocess.run([sys.executable, "-m", "pip", "install", "azure-cli"])

def install_firebase_cli():
    print("Installing Firebase CLI...")
    try:
        subprocess.run(["npm", "install", "-g", "firebase-tools"], check=True, shell=True)
    except Exception as e:
        print(f"Failed to install Firebase CLI (is Node.js/npm installed?). Error: {e}")

def install_netlify_cli():
    print("Installing Netlify CLI...")
    try:
        subprocess.run(["npm", "install", "-g", "netlify-cli"], check=True, shell=True)
    except Exception as e:
        print(f"Failed to install Netlify CLI (is Node.js/npm installed?). Error: {e}")

def install_heroku_cli():
    print("Installing Heroku CLI...")
    try:
        subprocess.run(["npm", "install", "-g", "heroku"], check=True, shell=True)
    except Exception as e:
        print(f"Failed to install Heroku CLI (is Node.js/npm installed?). Error: {e}")

def install_gcp_cli():
    print("Installing Google Cloud CLI...")
    print("For GCP CLI, please download the official installer: https://cloud.google.com/sdk/docs/install")
    print("Or if using Windows with winget: winget install Google.CloudSDK")

def main():
    print("=======================================")
    print("Welcome to ML Hackathon Toolkit Setup!")
    print("=======================================")
    print("This script will help you install common hackathon CLIs.")
    
    install_gh = input("Install GitHub CLI? [y/N]: ").lower().startswith('y')
    if install_gh:
        install_gh_cli()
        
    install_v = input("Install Vercel CLI? [y/N]: ").lower().startswith('y')
    if install_v:
        install_vercel()
        
    install_aws = input("Install AWS CLI? [y/N]: ").lower().startswith('y')
    if install_aws:
        install_aws_cli()
        
    install_azure = input("Install Azure CLI? [y/N]: ").lower().startswith('y')
    if install_azure:
        install_azure_cli()
        
    install_firebase = input("Install Firebase CLI? [y/N]: ").lower().startswith('y')
    if install_firebase:
        install_firebase_cli()
        
    install_netlify = input("Install Netlify CLI? [y/N]: ").lower().startswith('y')
    if install_netlify:
        install_netlify_cli()
        
    install_heroku = input("Install Heroku CLI? [y/N]: ").lower().startswith('y')
    if install_heroku:
        install_heroku_cli()
        
    install_gcp = input("Install Google Cloud (GCP) CLI? [y/N]: ").lower().startswith('y')
    if install_gcp:
        install_gcp_cli()
        
    print("\nSetup complete. Good luck on your hackathon!")

if __name__ == "__main__":
    main()
