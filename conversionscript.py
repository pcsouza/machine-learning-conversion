
#conversionscript.py
#Patrick Souza
#script to convert .mat data files from the coursera machine learning 
#course to JSON files
#
#Usage:
#called with python conversionscript.py [*.mat datafile]
#this script will convert the .mat file into JSON format and save to directory


import scipy.io
import numpy
import sys
import json

file_name = sys.argv[1]
new_file_name = file_name[:-4] + ".json"

try:
	mat_data = scipy.io.loadmat(file_name)
except:
	print "Improper file specified in arguments"


converted_data = {}

for i in mat_data:
	if type(mat_data[i]) == numpy.ndarray:
		converted_data[i] = mat_data[i].tolist()
	else:
		converted_data[i] = mat_data[i]

file_handle = open(new_file_name, "w")
file_handle.write(json.dumps(converted_data))
file_handle.close


