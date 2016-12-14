# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 14:31:42 2016

@author: Anshul Kanakia
"""
from linecache import getline
import os

class JoinCSV(object):
    @staticmethod
    def get_default_settings():
        return {
            'file': None,
            'file_match_string': None,
            'no_header_row': False,
            'destination_folder': None,
            'source_path': None}

    def __init__(self, settings):
        self.settings = settings
        if not self.settings['destination_folder']:
            self.settings['destination_folder'] = self.settings['source_path']

    def join(self):
        # Create destination file and write header row if we need to
        dfh = open(os.path.join(self.settings['destination_folder'], self.settings['file']), 'w')
        file_list = self._get_file_list()
        if not self.settings['no_header_row']:
            dfh.write(getline(file_list[0], 1))

        # Open and write contents of each matched file
        header_offset = 1 if self.settings['no_header_row'] else 2
        for infile in file_list:
            num_rows = sum(1 for line in open(infile) if line.rstrip())
            for line_index in range(header_offset, num_rows + 1):
                dfh.write(getline(infile, line_index))

        dfh.close()


    def _get_file_list(self):
        path = self.settings['source_path']
        matchstr = self.settings['file_match_string']

        # Get all file names in top-level directory
        for (dirpath, dirnames, filenames) in os.walk(self.settings['source_path']):
            return [os.path.join(path, f) for f in filenames if (f.find(matchstr) >= 0)]