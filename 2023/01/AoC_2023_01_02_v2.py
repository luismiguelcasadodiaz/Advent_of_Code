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
keys = {'1':'1', '2':'2', '3':'3', '4':'4', '5':'5', \
		'6':'6', '7':'7', '8':'8', '9':'9', '0':'0', \
		'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', \
		'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}



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
					line_digits.append((value,i))
		line_digits_sort = sorted(line_digits,key= lambda x: x[1])
		line_calibration = line_digits_sort[0][0] + line_digits_sort[-1][0]
		line_value = int(line_calibration)
		print(line.strip(),"",  line_digits_sort,line_value)
		line_calibration = ""
		line_digits = []
		total = total + line_value
	print("Total is {}".format(total))
