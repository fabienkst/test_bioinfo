#!/usr/local/bin/python

import os
import argparse
import re
import pandas as pd

def read_table(input):
    f = pd.read_table(input)
    print(f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Test", description="Main test program")
    mandatory = parser.add_argument_group("Mandatory options")
    mandatory.add_argument("--input", "-i", dest="input", required=True, help="Required input data")

    args = parser.parse_args()

    read_table(args.input)

