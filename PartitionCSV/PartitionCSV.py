# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 09:09:57 2016

@author: Anshul Kanakia
"""
from linecache import getline
import os

class PartitionCSV(object):
    @staticmethod
    def get_default_settings():
        return {
            'file': None,
            'no_header_row': False,
            'destination_folder': None,
            'partition_size': 100,
            'num_partitions': 0}


    def __init__(self, settings):
        self.settings = settings
        if not self.settings['destination_folder']:
            self.settings['destination_folder'] = os.path.split(self.settings['file'])[0]


    def partition(self):
        infile = self.settings['file']
        header_offset = 1 if self.settings['no_header_row'] else 2
        num_rows = sum(1 for line in open(infile) if line.rstrip()) - (header_offset - 1) # does not include header
        line_indices = range(header_offset, num_rows + 1 + (header_offset - 1))

        partition_vector = None
        if self.settings['num_partitions'] > 0:
            partition_vector = self._pv_from_np(num_rows, self.settings['num_partitions'])
        else:
            partition_vector = self._pv_from_ps(num_rows, self.settings['partition_size'])

        partition = 0
        next_stop_index = line_indices[0] + partition_vector[0]
        outfile = self._get_out_filename(line_indices[0], next_stop_index)
        outfp = open(outfile, 'w')
        if not self.settings['no_header_row']:
            outfp.write(getline(infile, 1))

        for line_index in line_indices:
            if (line_index == next_stop_index):
                outfp.close()
                partition += 1
                next_stop_index = line_index + partition_vector[partition]
                outfile = self._get_out_filename(line_index, next_stop_index)
                outfp = open(outfile, 'w')
                if not self.settings['no_header_row']:
                    outfp.write(getline(infile, 1))

            outfp.write(getline(infile, line_index))
        outfp.close()


    def _get_out_filename(self, start_index, end_index):
        return os.path.join(
            self.settings['destination_folder'],
            str(start_index) + "_" + str(end_index - 1) + "_" + os.path.split(self.settings['file'])[1])

    def _pv_from_np(self, nr, np):
        """
        Arguments
        ---------
        nr: int
            Total number of rows in the CSV (not including header row, if present).
        np: int
            Total number of desired partitions.

        Returns
        -------
        list
            List containing all the partition sizes for each file.
        """
        rem = nr % np
        div = nr / np
        pv = [div] * np

        i = 0
        for _ in range(rem):
            pv[i] += 1
            i += 1
            if i == len(pv):
                i = 0
        return pv


    def _pv_from_ps(self, nr, ps):
        """
        Arguments
        ---------
        nr: int
            Total number of rows in the CSV (not including header row, if present).
        ps: int
            Desired partition size (number of rows) for each file.

        Returns
        -------
        list
            List containing all the partition sizes for each file.
        """
        rem = nr % ps
        div = nr / ps
        return [ps] * div if rem == 0 else ([ps] * div) + [rem]