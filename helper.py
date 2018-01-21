
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
