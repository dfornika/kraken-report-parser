#!/usr/bin/env python

import sys

f = open(sys.argv[1], 'r')
rank = sys.argv[2].upper()
percent_threshold = float(sys.argv[3])

assert rank in {'U', 'D', 'K', 'P', 'C', 'O', 'F', 'G', 'S'}, "Rank must be one of [(U)nclassified, (D)omain, (K)ingdom, (P)hylum, (C)lass, (O)rder, (F)amily, (G)enus, or (S)pecies.]"

total_reads = 0

header = "percent_reads_in_clade\tnum_reads_in_clade\ttaxid\tname"

print header

for line in f:
    line = line.rstrip('\n').split("\t")
    percentage_reads_clade = float(line[0])
    number_reads_clade = int(line[1])
    number_reads_taxon = int(line[2])
    rank_code = line[3]
    ncbi_taxonomy_id = line[4]
    clade_name = line[5].lstrip(' ')

    total_reads += number_reads_taxon

    if clade_name == "unclassified":
        total_reads += number_reads_clade
    elif clade_name == "root":
        total_reads += number_reads_clade

    percent_reads_in_clade = number_reads_clade / float(total_reads) * 100
    
    if rank_code != rank:
        continue
    
    if percent_reads_in_clade > percent_threshold:
        print str('%.3f' % (percent_reads_in_clade)) + '\t' + str(number_reads_clade) + '\t' + ncbi_taxonomy_id + '\t' + clade_name

    

