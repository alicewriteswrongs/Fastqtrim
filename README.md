#Trimmer for fastq files

A quick python script for trimming a specified number of bases from the beginning of each read in a fastq file.

###Usage

usage: python trimmer.py [-h] [-s START] [INPUT] [OUTPUT]

*	[-s START] trims all bases before this point from the alignment
*	[INPUT]	file to be modified
*	[OUTPUT] defaults to stdout, file write not yet implemented
