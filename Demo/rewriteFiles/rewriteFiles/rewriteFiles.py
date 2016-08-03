def main():
	try:
		oldFile11 = open('tranlog_11.txt', 'r')
		newFile11 = open('newTranlog_11.txt', 'w')

	except:
		print("Unable to open files.")
		raise

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
		file = oldFile11.read()
		tuples = file.split('\n\n')
		print(len(tuples))
		
		while counter < (len(tuples)-1) :
			lines = tuples[counter]
			print(lines)
			otherAttributes = lines.split('acc_path')
			rest = 'acc_path' + otherAttributes[1].lower()
			rest = rest.replace('acc_path','acc_Path').replace('copyid','copyId').replace('fieldname','fieldName').replace('fieldtype','fieldType').replace('fieldval','fieldVal').replace('fieldstat','fieldStat').replace('memofldval','memoFldVal').replace('genfldval','genFldVal').replace('tranuser','tranUser').replace('transtn','tranStn').replace(' = ','=').replace(',','')
			attributes = lines.split(' ')
			acctNo = attributes[10].replace(',','')
			currentAcctNo = acctNo
			time = attributes[7].replace(',','')
			timestamp = attributes[5] + ' ' + attributes[6] + ' ' + time
			currentTime = attributes[6]
			currentDate = attributes[5]
			currentComplement = time

			if currentAcctNo != oldAcctNo:
				oldAcctNo = currentAcctNo
				lineNumberForEachAcctNo += 1

			if currentTime == oldTime and currentDate == oldDate and currentComplement == oldComplement and currentAcctNo == oldAcctNo:
				lineNumber += 1 
				counter += 1
			else:
				newFile11.write(str(lineNumber) + ' ' + str(acctNo) + ' ' + str(lineNumberForEachAcctNo) + ' tranlog ' + str(timestamp) + ' # ' + str(rest) + '\n\n')
				oldTime = currentTime
				oldDate = oldDate
				oldComplement = currentComplement
				lineNumber += 1 
				counter += 1

	except:
		print("Error reading/writing files")
		raise

if __name__ == '__main__':

	main()