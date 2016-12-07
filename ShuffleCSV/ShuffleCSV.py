# -*- coding: utf-8 -*-
"""
Created on Wed Dec 07 12:11:53 2016

@author: Anshul Kanakia
"""
class ShuffleCSV(object):
    def __init__(self, settings):
        self.settings = settings

    def shuffle(self):
        print 'Will shuffle {}'.format(self.settings['file'])
        print self.settings

    @staticmethod
    def get_default_settings():
        return {
            'file': "",
            'no_header_row': False,
            'shuffle_in_place': False,
            'destination_folder': ""}