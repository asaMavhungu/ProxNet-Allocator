# ProxNet-Allocator
Cellphone Tower frequency allocator

This script processes cell towers data from a CSV file, assigns frequencies to cell towers, and prints the results.

- The first 6 cells are assigned distinct frequencies (105 to 110).
- The remaining cells are assigned frequencies based on the farthest of the 6 closest distinct frequencies.

## Usage
Run the script with the following command:

`python main.py --filename your_input_file.csv`

Replace your_input_file.csv with the path to your CSV file containing cell towers data.

## Command-Line Options
--filename or -f: Specify the CSV file containing cell towers data. Default is cell_towers.csv.

## Files
Files used in the implementation:

### 1. main.py
This is the main script that processes the cell towers data, assigns frequencies, and prints the results.

### 2. v1.ipynb
This file a jupyter notebook with an implementation adapted from a 1-dimentional solution

### 3. v2.ipynb
This file a jupyter notebook with an implementation for the 2-dimentional solution

### 4. cell_towers.csv
This file contains the example data for the cellphone towers