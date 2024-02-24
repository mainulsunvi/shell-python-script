#!/usr/bin/python3

import os
import subprocess
import shutil


def src_dir():
    main_dir = os.path.join(os.path.abspath(os.pardir), "file-sync")
    return shutil.copytree(
        os.getcwd(),
        os.path.join(main_dir, "src"),
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns(".git", ".idea"),
    )


def rsync_check():
    rsync = subprocess.run(
        ["rsync", "--version"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        shell=True,
    )

    if os.name != "nt" and rsync.returncode == 1:
        print(f"Rsync is Installed... \n")
    else:
        try:
            subprocess.run(["sudo", "apt-get", "install", "-y", "rsync"], check=True)
        except subprocess.CalledProcessError:
            print("Cannot install Rsync, Try again!")
            return False

    return True


def sync_files(source, dest):
    if rsync_check():
        try:
            subprocess.run(
                ["rsync", "-avz", "--delete", f"{source}/", f"{dest}"], check=True
            )
        except subprocess.CalledProcessError:
            return False

    return True


if __name__ == "__main__":
    src = src_dir()
    dest = os.path.join(os.path.abspath(os.pardir), "file-sync", "dest")

    print(f"\n*********** FILE SYNC STARTED ***********\n")

    if not sync_files(src, dest):
        print("Failed to Sync Files")
        exit(1)

    print(f"\n*********** FILE SYNC DONE ***********\n")
