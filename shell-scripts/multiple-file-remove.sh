#!/usr/bin/bash

removeFile() {
    root_path=$(pwd)
    fileName='hello.py'

    for file in "$root_path"/*/*; do
        if [ "$(basename "$file")" = "$fileName" ]; then
            echo "removing $(basename "$file") ..."
            rm "$file"
            echo "$(basename "$file") is Removed ..."
        fi
    done
}

removeFile
