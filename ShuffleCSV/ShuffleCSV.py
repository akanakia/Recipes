# -*- coding: utf-8 -*-
"""
Created on Wed Dec 07 12:11:53 2016

@author: Anshul Kanakia
"""

from linecache import getline
import random
import os

class ShuffleCSV(object):
    def __init__(self, settings):
        self.settings = settings

    def shuffle(self):
        infile = self.settings['file']
        header_offset = 1 if self.settings['no_header_row'] else 2
        num_rows = sum(1 for line in open(infile) if line.rstrip())
        line_indices = range(header_offset, num_rows + 1)
        random.shuffle(line_indices)

        outfile = 'shuffled-' + os.path.split(infile)[1]
        if self.settings['destination_folder']:
            outfile = os.path.join(self.settings['destination_folder'], outfile)
        else:
            outfile = os.path.join(os.path.split(infile)[0], outfile)

        outfp = open(outfile, 'w')
        if not self.settings['no_header_row']:
            outfp.write(getline(infile, 1))

        for line_index in line_indices:
            outfp.write(getline(self.settings['file'], line_index))
        outfp.close()

    @staticmethod
    def get_default_settings():
        return {
            'file': "",
            'no_header_row': False,
            'shuffle_in_place': False,
            'destination_folder': None}