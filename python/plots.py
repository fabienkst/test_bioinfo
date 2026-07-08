#!/usr/local/bin/python

import matplotlib.pyplot as plt
import pandas as pd
import numpy as npc
import argparse
import os
import logging

def save_figure(plt, outfile_prefix, ext="pdf"):
	file = f"{outfile_prefix}.{ext}"
	plt.savefig(file, format=ext)

def read_data(input_data):
	dt = pd.read_table(input_data, sep="\t")
	print(dt)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog="plots.py", description="Script for designing plots")
	mandatory = parser.add_argument_group('Mandatory options.')
	mandatory.add_argument('--input', '-i', required=True, help="Input data.")
	mandatory.add_argument('--output', '-o', required=True, help="Output path for results.")

	args = parser.parse_args()

	pd.set_option("display.max_columns", None)
	pd.set_option("display.max_colwidth",None)
	read_data(args.input)