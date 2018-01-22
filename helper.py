
list_of_strings = dict()

def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()

def write_file(file_name, file_content):
    with open(file_name, 'w') as f:
        f.write(file_content)

def convert_string_to_table(data, sep=','):
    return [line.split(sep) for line in data.split('\n')]

def convert_table_to_string(table, sep=','):
    return '\n'.join([','.join(line) for line in table])

def transpose(table):
    tableT = []
    for line in table:
        for i in range(len(line)):
            if len(tableT) < i+1:
                tableT.append([])
            tableT[i].append(line[i])
    return tableT

def is_int(x):
    return all(list(map(lambda c: c in "0123456789.", str(x))))

def unzip(iterable):
    left = list(map(lambda x: x[0], iterable))
    right = list(map(lambda x: x[1], iterable))
    return (left, right)