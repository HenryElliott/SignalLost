#!/bin/bash

# Check if python3 exists
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found. Please install it."
    read -p "Press Enter to exit..."
    exit 1
fi

# Run the game
python3 ./main.py

# Keep terminal open after exit (if run from GUI)
read -p "Press Enter to exit..."
