def main():
	try:
		oldFile11 = open('tranlog_11.txt', 'r')
		newFile11 = open('newTranlog_11.txt', 'w')

	except:
		print("Unable to open files.")
		raise

	try:
		lineNumber = 1
		line = oldFile11.readline()

		while line:
			print(line)
			newFile11.write('lineNumber: ' + str(lineNumber) + 'AcctNo: ' + 'lineNumberForEachAcctNo: ' + 'Timestamp: ' + otherAttributes)
			lineNumber += 1 
			line = oldFile11.readline()

	except:
		print("Error reading/writing files")
		raise

if __name__ == '__main__':

	main()