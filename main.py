import pandas as pd
import argparse
import os

import math

class Cell:
	def __init__(self, cell_id, easting, northing, lon, lat):
		self.cell_id = cell_id
		self.easting = easting
		self.northing = northing
		self.lon = lon
		self.lat = lat
		self.frequency: int = 0

	def __repr__(self):
		return f"Cell_id: {self.cell_id}\t Easting: {self.easting} \t Northing: {self.northing} \t Frequency = {self.frequency}"

	def __str__(self):
		return f"Cell_id: {self.cell_id}\t Easting: {self.easting} \t Northing: {self.northing} \t Frequency = {self.frequency}"

def calculate_distance(cell1, cell2):
	return math.sqrt((cell1.easting - cell2.easting)**2 + (cell1.northing - cell2.northing)**2)


def is_valid_file(parser, arg):
	if not os.path.isfile(arg):
		parser.error(f"The file '{arg}' does not exist.")
	elif not arg.endswith('.csv'):
		parser.error("Invalid file format. Please provide a CSV file.")
	return arg


def main():
	parser = argparse.ArgumentParser(description='Process cell towers data.')
	parser.add_argument('--filename', '-f', type=lambda x: is_valid_file(parser, x), default='cell_towers.csv', help='CSV file containing cell towers data')


	args = parser.parse_args()

	raw_cells = []
	cells = []

	data = pd.read_csv(args.filename)

	# Iterate over the rows of the DataFrame and create Cell objects
	for index, row in data.iterrows():
		raw_cell = Cell(row['Cell ID'], row['Easting'], row['Northing'], row['Long'], row['Lat'])
		raw_cells.append(raw_cell)

	# Reverse list so that we can simulate the list as a queue with FIFO
	# Could implement the queue from the collections library but that is unnecessary overhead
	raw_cells.reverse()

	# The first 6 cells have distinct frequencies

	size = len(raw_cells)

	num = 6 if size > 6 else size
	for i in range(6):
		cell: Cell = raw_cells.pop()
		cell.frequency = i+105
		cells.append(cell)

	for i in range(len(raw_cells)):
		new_cell = raw_cells.pop()

		freqs = {
			105: float('inf'),
			106: float('inf'),
			107: float('inf'),
			108: float('inf'),
			109: float('inf'),
			110: float('inf')
		}

		for cell in cells:
			distance = calculate_distance(new_cell, cell)
			freqs[cell.frequency] = min(distance, freqs[cell.frequency])

		# Get the frequency associated with the closest tower
		# Use Lamda function to prevent function call from raising an exception error when key not found
		max_key = max(freqs, key=lambda k: freqs.get(k, float('inf')))
		new_cell.frequency = max_key
		cells.append(new_cell)

	for cell in cells:
		print(cell)


if __name__ == '__main__':
	main()