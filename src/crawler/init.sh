#!/bin/bash

dirs[1]="logs"
dirs[2]="rdfData"

for dir in "${dirs[@]}"; do
    if ! [ -d "$dir" ]; then
        mkdir "$dir"
        echo "Added missing folder $dir"
    fi
done

