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
