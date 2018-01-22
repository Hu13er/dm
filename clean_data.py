#!/bin/python3
#

import sys
import os
import helper

def clean_data(table, threshold=70):
    tableT = helper.transpose(table)
#    print(list(map(lambda col: (col.count("NULL") / len(col), (threshold / 100)), tableT)))
    cleaned_tableT = filter(lambda col: (col.count("NULL") / len(col)) < (threshold / 100), tableT)
    return helper.transpose(cleaned_tableT)

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
