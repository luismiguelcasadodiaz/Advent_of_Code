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
total = 0
line_digits = []
line_calibration = ""
line_value = 0
with open("input.txt","r") as f:
	lines = f.readlines()

	for line in lines:
		for i, c in enumerate(line):
			# gather numeric chars	
			if '0' <= c and c <= '9':
				line_digits.append(c)
		line_calibration = line_digits[0] + line_digits[-1] 
		line_value = int(line_calibration)
		line_calibration = ""
		line_digits = []
		print(line_value)
		total = total + line_value
	print("Total is {}".format(total))
