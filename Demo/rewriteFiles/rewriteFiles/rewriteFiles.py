def main():
	try:
		oldFile07 = open('tranlog_07.txt', 'r')
		newFile07 = open('newTranlog_07.txt', 'w')
		oldFile08 = open('tranlog_08.txt', 'r')
		newFile08 = open('newTranlog_08.txt', 'w')
		oldFile09 = open('tranlog_09.txt', 'r')
		newFile09 = open('newTranlog_09.txt', 'w')
		oldFile10 = open('tranlog_10.txt', 'r')
		newFile10 = open('newTranlog_10.txt', 'w')
		oldFile11 = open('tranlog_11.txt', 'r')
		newFile11 = open('newTranlog_11.txt', 'w')

	except:
		print("Unable to open files.")
		raise

	try:
		file07 = oldFile07.read()
		tuples07 = file07.split('\n\n')
		writeFile(tuples07, newFile07)
		tuples07.clear()
		file07 = []
		oldFile07.close()
		newFile07.close()

		file08 = oldFile08.read()
		tuples08 = file08.split('\n\n')
		writeFile(tuples08, newFile08)
		tuples08.clear()
		file08 = []
		oldFile08.close()
		newFile08.close()

		file09 = oldFile09.read()
		tuples09 = file09.split('\n\n')
		writeFile(tuples09, newFile09)
		tuples09.clear()
		file09 = []
		oldFile09.close()
		newFile09.close()

		file10 = oldFile10.read()
		tuples10 = file10.split('\n\n')
		writeFile(tuples10, newFile10)
		tuples10.clear()
		file10 = []
		oldFile10.close()
		newFile10.close()

		file11 = oldFile11.read()
		tuples11 = file11.split('\n\n')
		writeFile(tuples11, newFile11)
		tuples11.clear()
		file11 = []
		oldFile11.close()
		newFile11.close()

	except:
		print("Error reading files")
		raise

def writeFile(tuples, file):
	try:
		lineNumber = 1
		counter = 0
		lineNumberForEachAcctNo = 0
		currentAcctNo = 0
		oldAcctNo = 0
		currentTime = 0
		currentDate = 0
		currentComplement = 0
		oldTime = 0 
		oldDate = 0
		oldComplement = 0

		while counter < (len(tuples)-1) :
			lines = tuples[counter]
			print(lines)
			otherAttributes = lines.split('acc_path')
			rest = 'acc_path' + otherAttributes[1].lower()
			rest = rest.replace('acc_path','acc_Path').replace('copyid','copyId').replace('fieldname','fieldName').replace('fieldtype','fieldType').replace('fieldval','fieldVal').replace('fieldstat','fieldStat').replace('memofldval','memoFldVal').replace('genfldval','genFldVal').replace('tranuser','tranUser').replace('transtn','tranStn').replace(' = ','=').replace(',','')
			
			beginning = rest.find('fieldVal') # replacing blank spaces for underscores
			beginning += 9
			ending = rest.find(' fieldStat')
			restAttr = rest[0:beginning]
			while beginning < ending:
				if rest[beginning] == ' ':
					restAttr = restAttr + '_'
				else:
					restAttr = restAttr + rest[beginning]
				beginning += 1
			restAttr = restAttr + rest[ending:]

			attributes = lines.split(' ')
			acctNo = attributes[10].replace(',','')
			currentAcctNo = acctNo
			time = attributes[7].replace(',','')
			timestamp = attributes[5] + ' ' + attributes[6] + ' ' + time
			currentTime = attributes[6]
			currentDate = attributes[5]
			currentComplement = time

			if currentTime == oldTime and currentDate == oldDate and currentComplement == oldComplement and currentAcctNo == oldAcctNo:
				counter += 1
			else:
				if currentAcctNo != oldAcctNo:
					oldAcctNo = currentAcctNo
					lineNumberForEachAcctNo += 1

				file.write(str(lineNumber) + ' ' + str(acctNo) + ' ' + str(lineNumberForEachAcctNo) + ' tranlog ' + str(timestamp) + ' # ' + str(restAttr) + '\n\n')
				oldTime = currentTime
				oldDate = currentDate
				oldComplement = currentComplement
				lineNumber += 1 
				counter += 1

	except:
		print('Error writting the files.')
		raise

if __name__ == '__main__':

	main()