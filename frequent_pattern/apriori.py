#!/bin/python3
#

import sys
from itertools import chain, combinations
from collections import defaultdict

import data
import helper

def items_with_min_sup(itemset, transactionList, min_support, freq):
    output = set()
    local = defaultdict(int)

    for item in itemset:
        for transaction in transactionList:
            if item.issubset(transaction):
                freq[item] += 1
                local[item] += 1

    for item, count in local.items():
        support = float(count) / len(transactionList)
        if support >= min_support:
            output.add(item)

    return output

def apriori(transactions, min_support):
    def normalize_types(data):
        transactionList = list()
        itemset = set()
        for row in data:
            transaction = frozenset(row)
            transactionList.append(transaction)
            for item in transaction:
                itemset.add(frozenset([item]))
        return itemset, transactionList

    itemset, transactionList = normalize_types(transactions)

    freq = defaultdict(int)
    L = dict()

    C1 = items_with_min_sup(itemset, transactionList, min_support, freq)

    currentL = C1
    k = 2
    while currentL != set([]):
        L[k-1] = currentL
        currentL = join(currentL, k)
        currentC = items_with_min_sup(currentL, transactionList, min_support, freq)
        currentL = currentC
        k += 1

    def support(item):
        return float(freq[item]) / len(transactionList)
    output = []

    for key, value in L.items():
        output.extend([(list(item), support(item)) for item in value])

    return output

def subsets(ary):
    return chain(*[combinations(ary, i + 1) for i in range(ary)])

def join(itemset, length):
    return set([i.union(j) for i in itemset for j in itemset if len(i.union(j)) == length])

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: apriori <file_name> <minimum_support>")
        sys.exit(1)

    file_name = sys.argv[1]
    min_support = float(sys.argv[2]) / 100

    file_content = helper.read_file(file_name)
    table = helper.convert_string_to_table(file_content)
    clean_table = data.convert_table_to_boolean(table)
    trans = data.convert_table_to_trans(clean_table)

    frequent_patterns = apriori(trans, min_support)
    for fp in frequent_patterns:
        items, support = fp
        items = data.convert_cols_number_to_string(items)
        print("{ %s }" % ', '.join(map(str, items)), "->", support)
