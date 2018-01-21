#!/bin/python3
#

import sys
import os
import helper

def transpose(table):
    tableT = []
    for line in table:
        for i in range(len(line)):
            if len(tableT) < i+1:
                tableT.append([])
            tableT[i].append(line[i])
    return tableT

def clean_data(table, threshold=70):
    tableT = transpose(table)
    cleaned_tableT = filter(lambda col: col.count("NULL") / len(col) < threshold, tableT)
    return transpose(cleaned_tableT)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: filter <file_name> [<threshold>]")
        sys.exit(1)
    
    file_name = sys.argv[1]
    threshold = 70
    if len(sys.argv) == 3:
        threshold = int(sys.argv[2])

    file_content = helper.read_file(file_name)
    table = helper.convert_string_to_table(file_content, sep=',')
    table = clean_data(table, threshold=threshold)
    file_content = helper.convert_table_to_string(table)
    os.rename(file_name, file_name + ".backup")
    helper.write_file(file_name, file_content)