def convert_table_to_boolean(table):
    def mapper(row):
        return list(map(lambda item: item != '0', row))
    return list(map(mapper, table))

def convert_table_to_trans(table=[]):
    trans = []
    for row in table:
        tran = filter(lambda item: item[1] == True, enumerate(row))
        tran = map(lambda item: item[0], tran)
        trans.append(list(tran))
    return trans
