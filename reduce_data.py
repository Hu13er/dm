#!/bin/python3
#

import sys
import helper

def reduce_data(table, list_of_vars):
    tableT = helper.transpose(table)
    reduced_tableT = list(filter(lambda col: col[0] in list_of_vars, tableT))
    return helper.transpose(reduced_tableT)

def clean_data(table, types):
    def filter_nulls(row):
        for i, _ in enumerate(row):
            if types[i] == 'num' and (not helper.is_int(row[i])):
                return False
        return True

    return list(filter(filter_nulls, table))

def read_list_of_vars(file_name):
    return [line.strip().split('\t') for line in helper.read_file(file_name).strip().split('\n')]

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: filter <data_file_name> <list_of_vars_file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    list_of_vars_file_name = sys.argv[2]

    file_content = helper.read_file(file_name)
    table = helper.convert_string_to_table(file_content, sep=',')

    print("Orginal table rows:", len(table))
    list_of_vars = read_list_of_vars(list_of_vars_file_name)
    variables, types = helper.unzip(list_of_vars)
    table = reduce_data(table, variables)
    table = clean_data(table, types)
    print("Reduced and cleaned rows:", len(table))

    file_content = helper.convert_table_to_string(table)
    helper.write_file(file_name + ".new", file_content)
