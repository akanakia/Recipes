# -*- coding: utf-8 -*-
"""
Created on Wed Dec 07 12:11:53 2016

@author: Anshul Kanakia
"""
from linecache import getline
import random
import os

class ShuffleCSV(object):
    @staticmethod
    def get_default_settings():
        return {
            'file': None,
            'no_header_row': False,
            'destination_folder': None,
            'overwrite': False}


    def __init__(self, settings):
        self.settings = settings
        if not self.settings['destination_folder']:
            self.settings['destination_folder'] = os.path.split(self.settings['file'])[0]

    def shuffle(self):
        infile = self.settings['file']
        header_offset = 1 if self.settings['no_header_row'] else 2
        num_rows = sum(1 for line in open(infile) if line.rstrip()) # includes header row
        line_indices = range(header_offset, num_rows + 1)
        random.shuffle(line_indices)

        outfile = self._get_out_filename()
        outfp = open(outfile, 'w')
        if not self.settings['no_header_row']:
            outfp.write(getline(infile, 1))

        for line_index in line_indices:
            outfp.write(getline(self.settings['file'], line_index))
        outfp.close()

        if (self.settings['overwrite']):
            os.remove(infile)
            while (os.path.exists(infile)):
                pass # wait until the file is actually deleted to prevent a race condition
            os.rename(outfile, infile)


    def _get_out_filename(self):
        if self.settings['overwrite']:
            return self.settings['file'] + ".temp"

        return os.path.join(
            self.settings['destination_folder'],
            'shuffled-' + os.path.split(self.settings['file'])[1])