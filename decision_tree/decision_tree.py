import helper
import sys


working = ['low', 'medium', 'high']
income = ['low', 'high']
affiliation = ['HBCU', 'PBI', 'ANNHI', 'TRIBAL', 'AANAPII', 'HSI', 'NANTI', 'NORMAL']
city = set()

def update_city_list(ary):
	for item in ary:
		city.add(item)


def create_main_table(table):
	temp_table = []
	for row in table:
		city = row[0]

		for i in range(1, 14):
			row[i] = float(row[i])

		affil = affiliation[7]
		for i in range(1, 8):
			affil = affiliation[i - 1] if row[i] == 1 else affil


		working = row[8]
		income_low = row[9]
		income_hgh = row[10] + row[11] + row[12] + row[13]

		temp_table.append([city, affil, income_low, income_hgh, working])

	return temp_table


def create_main_node(tableT, table):
	income_low_average = helper.mean(tableT[2])
	income_hgh_average = helper.mean(tableT[3])
	working_seAk = helper.seAk(tableT[4])

	node = Node()

	for row in table:
		city = row[0]
		affil = row[1]
		income = 'low' if row[3] < income_hgh_average else 'high'
		working = 'low' if row[4] < working_seAk[0] else ('high' if row[4] < working_seAk[1] else 'medium')
		
		node.vec.append((city, affil, income, working))

	return node


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: filter <data_file_name> <list_of_vars_file_name>")
		sys.exit(1)

	file_name = sys.argv[1]

	file_content = helper.read_file(file_name)
	temp_table = helper.convert_string_to_table(file_content, sep=',')

	table = create_main_table(temp_table)
	tableT = helper.transpose(table)

	update_city_list(tableT[0])

	main_node = create_main_node(tableT, table)


class Node():
	def __init__(self):
		self.vec = list()
		self.if_then_rule = list()