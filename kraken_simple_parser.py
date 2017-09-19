#!/usr/bin/env python

import sys

f = open(sys.argv[1], 'r')
selected_rank_code = sys.argv[2].upper()
percent_threshold = float(sys.argv[3])

rank_codes = {'U', 'D', 'K', 'P', 'C', 'O', 'F', 'G', 'S', '-'}
assert rank_code in rank_codes, "Rank must be one of [(U)nclassified, (D)omain, (K)ingdom, (P)hylum, (C)lass, (O)rder, (F)amily, (G)enus, or (S)pecies.]"

total_reads = 0
unclassified_reads = 0
total_reads_reported = 0
other_reads = 0

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

    if clade_name == "unclassified":
        unclassified_reads = number_reads_clade
        total_reads += number_reads_clade
        continue
    elif clade_name == "root":
        total_reads += number_reads_clade
        continue

    percent_reads_in_clade = number_reads_clade / float(total_reads) * 100

    if rank_code == selected_rank_code and percent_reads_in_clade >= percent_threshold:
        print str('%.3f' % (percent_reads_in_clade)) + '\t' + str(number_reads_clade) + '\t' + ncbi_taxonomy_id + '\t' + clade_name
        total_reads_reported += number_reads_clade


print str('%.3f' % (unclassified_reads / float(total_reads) * 100)) + '\t' + str(unclassified_reads) + '\t\t' + 'unclassified'
total_reads_reported += unclassified_reads
other_reads = total_reads - total_reads_reported
print str('%.3f' % (other_reads / float(total_reads) * 100)) + '\t' + str(other_reads) + '\t\t' + 'other'
