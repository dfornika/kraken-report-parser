#!/usr/bin/env python

import sys
import fileinput

selected_rank_code = sys.argv[1].upper()
percent_threshold = float(sys.argv[2])
max_columns = int(sys.argv[3])
filenames = sys.argv[4:]

rank_codes = {'U', 'D', 'K', 'P', 'C', 'O', 'F', 'G', 'S'}
assert selected_rank_code in rank_codes, "Rank must be one of [(U)nclassified, (D)omain, (K)ingdom, (P)hylum, (C)lass, (O)rder, (F)amily, (G)enus, or (S)pecies.]"

total_reads = 0
unclassified_reads = 0
total_reads_reported = 0
other_reads = 0
results = []

header = "sample\tpercent_unclassified\tnum_reads_unclassified\tpercent_other\tnum_reads_other"

for i in range(max_columns):
    header += "\tpercent_reads_in_clade" + str(i + 1) + "\tnumber_reads_in_clade" + str(i + 1) + "\tncbi_taxonomy_id" + str(i + 1) + "\tclade_name" + str(i + 1)

print header

for filename in filenames:
    f = open(filename, 'r')
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
            results.append({'percent_reads_in_clade': percent_reads_in_clade, 'number_reads_in_clade': number_reads_clade, 'ncbi_taxonomy_id': ncbi_taxonomy_id, 'clade_name': clade_name})
            total_reads_reported += number_reads_clade

    top_results = sorted(results, key=lambda k: k['percent_reads_in_clade'])[:max_columns]
    
    total_reads_reported += unclassified_reads
    other_reads = total_reads - total_reads_reported
    
    output =  filename + '\t' + \
        str('%.3f' % (unclassified_reads / float(total_reads) * 100)) + '\t' + str(unclassified_reads) + '\t' +\
        str('%.3f' % (other_reads / float(total_reads) * 100)) + '\t' + str(other_reads)

    for result in top_results:
        output += "\t" + str('%.3f' % result['percent_reads_in_clade'])
        output += "\t" + str(result['number_reads_in_clade'])
        output += "\t" + str(result['ncbi_taxonomy_id'])
        output += "\t" + str(result['clade_name'])
        
    print output
        
