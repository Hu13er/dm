#!/bin/python3
#

import helper
import sys
import math
import copy




################################################################
################################################################

class Node():
	def __init__(self, vec=[], if_then_rule=[]):
		self.vec = vec
		self.if_then_rule = if_then_rule


if_then_rules = []

def create_if_then_rule(node):
	names = ['city', 'affiliation', 'income']

	str = 'IF '

	ary = node.if_then_rule
	data_set = node.vec

	for i in range(len(ary)):
		if i % 2 == 1:
			continue
		str += " {} = {},".format(names[ary[i]], ary[i + 1])

	str += " THEN"

	for val in working:
		s = 0
		for row in data_set:
			if val == row[3]:
				s += 1
		value = 0 if s == 0 else s * 100 / len(data_set)
		str += " {}_per = {}".format(val, value)

	if_then_rules.append(str)


def info(data_set):
	inf = 0
	for work in working:
		s = 1
		for row in data_set:
			if work == row[3]:
				s += 1
		div = 0.0001 if len(data_set) == 0 else len(data_set)
		p = s / div
		inf += p * math.log(p)
	return -inf


def info_A(data_set, num):
	infA = 0

	for val in attribute[num]:
		temp_data = []
		for row in data_set:
			if val == row[num]:
				temp_data.append(row)

		div = 0.0001 if len(data_set) == 0 else len(data_set)
		infA += info(temp_data) * len(temp_data) / div

	return infA


def split_info_A(data_set, num):
	split = 0

	for val in attribute[num]:
		s = 1
		for row in data_set:
			if val == row[num]:
				s += 1

		p = s / (0.00001 if len(data_set) == 0 else len(data_set))

		split += p * math.log(p, 2) * 5

	if split == 0:
		return 1
	return -split


def attribute_selection(data_set, applied):
	mx = 0
	index = -1
	main_info = info(data_set)

	# print("applied" , applied)

	for i in range(len(attribute)):
		if i in applied:
			continue
		# print('i ==========================  ', i)
		split_A = split_info_A(data_set, i)
		info_a = info_A(data_set, i)

		gain_A = main_info - info_a
		gain_ration_A = gain_A / split_A

		# print(gain_ration_A, gain_A, split_A, info_a, main_info)

		if gain_ration_A > mx:
			mx = gain_ration_A
			index = i

	return index


def decision(node, applied):
	data_set = copy.deepcopy(node.vec)
	select = attribute_selection(data_set, applied)

	# print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
	# print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
	# print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

	# print(data_set)

	# print('----------------------')
	# print('----------------------')
	# print('----------------------')

	# print(node.if_then_rule)

	if select == -1:
		create_if_then_rule(node)
		return

	for val in attribute[select]:
		child_data = []
		for row in data_set:
			if row[select] == val:
				child_data.append(row)

		child_if_then = copy.deepcopy(node.if_then_rule)
		child_if_then.append(select)
		child_if_then.append(val)

		app = copy.deepcopy(applied)
		app.append(select)

		decision(Node(vec = child_data, if_then_rule = child_if_then), app)


############################################################
############################################################


working = ['low', 'medium', 'high']
income = ['low', 'high']
affiliation = ['HBCU', 'PBI', 'ANNHI', 'TRIBAL', 'AANAPII', 'HSI', 'NANTI', 'NORMAL']
city = set()
attribute = [city, affiliation, income]

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

	decision(main_node, [])

	for rule in if_then_rules:
		print(rule)






 