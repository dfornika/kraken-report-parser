#!/usr/bin/env python

import sys
import re
import pprint
import json

from treelib import Node, Tree

f = open(sys.argv[1], 'r')

def calculate_depth(clade_name):
    num_spaces = len(re.split("\S+", clade_name)[0])
    assert num_spaces % 2 == 0, "Odd number of spaces before clade name. Should be multiple of two."
    depth = num_spaces / 2
    return depth

tree = Tree()
previous = None

for line in f:
    line = line.rstrip('\n').split("\t")
    percentage_reads_clade = float(line[0])
    number_reads_clade = int(line[1])
    number_reads_taxon = int(line[2])
    rank_code = line[3]
    ncbi_taxonomy_id = line[4]
    clade_name = line[5]
    depth = calculate_depth(clade_name)
    clade_name = clade_name.lstrip(' ')
    
    if clade_name == "unclassified":
        unclassified = Node(tag = clade_name,
                            identifier = ncbi_taxonomy_id,
                            data = { "num_reads": number_reads_taxon,
                                     "rank_code": rank_code})
    elif clade_name == "root":
        tree.create_node(tag = clade_name,
                         identifier = ncbi_taxonomy_id, 
                         data = { "num_reads": number_reads_taxon,
                                  "rank_code": rank_code,
                                  "depth": depth})
        previous = tree.get_node(str(ncbi_taxonomy_id))
    elif depth > tree.depth(previous):
        tree.create_node(tag = clade_name,
                         identifier = ncbi_taxonomy_id,
                         data = { "num_reads": number_reads_taxon,
                                  "rank_code": rank_code,
                                  "depth": depth},
                         parent = previous)
        previous = tree.get_node(str(ncbi_taxonomy_id))
    elif depth == tree.depth(previous):
        tree.create_node(tag = clade_name,
                         identifier = ncbi_taxonomy_id,
                         data = { "num_reads": number_reads_taxon,
                                  "rank_code": rank_code,
                                  "depth": depth},
                         parent = tree.parent(previous.identifier))
        previous = tree.get_node(str(ncbi_taxonomy_id))
    elif depth < tree.depth(previous):
        previous_search = previous
        while(tree.depth(previous_search) > depth):
            previous_search = tree.parent(previous_search.identifier)
        tree.create_node(tag = clade_name,
                         identifier = ncbi_taxonomy_id,
                         data = { "num_reads": number_reads_taxon,
                                  "rank_code": rank_code,
                                  "depth": depth},
                         parent = tree.parent(previous_search.identifier))
        previous = tree.get_node(str(ncbi_taxonomy_id))

