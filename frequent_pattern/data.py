import helper
import itertools

def convert_table_to_boolean(table):
    def mapper(row):
        return map(lambda item: item != '0', row)
    return list(map(mapper, table))

def convert_table_to_trans(table):
    transactions = []
    for row in table:
        transaction = filter(lambda item: item[1] is True, enumerate(row))
        transaction = map(lambda item: item[0], transaction)
        transactions.append(list(transaction))
    return transactions

def convert_cols_number_to_string(cols_number):
    order = """
            PCIP01 PCIP03 PCIP04 PCIP05
            PCIP09 PCIP10 PCIP11 PCIP12
            PCIP13 PCIP14 PCIP15 PCIP16
            PCIP19 PCIP22 PCIP23 PCIP24
            PCIP25 PCIP26 PCIP27 PCIP29
            PCIP30 PCIP31 PCIP38 PCIP39
            PCIP40 PCIP41 PCIP42 PCIP43
            PCIP44 PCIP45 PCIP46 PCIP47
            PCIP48 PCIP49 PCIP50 PCIP51
            PCIP52 PCIP54"""
    order = [line.split() for line in order.strip().split('\n')]
    order = itertools.chain(*order)
    order = [word.strip() for word in order]

    return [order[i] for i in cols_number]
