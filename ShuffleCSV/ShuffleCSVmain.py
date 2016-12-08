# -*- coding: utf-8 -*-
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
        "-p", \
        "--inplace", \
        action="store_true", \
        help="The original CSV will be overriden with the shuffled CSV.")

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
    settings['shuffle_in_place'] = args.inplace
    if ((not args.inplace) and args.destinationfolder):
        settings['destination_folder'] = args.destinationfolder

    return settings


def main():
    args = parse_args()
    settings = set_ShuffleCSV_settings(args)
    shuffler = ShuffleCSV(settings)
    shuffler.shuffle()

if __name__ == "__main__":
    main()