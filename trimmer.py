#!/usr/bin/env python
# encoding: utf-8

"""
trimmer.py
Created by Ben Pote on 1/14/14

The author may be contacted at ben.pote@gmail.com

Takes a fastq file and trims off a certain number of lines.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

import gzip
import argparse
import sys

#####get arguments
def get_args():
    """ parse sys.argv """
    #initiate parser	
    parser = argparse.ArgumentParser()
    #add commandline argument
    parser.add_argument('-s','--start',
        required=False,
        type=int,
        help='Trim x number of bases from the start')

    
    parser.add_argument('INPUT',
        type=argparse.FileType('rb'),
        default=sys.stdin,
        nargs='?',
        help='VCF file')

    parser.add_argument('OUTPUT',
        type=argparse.FileType('w'),
        default=sys.stdout,
        nargs='?',
        help='VCF file')
    #process arguments
    args = parser.parse_args()
    return args


#### main function
def main(args):
    start = args.start
    fin = enumerate(args.INPUT)
    fout = args.OUTPUT
    end = args.end
    for line in fin:
        count, text = line
        print text[start:]




if __name__ == '__main__':
	args = get_args()
	main(args)
