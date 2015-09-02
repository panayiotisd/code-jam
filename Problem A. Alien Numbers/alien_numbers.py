'''***************************************************************************
  Name 		  : alien_numbers.py
  Version     : 1.0
  Author(s)   : Panayiotis Danassis (panayiotis.dn [at] gmail [dot] com)
  Date        : September 2, 2015
  Language    :	Python
  Description : Solution to the Problem A: "Alien Numbers" of the Google's
  				Code Jam Practice Problems
  				Usage: python alien_numbers.py <input file> <output file>
  -----------
  Copyright (C) 2015  Panayiotis Danassis
****************************************************************************'''

import sys
# Function Declarations
def convertToDec(number, source_language):
	# Converts the given number from the source_language to decimal number
	result = 0
	base = len(source_language)
	for pos, digit in enumerate(reversed(number)):
		result += (base ** pos) * source_language.find(digit)
	return result

def convertToArbitraryLanguage(number, target_language):
	# Converts the given decimal number to a string of the target_language
	result = ""
	base = len(target_language)
	while number > 0:
		remainder = number % base
		number /= base
		result += target_language[remainder]
	return result[::-1]

# Main Routine
with open(sys.argv[1], 'r') as input_file:
	with open(sys.argv[2], 'w') as output_file:
		N = int(input_file.readline())
		cases = [x.replace("\n", "") for x in input_file]
		for index, case in enumerate(cases):
			#print index, case
			case = case.split(" ")
			number, source_language, target_language = case[0], case[1], case[2]
			number = convertToDec(number, source_language)
			number_in_target_language = convertToArbitraryLanguage(number, target_language)
			output_file.write("Case #%s: %s\n" % (str(index + 1), number_in_target_language))