# -*- coding: utf-8 -*-
"""
Created on Wed Dec 07 12:05:23 2016

@author: Anshul Kanakia
"""
import argparse
import os

def checkext(choices):
    """
    Restricts possible file extensions as valid input.

    Usage
    -----
    argparse.ArgumentParser().add_argument('<argument-name>', action=checkext({<valid-file-extensions>}))
    """
    class Act(argparse.Action):
        def __call__(self, parser, namespace, filename, option_string=None):
            ext = os.path.splitext(filename)[1][1:]
            if ext not in choices:
                option_string = '({})'.format(option_string) if option_string else ''
                parser.error("File not supported. Supported file types are {}{}".format(choices, option_string))
            else:
                if not os.path.exists(filename):
                    parser.error("File {} not found.".format(filename))
                else:
                    setattr(namespace, self.dest, filename)
    return Act

def checkvaliddir():
    """
    Ensures that the specified directory exists.

    Usage
    -----
    argparse.ArgumentParser().add_argument('<argument-name>', action=checkvaliddir)
    """
    class Act(argparse.Action):
        def __call__(self, parser, namespace, dirpath, option_string=None):
            if not os.path.isdir(dirpath):
                option_string = '({})'.format(option_string) if option_string else ''
                parser.error("{}{} is not a valid directory.".format(dirpath, option_string))
            else:
                setattr(namespace, self.dest, dirpath)
    return Act