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
        
    print("Setup complete. Good luck on your hackathon!")

if __name__ == "__main__":
    main()
