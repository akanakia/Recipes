# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 14:31:49 2016

@author: Anshul Kanakia
"""
import argparse
import argparseHelpers
from JoinCSV import JoinCSV

def parse_args():
    argparser = argparse.ArgumentParser(description="Partition a CSV file into smaller files.")

    argparser.add_argument(
        "file",
        help="The name of the generated output file containing all the joined data.")

    argparser.add_argument(
        "filematchstring",
        help="All files containing this substring in their name will be joined.")

    argparser.add_argument(
        "sourcepath",
        action=argparseHelpers.checkvaliddir(),
        help="This folder will be searched for files to join.")

    argparser.add_argument(
        "-r",
        "--noheader",
        action="store_true",
        help="The first row of the CSV will be not be treated as a header if this option is specified.")

    argparser.add_argument(
        "-d",
        "--destinationfolder",
        action=argparseHelpers.checkvaliddir(),
        help="If specified, this folder will be used to store output joined CSV file instead of the source path.")

    return argparser.parse_args()

def fill_settings(args):
    settings = JoinCSV.get_default_settings()
    settings['file'] = args.file
    settings['file_match_string'] = args.filematchstring
    settings['source_path'] = args.sourcepath
    settings['no_header_row'] = args.noheader
    if args.destinationfolder:
        settings['destination_folder'] = args.destinationfolder


    return settings

def main():
    args = parse_args()
    settings = fill_settings(args)
    joiner = JoinCSV(settings)
    joiner.join()

if __name__ == "__main__":
    main()