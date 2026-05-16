import numpy as np
import json

with open("scrambles.json","r") as file:
	data = json.load(file)

moves = ["U", "R", "L", "B", "U'", "R'", "L'", "B'"]

nNS = 131

cases = [" R U R", " L' U' L'", " B U' R' U", " R' L R B'", " B R U'", " L' U' L", " R U R' B' L' U", " B U' R U'", " B U' R U B", " B' L' U' L B'", " B L' B'", " B' R B", " U B L'", " L' B' L", " B' U R' B' U ", " L R' B U R'", " R' U' B L' U' L", " U B R' L R B'"]
nCases = len(cases)

nMoves = int(input("Enter number of random moves: "))

while True:
	alg = data[str(np.random.randint(nNS)+1)]
	scram = alg[np.random.randint(len(alg))]
	c = cases[np.random.randint(nCases)]
	scram = scram + c
	check = False
	while check == False:
		check = True
		for i in range(len(scram)):
			if i >= 3 and i < len(scram) and scram[i] != " " and scram[i] != "'":
				if scram[i] == scram[i-2] and scram[i] != "'" and (i == len(scram)-1 or scram[i+1] != "'"):
					scram = scram[:i-2] + scram[i] + "'" + scram[i+1:]
					check = False
				elif scram[i] == scram[i-3] and scram[i-2] == "'" and (i < len(scram)-1 and scram[i+1] == "'"):
					scram = scram[:i-2] + scram[i+2:]
					check = False
				elif scram[i] == scram[i-2] and (i < len(scram)-1 and scram[i+1] == "'"):
					scram = scram[:i-3] + scram[i+2:]
					check = False
				elif scram[i] == scram[i-3] and scram[i-2] == "'" and (i == len(scram)-1 or scram[i+1] != "'"):
					scram = scram[:i-3] + scram[i+2:]
					check = False

	for i in range(nMoves):
		m = moves[np.random.randint(8)]
		while m == scram[-1] or m == scram[-2] + "'" or m == scram[-1] + "'" or m == scram[-2]:
			m = moves[np.random.randint(8)]
		scram = scram + " " + m
	input(scram)
