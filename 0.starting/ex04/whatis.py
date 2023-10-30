"""Script that takes a number as argument, checks whether it is odd or even,
and prints the result."""

import sys

if len(sys.argv) < 1:
	sys.exit(1)
try:	
	if len(sys.argv) > 1:
		raise AssertionError("More than one argument is provided")


	if...._
		raise ....
		
except AssertionError as error:
	print("error")
	sys.exit(1)

# try:
# 	sys.exit(0)
# assert len(sys.argv) > 1, "ERROR"
