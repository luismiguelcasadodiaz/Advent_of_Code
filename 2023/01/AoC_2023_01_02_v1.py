#!/home/luis/miniconda3/bin/python

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    AoC_2023_01.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: luicasad <luicasad@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/02 03:04:59 by luicasad          #+#    #+#              #
#    Updated: 2023/12/02 03:04:59 by luicasad         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
keys = {'1':('1',1), '2':('2',1), '3':('3',1), '4':('4',1), '5':('5',1), \
		'6':('6',1), '7':('7',1), '8':('8',1), '9':('9',1), '0':('0',1), \
		'one':('1',3), 'two':('2',3), 'three':('3',5), 'four':('4',4), 'five':('5',4), \
		'six':('6',3), 'seven':('7',5), 'eight':('8',5), 'nine':('9',4)}


def	key_in_line(s:str,k:str)->int:
	"""
		Checks if key k is in string s.

		Retunrs:
		if K is not in s -1
		if k is in S the starting pos in s.
	"""
	s_len = len(s)
	k_len = len(k)
	i_s = 0
	while (i_s < s_len):
		found = 1
		i_k = 0
		while found and (i_k < k_len):
			if s[i_s + i_k] != k[i_k]:
				found = 0
			i_k = i_k + 1
		if found:
			return (i_s)
		i_s = i_s + 1
	return (-1)


pos = 0
total = 0
line_digits = []
line_calibration = ""
line_value = 0
with open("input2.txt","r") as f:
	lines = f.readlines()

	for line in lines:
		for i, c in enumerate(line):
			for key, value in keys.items():
				if line[i:].startswith(key):
					line_digits.append((value[0],i))
		line_digits_sorted=sorted(line_digits, key= lambda x: x[1])
		line_calibration = line_digits_sorted[0][0] + line_digits_sorted[-1][0]
		line_value = int(line_calibration)
		line_calibration = ""
		line_digits = []
		print(line_value, end=", ")
		total = total + line_value
	print("Total is {}".format(total))
