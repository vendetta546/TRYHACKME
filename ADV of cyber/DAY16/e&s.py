import zipfile
import os

count = 0

#Extract the primary file
with zipfile.ZipFile('final-final-compressed.zip','r') as zip_decom1:
	zip_decom1.extractall('decom1')

#read and extract each zip file to decom2
ListFile = os.listdir('decom1')
for l in ListFile:
	with zipfile.ZipFile('decom1/' + l,'r') as zip_decom2:
		zip_decom2.extractall('decom2')

# calculate the number of file (exclude .zip)
ListFile = os.listdir('decom2')
for l in ListFile:
	if 'zip' not in l:
		count = count + 1
print("Number of extracted file: " + str(count))
