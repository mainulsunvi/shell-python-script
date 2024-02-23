#!/usr/bin/python3

import os
import subprocess


def clone_code():
    print("Cloning the Django app...")

    if os.path.isdir("django-notes-app"):
        print("The code directory already exists. Skipping clone.")
        os.chdir("django-notes-app")
    else:
        try:
            subprocess.run(["git", "clone", "https://github.com/LondheShubham153/django-notes-app.git"], check=True)

        except subprocess.CalledProcessError:
            print("Failed to clone the code.")
            return False

    return True


def install_requirements():
    print("Installing dependencies...")

    try:
        subprocess.run(["sudo", "apt-get", "update"], check=True)
        subprocess.run(["sudo", "apt-get", "install", "-y", "docker.io", "nginx", "docker-compose"], check=True)

    except subprocess.CalledProcessError:
        print("Failed to install dependencies.")
        return False

    return True


def services_restart():
    print("Performing required restarts...")

    try:
        subprocess.run(["sudo", "chown", "$USER", "/var/run/docker.sock"], check=True)
        subprocess.run(["sudo", "systemctl", "enable", "docker"], check=True)
        subprocess.run(["sudo", "systemctl", "enable", "nginx"], check=True)
        subprocess.run(["sudo", "systemctl", "restart", "docker"], check=True)

    except subprocess.CalledProcessError:
        print("Failed to change ownership of docker.sock.")
        return False

    return True


def deploy_code():
    print("Building and deploying the Django app...")

    try:
        os.chdir("django-notes-app")
        subprocess.run(["docker", "build", "-t", "notes-app", "."], check=True)
        subprocess.run(["docker-compose", "up", "-d"], check=True)
    except subprocess.CalledProcessError:
        print("Failed to build and deploy the app.")
        return False

    return True


if __name__ == "__main__":

    print("********** DEPLOYMENT STARTED *********")

    if not clone_code():
        os.chdir("django-notes-app")

    if not install_requirements():
        exit(1)

    if not services_restart():
        exit(1)

    if not deploy_code():
        print("Deployment failed. Mailing the admin...")
        exit(1)

    print("********** DEPLOYMENT DONE *********")
