#!/usr/bin/env python

import sys
import re
import pprint
import json

from treelib import Node, Tree

f = open(sys.argv[1], 'r')
pp = pprint.PrettyPrinter(indent=2)

def calculate_depth(clade_name):
    """Node depth is represented by number of spaces before the
       clade name (Each level indented by 2 spaces).
    """
    num_spaces = len(re.split("\S+", clade_name)[0])
    assert num_spaces % 2 == 0, "Odd number of spaces before clade name. Should be multiple of two."
    depth = num_spaces / 2
    return depth

tree = Tree()
previous = None
kraken_data = {}

def add_node(tree, parent, data_dict):
    tree.create_node(tag = data_dict['name'],
                     identifier = data_dict['ncbi_taxonomy_id'],
                     data = data_dict.copy(),
                     parent = parent)

for line in f:
    line = line.rstrip('\n').split("\t")
    kraken_data['percent_reads_clade'] = float(line[0])
    kraken_data['num_reads_clade'] = int(line[1])
    kraken_data['num_reads_taxon'] = int(line[2])
    kraken_data['rank_code'] = line[3]
    kraken_data['ncbi_taxonomy_id'] = line[4]
    kraken_data['name'] = line[5]
    kraken_data['depth'] = calculate_depth(kraken_data['name'])
    kraken_data['name'] = kraken_data['name'].lstrip(' ')
    
    if kraken_data['name'] == "unclassified":
        unclassified = Node(tag = kraken_data['name'],
                            identifier = kraken_data['ncbi_taxonomy_id'],
                            data = kraken_data)
    elif kraken_data['name'] == "root":
        add_node(tree, None, kraken_data)
        previous = tree.get_node(kraken_data['ncbi_taxonomy_id'])
    elif kraken_data['depth'] > tree.depth(previous):
        add_node(tree, previous, kraken_data)
        previous = tree.get_node(kraken_data['ncbi_taxonomy_id'])
    elif kraken_data['depth'] == tree.depth(previous):
        add_node(tree, tree.parent(previous.identifier), kraken_data)
        previous = tree.get_node(kraken_data['ncbi_taxonomy_id'])
    elif kraken_data['depth'] < tree.depth(previous):
        previous_search = previous
        while(tree.depth(previous_search) > kraken_data['depth']):
            previous_search = tree.parent(previous_search.identifier)
        add_node(tree, tree.parent(previous_search.identifier), kraken_data)
        previous = tree.get_node(kraken_data['ncbi_taxonomy_id'])

tree_dict = tree.to_dict(with_data=True)

def transform(tree_dict):
    for key in tree_dict.keys():
        for data_key in tree_dict[key]['data'].keys():
            tree_dict[data_key] = tree_dict[key]['data'][data_key]
        tree_dict[key].pop('data', None)
        tree_dict.pop('depth', None)
    if 'children' in tree_dict[key]:
        for child in tree_dict[key]['children']:
            transform(child)
        tree_dict['children'] = tree_dict[key]['children']
        tree_dict[key].pop('children', None)
    tree_dict.pop(key, None)
    tree_dict.pop('root', None)

transform(tree_dict)

print json.dumps(tree_dict)

