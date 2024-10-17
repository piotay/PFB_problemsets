#!/usr/bin/env python3 
import sys

fav_thing = sys.argv[1]

favs = {"book" : "HHGTG", "song" : "Lipgloss", "tree" : "Southern Live Oak"}

favs["organism"] = "oat"

favs["organism"] = "flossy"

favs[fav_thing] = input(f"What is your fav {fav_thing}?")

print(f"Key: {fav_thing}\tValue:{favs[fav_thing]}")

