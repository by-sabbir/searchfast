#!/usr/bin/env python
"""
	usage: simSearch [location] [search]
"""
import os
import sys


pathCount = 0
fileCount = 0
dirCount = 0
listOfFiles = []
fileCmd = ""

search = sys.argv[2].lower()
path = sys.argv[1]
file = os.walk(path)
count = 0


def cmd(cmd):
	os.system(cmd)

def linkCreator(links):
	link = links
	link = stringCheck(link)
	linkLst = link.split()
	created = ""
	strng = "\\ "
	index = []
	linkLen = len(linkLst) - 1
	for add in range(linkLen):
		created += linkLst[add] + strng
	created += linkLst[linkLen]

	return created


def stringCheck(strRec):
	this = ""
	sp_chars = "!@#$%^&*()_+{}[]=-;:\|,./"
	for strings in strRec:
		for each in strings:
			if "\'" in each:
				each = "\\'"
			# if " " in each:
			# 	each = "\ "
			if each in sp_chars:
				each = "\\" + each
			this += each
	return this


def openFile(pathToDir, file):
	global listOfFiles
	location = pathToDir + '/' + file
	listOfFiles.append(location)
	# print(listOfFiles)
	# cmd('nemo {}'.format(location))

def expandDir(item, searchStr=search):
	global dirCount
	for each in item:
		if search in each.lower():
			print(path)
			dirCount += 1
			each += ' *'
			print('\t', each)



def expandFile(item, searchStr=None):
	global fileCount
	for each in item:
		if search in each.lower():
			fileCount += 1
			print(fileCount, "| ", path)
			openFile(path, each)
			each += ' *'
			print('\t', each)
			print("\n")


for all in file:
	path = all[0]
	subDir = all[1]
	files = all[2]

	if search in path:
		print(path)
		pathCount += 1
	expandDir(subDir)
	expandFile(files)

print("\n_________________________________________\n")

print("       ------Search Result ------\n")

print("Search for: ", search)
print("All Hits -> ", pathCount+ dirCount + fileCount)

print("Path Match {} Dir Match {} File Match {}".format(pathCount, dirCount, fileCount))
print("\n_________________________________________\n")

# print(listOfFiles)

ans = input("Open All in File Manager? (y/n)")

if ans == 'y':
	for item in listOfFiles:
		item = linkCreator(item)
		fileCmd += item + ' '
	# print(fileCmd)
	cmd('nemo ' + fileCmd)
