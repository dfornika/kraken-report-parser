#!/usr/bin/env python

import sys
import pprint
import re

f = open(sys.argv[1], 'r')
target_organism = sys.argv[2].lower()
threshold_percentage = float(sys.argv[3])

pp = pprint.PrettyPrinter(indent=2)

def calculate_depth(clade_name):
    """Node depth is represented by number of spaces before the
       clade name (Each level indented by 2 spaces).
    """
    num_spaces = len(re.split("\S+", clade_name)[0])
    assert num_spaces % 2 == 0, "Odd number of spaces before clade name. Should be multiple of two."
    depth = num_spaces / 2
    return depth

kraken_line = {}
kraken_data = []
target_organism_depth = 1000

for line in f:
    # Parse each line of the kraken report into a dict
    line = line.rstrip('\n').split("\t")
    kraken_line['percent_reads_clade'] = float(line[0])
    kraken_line['num_reads_clade'] = int(line[1])
    kraken_line['num_reads_taxon'] = int(line[2])
    kraken_line['rank_code'] = line[3]
    kraken_line['ncbi_taxonomy_id'] = line[4]
    kraken_line['name'] = line[5]
    kraken_line['depth'] = calculate_depth(kraken_line['name'])
    kraken_line['name'] = kraken_line['name'].lstrip(' ')

    if (kraken_line['name'].lower() == target_organism):
        target_organism_depth = kraken_line['depth']
    
    kraken_data.append(kraken_line.copy())

contaminants = [d['name'] + ": " + str(d['percent_reads_clade']) + "%" for d
                in kraken_data
                if d['percent_reads_clade'] > threshold_percentage
                and d['depth'] == target_organism_depth
                and d['name'].lower() != target_organism]

print contaminants

