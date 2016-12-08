# -*- coding: utf-8 -*-
"""
Created on Wed Dec 07 12:10:02 2016

@author: Anshul Kanakia
"""
import argparse
import argparseHelpers
from ShuffleCSV import ShuffleCSV


def parse_args():
    argparser = argparse.ArgumentParser(description="Shuffle the rows of the provided CSV file.")

    argparser.add_argument(
        "csvfile", \
        action=argparseHelpers.checkext({'csv'}), \
        help="The file path of the CSV file to shuffle.")

    argparser.add_argument(
        "-n", \
        "--noheader", \
        action="store_true", \
        help="The first row of the CSV will also be shuffled if this option is specified.")

    argparser.add_argument(
        "-o", \
        "--overwrite", \
        action="store_true", \
        help="The original CSV will be overwritten with the shuffled CSV." + \
        "This option may require running in Administrator mode.")

    argparser.add_argument(
        "-d", \
        "--destinationfolder", \
        action=argparseHelpers.checkvaliddir(), \
        help="Destination folder for output shuffled CSV file. " + \
            "Has no effect if --inplace [-p] option is also specified.")
    return argparser.parse_args()


def set_ShuffleCSV_settings(args):
    settings = ShuffleCSV.get_default_settings()
    settings['file'] = args.csvfile
    settings['no_header_row'] = args.noheader
    settings['overwrite'] = args.overwrite
    if ((not args.overwrite) and args.destinationfolder):
        settings['destination_folder'] = args.destinationfolder

    return settings


def main():
    args = parse_args()
    settings = set_ShuffleCSV_settings(args)
    shuffler = ShuffleCSV(settings)
    shuffler.shuffle()

if __name__ == "__main__":
    main()