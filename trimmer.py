#!/usr/bin/env python
# encoding: utf-8

"""
trimmer.py
Created by Ben Pote on 1/14/14

The author may be contacted at ben.pote@gmail.com

Takes a fastq file and trims off a certain number of lines.
"""

import argparse

def get_args():
	""" parse sys.argv """
	#initiate parser	
	parser = argparse.ArgumentParser()
	#add commandline argument
	parser.add_argument('-s','--start',
		required=False,
		type=int,
		help='Trim x number of bases from the start')
	#process arguments
	args = parser.parse_args()
	return args

get_args