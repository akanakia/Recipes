# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 09:10:08 2016

@author: Anshul Kanakia
"""
import argparse
import argparseHelpers
from PartitionCSV import PartitionCSV

def parse_args():
    argparser = argparse.ArgumentParser(description="Partition a CSV file into smaller files.")

    argparser.add_argument(
        "csvfile",
        action=argparseHelpers.checkext({'csv'}),
        help="The file path of the CSV file to partition.")

    argparser.add_argument(
        "-r",
        "--noheader",
        action="store_true",
        help="The first row of the CSV will be not be treated as a header if this option is specified.")

    argparser.add_argument(
        "-d",
        "--destinationfolder",
        action=argparseHelpers.checkvaliddir(),
        help="Destination folder for output shuffled CSV file. " + \
            "Has no effect if --inplace [-p] option is also specified.")

    argparser.add_argument(
        "-s",
        "--partitionsize",
        type=int,
        help="The partition size or equivalently, number of data rows in each partitioned file. " + \
            "This is a best effort value. " + \
            "Partitioned files will have rows as close to this value as possible. " + \
            "Default value for this parameter is 100. " + \
            "This value is ignored if option --numpartitions [-n] is also specified.")

    argparser.add_argument(
        "-n",
        "--numpartitions",
        type=int,
        help="The number of partitioned files to create. " + \
        "The input file will be partitioned into this many smaller CSV files. " + \
        "The smaller CSV files will have a similar partition size but " + \
        "are not gauranteed to each have the same number of rows.")

    return argparser.parse_args()

def fill_settings(args):
    settings = PartitionCSV.get_default_settings()
    settings['file'] = args.csvfile
    settings['no_header_row'] = args.noheader
    if args.destinationfolder:
        settings['destination_folder'] = args.destinationfolder
    if args.partitionsize:
        settings['partition_size'] = args.partitionsize
    if args.numpartitions:
        settings['num_partitions'] = args.numpartitions

    return settings

def main():
    args = parse_args()
    settings = fill_settings(args)
    partitioner = PartitionCSV(settings)
    partitioner.partition()

if __name__ == "__main__":
    main()