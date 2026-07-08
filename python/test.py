#!/usr/local/bin/python

import os
import argparse
import re

def test_calcul(input_data):
    new_input = int(input_data)*2
    return str(new_input)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Test", description="Main test program")
    mandatory = parser.add_argument_group("Mandatory options")
    mandatory.add_argument("--input", "-i", dest="input", required=True, help="Required input data")

    args = parser.parse_args()

    print ("Welcome ! \n" + args.input)
    print("Processing...")
    New_data = test_calcul(args.input)
    print("Output is \n" + New_data)